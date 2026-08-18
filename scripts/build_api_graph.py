#!/usr/bin/env python3
"""Build a static T-FLEX API graph from .NET assemblies and XML docs.

Reflection facts from TFlex*.dll are treated as structural facts. XML/LLM docs
are attached as documentation evidence and semantic hints.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


DEFAULT_ASSEMBLIES = [
    "TFlexAPI.dll",
    "TFlexAPI3D.dll",
    "TFlexAPIData.dll",
    "TFlexCommandAPI.dll",
]

SYSTEM_MEMBERS = {
    "Equals",
    "Finalize",
    "GetHashCode",
    "GetType",
    "MemberwiseClone",
    "ReferenceEquals",
    "ToString",
}

DANGEROUS_RE = re.compile(
    r"^(Add|Append|Apply|Begin|Build|Change|Clear|Close|Commit|Connect|Copy|"
    r"Create|Delete|Disable|Disconnect|Do|Edit|Enable|End|Execute|Exit|Export|"
    r"Import|Insert|Load|Move|New|Open|Paste|Rebuild|Redo|Remove|Rename|Reset|"
    r"Run|Save|Set|Start|Stop|Undo|Unload|Update|Write)",
    re.I,
)
SAFE_QUERY_RE = re.compile(r"^(Can|Check|Contains|Count|Find|Get|Has|Is|TryGet)", re.I)
API_PREFIXES = ("TFlex", "RGK", "RGPlatform", "Constraints2D", "PreciseGeometryUtils")


REFLECT_PS1 = r'''
param(
  [Parameter(Mandatory=$true)][string]$Root,
  [Parameter(Mandatory=$true)][string]$AssemblyNames
)
$ErrorActionPreference = "Stop"

[AppDomain]::CurrentDomain.add_AssemblyResolve({
  param($sender, $args)
  $name = (New-Object System.Reflection.AssemblyName($args.Name)).Name + ".dll"
  $candidate = Join-Path $Root $name
  if (Test-Path $candidate) {
    return [System.Reflection.Assembly]::LoadFrom($candidate)
  }
  return $null
})

function Type-Name($t) {
  if ($null -eq $t) { return $null }
  if ($t.IsByRef -or $t.IsPointer) { return (Type-Name $t.GetElementType()) }
  if ($t.IsArray) { return (Type-Name $t.GetElementType()) + "[]" }
  if ($t.IsGenericType) {
    $def = $t.GetGenericTypeDefinition().FullName -replace '`[0-9]+$',''
    $args = ($t.GetGenericArguments() | ForEach-Object { Type-Name $_ }) -join ","
    return "$def<$args>"
  }
  return $t.FullName
}

function Param-Record($p) {
  [ordered]@{
    name = $p.Name
    position = $p.Position
    type = (Type-Name $p.ParameterType)
    is_out = $p.IsOut
    is_in = $p.IsIn
    is_optional = $p.IsOptional
    has_default = $p.HasDefaultValue
  }
}

function Method-Signature($m) {
  $params = ($m.GetParameters() | ForEach-Object { Type-Name $_.ParameterType }) -join ","
  return "$($m.Name)($params)"
}

function Write-Record($obj) {
  $obj | ConvertTo-Json -Compress -Depth 12
}

$loaded = @()
foreach ($name in ($AssemblyNames -split '\|')) {
  $path = Join-Path $Root $name
  if (Test-Path $path) {
    $loaded += [System.Reflection.Assembly]::LoadFrom($path)
  }
}

$flags = [System.Reflection.BindingFlags]"Public,Instance,Static,DeclaredOnly"
foreach ($asm in $loaded) {
  Write-Record ([ordered]@{
    record_kind = "assembly"
    name = $asm.GetName().Name
    full_name = $asm.FullName
    version = $asm.GetName().Version.ToString()
    location = $asm.Location
  })

  try {
    $types = $asm.GetTypes()
  } catch [System.Reflection.ReflectionTypeLoadException] {
    $types = $_.Exception.Types | Where-Object { $null -ne $_ }
  }

  foreach ($t in $types) {
    if ($t.FullName -like "<*") { continue }
    $typeKind = "class"
    if ($t.IsEnum) { $typeKind = "enum" }
    elseif ($t.IsInterface) { $typeKind = "interface" }
    elseif ($t.IsValueType) { $typeKind = "struct" }
    elseif ($t.IsSubclassOf([System.Delegate])) { $typeKind = "delegate" }

    Write-Record ([ordered]@{
      record_kind = "type"
      assembly = $asm.GetName().Name
      full_name = $t.FullName
      name = $t.Name
      namespace = $t.Namespace
      type_kind = $typeKind
      is_public = ($t.IsPublic -or $t.IsNestedPublic)
      is_abstract = $t.IsAbstract
      is_sealed = $t.IsSealed
      base_type = (Type-Name $t.BaseType)
      interfaces = @($t.GetInterfaces() | ForEach-Object { Type-Name $_ })
    })

    if ($t.IsEnum) {
      foreach ($field in $t.GetFields([System.Reflection.BindingFlags]"Public,Static")) {
        Write-Record ([ordered]@{
          record_kind = "enum_value"
          assembly = $asm.GetName().Name
          declaring_type = $t.FullName
          name = $field.Name
          value = [int64]$field.GetRawConstantValue()
        })
      }
      continue
    }

    foreach ($ctor in $t.GetConstructors($flags)) {
      Write-Record ([ordered]@{
        record_kind = "member"
        assembly = $asm.GetName().Name
        declaring_type = $t.FullName
        name = "#ctor"
        member_kind = "constructor"
        signature = (Method-Signature $ctor)
        is_static = $ctor.IsStatic
        return_type = $null
        parameters = @($ctor.GetParameters() | ForEach-Object { Param-Record $_ })
      })
    }
    foreach ($method in $t.GetMethods($flags)) {
      if ($method.IsSpecialName) { continue }
      Write-Record ([ordered]@{
        record_kind = "member"
        assembly = $asm.GetName().Name
        declaring_type = $t.FullName
        name = $method.Name
        member_kind = "method"
        signature = (Method-Signature $method)
        is_static = $method.IsStatic
        return_type = (Type-Name $method.ReturnType)
        parameters = @($method.GetParameters() | ForEach-Object { Param-Record $_ })
      })
    }
    foreach ($prop in $t.GetProperties($flags)) {
      $getter = $prop.GetGetMethod($false)
      $setter = $prop.GetSetMethod($false)
      Write-Record ([ordered]@{
        record_kind = "member"
        assembly = $asm.GetName().Name
        declaring_type = $t.FullName
        name = $prop.Name
        member_kind = "property"
        signature = $prop.Name
        is_static = (($getter -and $getter.IsStatic) -or ($setter -and $setter.IsStatic))
        can_read = ($null -ne $getter)
        can_write = ($null -ne $setter)
        return_type = (Type-Name $prop.PropertyType)
        parameters = @($prop.GetIndexParameters() | ForEach-Object { Param-Record $_ })
      })
    }
    foreach ($field in $t.GetFields($flags)) {
      Write-Record ([ordered]@{
        record_kind = "member"
        assembly = $asm.GetName().Name
        declaring_type = $t.FullName
        name = $field.Name
        member_kind = "field"
        signature = $field.Name
        is_static = $field.IsStatic
        return_type = (Type-Name $field.FieldType)
        parameters = @()
      })
    }
    foreach ($event in $t.GetEvents($flags)) {
      Write-Record ([ordered]@{
        record_kind = "member"
        assembly = $asm.GetName().Name
        declaring_type = $t.FullName
        name = $event.Name
        member_kind = "event"
        signature = $event.Name
        is_static = $false
        return_type = (Type-Name $event.EventHandlerType)
        parameters = @()
      })
    }
  }
}
'''


def stable_hash(value: str, length: int = 12) -> str:
    return hashlib.sha1(value.encode("utf-8")).hexdigest()[:length]


def slug(value: str) -> str:
    value = re.sub(r"[^A-Za-z0-9_.:-]+", "_", value.strip())
    value = value.strip("_")
    return value or "unnamed"


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def add_edge(edges: dict[str, dict[str, Any]], edge: dict[str, Any]) -> None:
    basis = json.dumps(edge, ensure_ascii=False, sort_keys=True)
    edge.setdefault("id", f"edge:{stable_hash(basis, 16)}")
    edges[edge["id"]] = edge


def type_id(assembly: str, full_name: str) -> str:
    return f"type:{slug(assembly)}:{slug(full_name)}"


def member_id(record: dict[str, Any]) -> str:
    sig_hash = stable_hash(record.get("signature") or record["name"], 10)
    return (
        f"member:{slug(record['assembly'])}:{slug(record['declaring_type'])}."
        f"{slug(record['name'])}:{record['member_kind']}:{sig_hash}"
    )


def load_doc_symbols(path: Path) -> tuple[dict[str, dict[str, Any]], dict[tuple[str, str], dict[str, Any]], dict[tuple[str, str, str, str], list[dict[str, Any]]]]:
    by_id: dict[str, dict[str, Any]] = {}
    type_docs: dict[tuple[str, str], dict[str, Any]] = {}
    member_docs: dict[tuple[str, str, str, str], list[dict[str, Any]]] = defaultdict(list)
    if not path.exists():
        return by_id, type_docs, member_docs

    with path.open(encoding="utf-8") as fh:
        for line in fh:
            rec = json.loads(line)
            by_id[rec["id"]] = rec
            assembly = rec.get("assembly") or ""
            if rec.get("kind") == "type" and rec.get("type"):
                type_docs.setdefault((assembly, rec["type"]), rec)
            elif rec.get("type") and rec.get("name"):
                member_docs[(assembly, rec["type"], rec["name"], rec.get("kind") or "")].append(rec)
    return by_id, type_docs, member_docs


def reflect_records(root: Path, assemblies: list[str]) -> list[dict[str, Any]]:
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", suffix=".ps1", delete=False) as fh:
        fh.write(REFLECT_PS1)
        ps1 = Path(fh.name)
    try:
        cmd = [
            "powershell",
            "-NoProfile",
            "-ExecutionPolicy",
            "Bypass",
            "-File",
            str(ps1),
            "-Root",
            str(root),
            "-AssemblyNames",
            "|".join(assemblies),
        ]
        proc = subprocess.run(cmd, text=True, encoding="utf-8", capture_output=True, check=False)
        if proc.returncode != 0:
            raise RuntimeError(proc.stderr.strip() or proc.stdout.strip())
        records = []
        for line in proc.stdout.splitlines():
            if line.strip():
                records.append(json.loads(line))
        return records
    finally:
        try:
            ps1.unlink()
        except OSError:
            pass


def classify_risk(member: dict[str, Any]) -> tuple[str, str]:
    name = member["name"]
    if member["member_kind"] == "property":
        if member.get("can_write") and not member.get("can_read"):
            return "mutation", "write-only property"
        if member.get("can_write"):
            return "mixed", "property has setter"
        return "safe_read", "read-only property"
    if member["member_kind"] == "field":
        return "safe_read", "field access"
    if name in SYSTEM_MEMBERS:
        return "safe_read", "system member"
    if DANGEROUS_RE.search(name):
        return "mutation_or_external_effect", "name matches mutation/external-effect verb"
    if SAFE_QUERY_RE.search(name):
        return "likely_safe_read", "name matches query verb"
    return "unknown", "method risk not classified"


def normalize_type_name(name: str | None) -> str | None:
    if not name or name == "System.Void":
        return None
    name = re.sub(r"\[\]$", "", name)
    if "<" in name:
        name = name.split("<", 1)[0]
    return name


def is_api_type(full_name: str | None) -> bool:
    full_name = normalize_type_name(full_name)
    return bool(full_name and full_name.startswith(API_PREFIXES))


def source_inventory(root: Path, assemblies: list[str], raw_dir: Path, symbols_jsonl: Path) -> list[dict[str, Any]]:
    sources = []
    for name in assemblies:
        path = root / name
        if path.exists():
            sources.append({"kind": "assembly", "name": name, "path": str(path), "sha256": sha256_file(path)})
    for path in sorted(raw_dir.glob("TFlex*.xml")):
        sources.append({"kind": "xml_docs", "name": path.name, "path": str(path), "sha256": sha256_file(path)})
    if symbols_jsonl.exists():
        sources.append({"kind": "llm_symbols", "name": symbols_jsonl.name, "path": str(symbols_jsonl), "sha256": sha256_file(symbols_jsonl)})
    return sources


def build_graph(args: argparse.Namespace) -> tuple[dict[str, dict[str, Any]], dict[str, dict[str, Any]], dict[str, Any]]:
    doc_by_id, type_docs, member_docs = load_doc_symbols(args.symbols_jsonl)
    records = reflect_records(args.tflex_root, args.assembly)

    nodes: dict[str, dict[str, Any]] = {}
    edges: dict[str, dict[str, Any]] = {}
    counters: Counter[str] = Counter()
    known_types: dict[str, list[tuple[str, str]]] = defaultdict(list)

    for record in records:
        if record["record_kind"] == "type":
            known_types[record["full_name"]].append((record["assembly"], type_id(record["assembly"], record["full_name"])))

    for record in records:
        kind = record["record_kind"]
        if kind == "assembly":
            node_id = f"assembly:{slug(record['name'])}"
            nodes[node_id] = {"id": node_id, "kind": "assembly", **record}
            counters["assemblies"] += 1
            continue

        if kind == "type":
            tid = type_id(record["assembly"], record["full_name"])
            doc = type_docs.get((record["assembly"], record["full_name"]))
            nodes[tid] = {
                "id": tid,
                "kind": "type",
                "assembly": record["assembly"],
                "full_name": record["full_name"],
                "name": record["name"],
                "namespace": record.get("namespace"),
                "type_kind": record["type_kind"],
                "is_public": record["is_public"],
                "is_abstract": record["is_abstract"],
                "is_sealed": record["is_sealed"],
                "base_type": record.get("base_type"),
                "interfaces": record.get("interfaces") or [],
                "summary": doc.get("summary") if doc else None,
                "remarks": doc.get("remarks") if doc else None,
                "doc_symbol_id": doc.get("id") if doc else None,
                "source": "assembly_reflection",
            }
            add_edge(edges, {"from": f"assembly:{slug(record['assembly'])}", "to": tid, "kind": "defines_type", "source": record["assembly"]})
            if doc:
                doc_id = f"doc_symbol:{slug(doc['id'])}"
                nodes[doc_id] = {**doc, "id": doc_id, "kind": "doc_symbol", "doc_symbol_id": doc["id"]}
                add_edge(edges, {"from": tid, "to": doc_id, "kind": "documented_in", "source": str(args.symbols_jsonl)})
            counters["types"] += 1
            continue

        if kind == "enum_value":
            owner = type_id(record["assembly"], record["declaring_type"])
            eid = f"enum_value:{slug(record['assembly'])}:{slug(record['declaring_type'])}.{slug(record['name'])}"
            nodes[eid] = {"id": eid, "kind": "enum_value", **record}
            add_edge(edges, {"from": owner, "to": eid, "kind": "enum_value", "name": record["name"], "value": record["value"], "source": record["assembly"]})
            counters["enum_values"] += 1
            continue

        if kind != "member":
            continue

        mid = member_id(record)
        owner = type_id(record["assembly"], record["declaring_type"])
        risk, risk_reason = classify_risk(record)
        docs = member_docs.get((record["assembly"], record["declaring_type"], record["name"], record["member_kind"]), [])
        if not docs:
            # XML docs use kind=method for constructors and property for properties.
            alt_kind = "method" if record["member_kind"] == "constructor" else record["member_kind"]
            docs = member_docs.get((record["assembly"], record["declaring_type"], record["name"], alt_kind), [])
        doc = docs[0] if docs else None

        nodes[mid] = {
            "id": mid,
            "kind": "member",
            "assembly": record["assembly"],
            "owner": record["declaring_type"],
            "name": record["name"],
            "member_kind": record["member_kind"],
            "signature": record.get("signature"),
            "is_static": record.get("is_static"),
            "can_read": record.get("can_read"),
            "can_write": record.get("can_write"),
            "return_type": record.get("return_type"),
            "required_param_count": sum(1 for p in record.get("parameters") or [] if not p.get("is_optional")),
            "risk": risk,
            "risk_reason": risk_reason,
            "summary": doc.get("summary") if doc else None,
            "remarks": doc.get("remarks") if doc else None,
            "doc_symbol_id": doc.get("id") if doc else None,
            "source": "assembly_reflection",
        }
        add_edge(edges, {"from": owner, "to": mid, "kind": "has_member", "member": record["name"], "member_kind": record["member_kind"], "source": record["assembly"]})

        if doc:
            doc_id = f"doc_symbol:{slug(doc['id'])}"
            nodes[doc_id] = {**doc, "id": doc_id, "kind": "doc_symbol", "doc_symbol_id": doc["id"]}
            add_edge(edges, {"from": mid, "to": doc_id, "kind": "documented_in", "source": str(args.symbols_jsonl)})

        ret = normalize_type_name(record.get("return_type"))
        if ret and is_api_type(ret):
            targets = known_types.get(ret) or []
            for target_assembly, target_id in targets:
                add_edge(edges, {"from": mid, "to": target_id, "kind": "returns", "return_type": record.get("return_type"), "source": record["assembly"]})
                if record["member_kind"] in {"method", "property", "field"}:
                    add_edge(edges, {
                        "from": owner,
                        "to": target_id,
                        "kind": "api_transition",
                        "member": record["name"],
                        "member_id": mid,
                        "member_kind": record["member_kind"],
                        "risk": risk,
                        "required_param_count": sum(1 for p in record.get("parameters") or [] if not p.get("is_optional")),
                        "confidence": 0.95 if target_assembly == record["assembly"] else 0.8,
                        "confidence_reason": "assembly reflection return type",
                        "source": record["assembly"],
                    })
                    counters["api_transitions"] += 1

        for p in record.get("parameters") or []:
            pid = f"parameter:{stable_hash(mid + ':' + str(p.get('position')), 16)}"
            nodes[pid] = {"id": pid, "kind": "parameter", "owner_member_id": mid, **p}
            add_edge(edges, {"from": mid, "to": pid, "kind": "has_parameter", "index": p.get("position"), "source": record["assembly"]})
            ptype = normalize_type_name(p.get("type"))
            if ptype and is_api_type(ptype):
                for _, target_id in known_types.get(ptype, []):
                    add_edge(edges, {"from": pid, "to": target_id, "kind": "parameter_type", "source": record["assembly"]})
        counters["members"] += 1

    manifest = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "generator": "scripts/build_api_graph.py",
        "tflex_root": str(args.tflex_root),
        "symbols_jsonl": str(args.symbols_jsonl),
        "assembly_count": counters.get("assemblies", 0),
        "node_count": len(nodes),
        "edge_count": len(edges),
        "counters": dict(counters),
        "sources": source_inventory(args.tflex_root, args.assembly, args.raw_dir, args.symbols_jsonl),
    }
    return nodes, edges, manifest


def write_jsonl(path: Path, records: list[dict[str, Any]]) -> None:
    with path.open("w", encoding="utf-8", newline="\n") as fh:
        for record in records:
            fh.write(json.dumps(record, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n")


def write_seed_capabilities(path: Path) -> None:
    if path.exists():
        return
    seeds = [
        {
            "id": "get_application",
            "title": "Получить статический объект TFlex.Application",
            "status": "seed_unvalidated",
            "risk": "safe_read",
            "returns": "TFlex.Application",
            "requires_context": ["tflex_api_session"],
            "implementation_path": ["TFlex.Application"],
            "api_symbols": ["type:TFlexAPI:TFlex.Application"],
        },
        {
            "id": "get_active_document",
            "title": "Получить активный документ",
            "status": "seed_unvalidated",
            "risk": "safe_read",
            "returns": "TFlex.Model.Document",
            "requires_context": ["tflex_running", "document_opened"],
            "implementation_path": ["TFlex.Application.ActiveDocument"],
            "api_symbols": ["type:TFlexAPI:TFlex.Application", "type:TFlexAPI:TFlex.Model.Document"],
        },
        {
            "id": "get_documents_collection",
            "title": "Получить перечислитель открытых документов",
            "status": "seed_unvalidated",
            "risk": "safe_read",
            "returns": "TFlex.Documents",
            "requires_context": ["tflex_running"],
            "implementation_path": ["TFlex.Application.Documents"],
            "api_symbols": ["type:TFlexAPI:TFlex.Application", "type:TFlexAPI:TFlex.Documents"],
        },
    ]
    write_jsonl(path, seeds)


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--tflex-root",
        type=Path,
        default=Path(os.environ.get("TFLEX_ROOT", r"C:\Program Files\T-FLEX CAD 17\Program")),
        help="T-FLEX Program directory with TFlex*.dll.",
    )
    parser.add_argument("--symbols-jsonl", type=Path, default=Path("llm/symbols.jsonl"))
    parser.add_argument("--raw-dir", type=Path, default=Path("raw"))
    parser.add_argument("--out", type=Path, default=Path("graph"))
    parser.add_argument("--assembly", action="append", default=None, help="Assembly file name to reflect. Can be passed multiple times.")
    args = parser.parse_args(argv)
    if args.assembly is None:
        args.assembly = [name for name in DEFAULT_ASSEMBLIES if (args.tflex_root / name).exists()]
    return args


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    if not args.assembly:
        raise SystemExit(f"No T-FLEX assemblies found under {args.tflex_root}")

    nodes, edges, manifest = build_graph(args)
    args.out.mkdir(parents=True, exist_ok=True)
    write_jsonl(args.out / "static_nodes.jsonl", sorted(nodes.values(), key=lambda r: r["id"]))
    write_jsonl(args.out / "static_edges.jsonl", sorted(edges.values(), key=lambda r: r["id"]))
    with (args.out / "manifest.json").open("w", encoding="utf-8", newline="\n") as fh:
        json.dump(manifest, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    with (args.out / "source_inventory.json").open("w", encoding="utf-8", newline="\n") as fh:
        json.dump(manifest["sources"], fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    write_seed_capabilities(args.out / "capabilities.seed.jsonl")

    print(json.dumps({
        "out": str(args.out),
        "nodes": len(nodes),
        "edges": len(edges),
        "assemblies": manifest["assembly_count"],
        "api_transitions": manifest["counters"].get("api_transitions", 0),
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
