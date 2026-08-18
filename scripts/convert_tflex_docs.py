#!/usr/bin/env python3
"""Convert T-FLEX CAD .NET XML docs and extracted CHM HTML into LLM-friendly files."""
from __future__ import annotations

import argparse
import hashlib
import html
import json
import re
import shutil
from collections import defaultdict
from dataclasses import dataclass
from html.parser import HTMLParser
from pathlib import Path
from typing import Iterable
import xml.etree.ElementTree as ET

KIND_BY_PREFIX = {
    "N": "namespace",
    "T": "type",
    "M": "method",
    "P": "property",
    "F": "field",
    "E": "event",
    "O": "overload",
}

SKIP_TAGS = {"script", "style", "noscript", "svg"}
BLOCK_TAGS = {
    "p", "div", "section", "article", "header", "footer", "main", "aside",
    "h1", "h2", "h3", "h4", "h5", "h6", "li", "tr", "table", "ul", "ol",
    "pre", "blockquote", "br", "hr", "dt", "dd",
}

@dataclass
class Symbol:
    id: str
    kind: str
    assembly: str
    namespace: str | None
    type: str | None
    name: str
    signature: str
    summary: str | None
    remarks: str | None
    params: dict[str, str]
    returns: str | None
    value: str | None
    examples: list[str]
    seealso: list[str]
    source_file: str


def clean_ws(text: str | None) -> str | None:
    if text is None:
        return None
    text = html.unescape(text)
    text = re.sub(r"\s+", " ", text).strip()
    return text or None


def element_text(el: ET.Element | None) -> str | None:
    if el is None:
        return None
    parts: list[str] = []
    if el.text:
        parts.append(el.text)
    for child in list(el):
        tag = child.tag.split("}")[-1]
        if tag in {"see", "seealso"}:
            cref = child.attrib.get("cref") or child.attrib.get("href") or child.attrib.get("langword")
            if cref:
                parts.append(f"`{cref}`")
        elif tag == "paramref":
            name = child.attrib.get("name")
            if name:
                parts.append(f"`{name}`")
        elif tag == "typeparamref":
            name = child.attrib.get("name")
            if name:
                parts.append(f"`{name}`")
        elif tag in {"code", "c"}:
            txt = "".join(child.itertext()).strip()
            if txt:
                parts.append(f"`{txt}`")
        else:
            txt = element_text(child)
            if txt:
                parts.append(txt)
        if child.tail:
            parts.append(child.tail)
    return clean_ws(" ".join(parts))


def split_params(member_tail: str) -> tuple[str, str | None]:
    if "(" not in member_tail or not member_tail.endswith(")"):
        return member_tail, None
    before, params = member_tail.rsplit("(", 1)
    return before, params[:-1]


def parse_member_id(member_id: str) -> tuple[str, str | None, str | None, str, str]:
    prefix = member_id[:1]
    kind = KIND_BY_PREFIX.get(prefix, "member")
    body = member_id[2:] if len(member_id) > 2 and member_id[1] == ":" else member_id

    if kind == "namespace":
        return kind, body, None, body.rsplit(".", 1)[-1], body

    if kind == "type":
        namespace = body.rsplit(".", 1)[0] if "." in body else None
        return kind, namespace, body, body.rsplit(".", 1)[-1], body

    base, raw_params = split_params(body)
    type_name = base.rsplit(".", 1)[0] if "." in base else None
    name = base.rsplit(".", 1)[-1]
    namespace = type_name.rsplit(".", 1)[0] if type_name and "." in type_name else None
    if raw_params is None:
        signature = name
    else:
        params = raw_params.replace("@", "ref ").replace("`0", "T")
        signature = f"{name}({params})"
    return kind, namespace, type_name, name, signature


def parse_xml_file(path: Path) -> tuple[str, list[Symbol]]:
    tree = ET.parse(path)
    root = tree.getroot()
    assembly = clean_ws(element_text(root.find("./assembly/name"))) or path.stem
    symbols: list[Symbol] = []
    for member in root.findall("./members/member"):
        member_id = member.attrib.get("name", "")
        kind, namespace, type_name, name, signature = parse_member_id(member_id)
        params = {}
        for p in member.findall("param"):
            pname = p.attrib.get("name")
            if pname:
                params[pname] = element_text(p) or ""
        examples = [t for t in (element_text(e) for e in member.findall("example")) if t]
        seealso = []
        for s in member.findall("seealso"):
            ref = s.attrib.get("cref") or s.attrib.get("href")
            if ref:
                seealso.append(ref)
        symbols.append(Symbol(
            id=member_id,
            kind=kind,
            assembly=assembly,
            namespace=namespace,
            type=type_name,
            name=name,
            signature=signature,
            summary=element_text(member.find("summary")),
            remarks=element_text(member.find("remarks")),
            params=params,
            returns=element_text(member.find("returns")),
            value=element_text(member.find("value")),
            examples=examples,
            seealso=seealso,
            source_file=path.name,
        ))
    return assembly, symbols


def as_json(symbol: Symbol) -> dict:
    return {
        "id": symbol.id,
        "kind": symbol.kind,
        "assembly": symbol.assembly,
        "namespace": symbol.namespace,
        "type": symbol.type,
        "name": symbol.name,
        "signature": symbol.signature,
        "summary": symbol.summary,
        "remarks": symbol.remarks,
        "params": symbol.params,
        "returns": symbol.returns,
        "value": symbol.value,
        "examples": symbol.examples,
        "seealso": symbol.seealso,
        "source_file": symbol.source_file,
    }


def safe_name(name: str) -> str:
    name = re.sub(r"[<>:\"/\\|?*\x00-\x1f]", "_", name)
    name = re.sub(r"\s+", "_", name).strip("._ ")
    return name[:180] or "unnamed"


def write_type_pages(symbols: list[Symbol], out_dir: Path) -> int:
    types_dir = out_dir / "types"
    if types_dir.exists():
        shutil.rmtree(types_dir)
    types_dir.mkdir(parents=True, exist_ok=True)
    by_type: dict[tuple[str, str], list[Symbol]] = defaultdict(list)
    for sym in symbols:
        key = sym.type if sym.kind != "type" and sym.type else (sym.id[2:] if sym.kind == "type" else "_global")
        by_type[(sym.assembly, key)].append(sym)

    for (assembly_key, type_name), items in sorted(by_type.items()):
        type_symbol = next((s for s in items if s.kind == "type"), None)
        namespace = (type_symbol.namespace if type_symbol else next((s.namespace for s in items if s.namespace), None)) or ""
        assembly = (type_symbol.assembly if type_symbol else items[0].assembly)
        lines = [f"# {type_name}", "", f"Assembly: `{assembly}`"]
        if namespace:
            lines += [f"Namespace: `{namespace}`"]
        if type_symbol and type_symbol.summary:
            lines += ["", "## Summary", "", type_symbol.summary]
        if type_symbol and type_symbol.remarks:
            lines += ["", "## Remarks", "", type_symbol.remarks]

        for kind in ["constructor", "method", "property", "event", "field", "member", "overload"]:
            group = [s for s in items if s.kind == kind or (kind == "constructor" and s.kind == "method" and s.name == "#ctor")]
            if not group:
                continue
            title = "Constructors" if kind == "constructor" else kind.capitalize() + "s"
            lines += ["", f"## {title}"]
            for s in sorted(group, key=lambda x: (x.name, x.id)):
                display = s.signature.replace("#ctor", type_name.rsplit('.', 1)[-1])
                lines += ["", f"### `{display}`", "", f"ID: `{s.id}`"]
                if s.summary:
                    lines += ["", s.summary]
                if s.params:
                    lines += ["", "Parameters:"]
                    for pname, ptext in s.params.items():
                        lines.append(f"- `{pname}`: {ptext}")
                if s.returns:
                    lines += ["", f"Returns: {s.returns}"]
                if s.value:
                    lines += ["", f"Value: {s.value}"]
                if s.remarks:
                    lines += ["", f"Remarks: {s.remarks}"]
                if s.examples:
                    lines += ["", "Examples:"]
                    for ex in s.examples:
                        lines.append(f"- {ex}")
        digest = hashlib.sha1(f"{assembly_key}:{type_name}".encode("utf-8")).hexdigest()[:8]
        (types_dir / f"{safe_name(assembly_key)}__{safe_name(type_name)}__{digest}.md").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    return len(by_type)


class HTMLToText(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.parts: list[str] = []
        self.skip_stack: list[str] = []
        self.title: str | None = None
        self._in_title = False

    def handle_starttag(self, tag: str, attrs):
        tag = tag.lower()
        if tag in SKIP_TAGS:
            self.skip_stack.append(tag)
            return
        if self.skip_stack:
            return
        if tag == "title":
            self._in_title = True
        if tag in BLOCK_TAGS:
            self.parts.append("\n")
        if tag in {"h1", "h2", "h3"}:
            self.parts.append("\n" + {"h1":"#", "h2":"##", "h3":"###"}[tag] + " ")
        if tag == "li":
            self.parts.append("- ")

    def handle_endtag(self, tag: str):
        tag = tag.lower()
        if self.skip_stack:
            if tag == self.skip_stack[-1]:
                self.skip_stack.pop()
            return
        if tag == "title":
            self._in_title = False
        if tag in BLOCK_TAGS:
            self.parts.append("\n")

    def handle_data(self, data: str):
        if self.skip_stack:
            return
        if self._in_title:
            t = clean_ws(data)
            if t:
                self.title = t
        self.parts.append(data)


def html_to_markdown(path: Path) -> tuple[str, str]:
    raw = path.read_bytes()
    text = None
    for enc in ("utf-8", "cp1251", "windows-1251"):
        try:
            text = raw.decode(enc)
            break
        except UnicodeDecodeError:
            continue
    if text is None:
        text = raw.decode("utf-8", errors="ignore")
    parser = HTMLToText()
    parser.feed(text)
    body = html.unescape("".join(parser.parts))
    body = re.sub(r"[ \t\r\f\v]+", " ", body)
    body = re.sub(r"\n{3,}", "\n\n", body)
    body = "\n".join(line.strip() for line in body.splitlines())
    body = re.sub(r"\n{3,}", "\n\n", body).strip()
    title = parser.title or clean_ws(re.sub(r"<[^>]+>", " ", text[:2000])) or path.stem
    return title, body


def write_chm_pages(chm_extract: Path | None, out_dir: Path) -> int:
    chm_dir = out_dir / "chm_pages"
    if chm_dir.exists():
        shutil.rmtree(chm_dir)
    jsonl_path = out_dir / "chm_pages.jsonl"
    if jsonl_path.exists():
        jsonl_path.unlink()
    if not chm_extract or not chm_extract.exists():
        return 0
    count = 0
    with jsonl_path.open("w", encoding="utf-8", newline="\n") as fh:
        for path in sorted(chm_extract.rglob("*")):
            if path.suffix.lower() not in {".htm", ".html"}:
                continue
            title, body = html_to_markdown(path)
            if len(body) < 40:
                continue
            rel = path.relative_to(chm_extract).as_posix()
            digest = hashlib.sha1(rel.encode("utf-8")).hexdigest()[:8]
            record = {
                "id": f"{safe_name(path.stem)}_{digest}",
                "title": title,
                "source_chm_path": rel,
                "content": body,
            }
            fh.write(json.dumps(record, ensure_ascii=False, separators=(",", ":")) + "\n")
            count += 1
    return count


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--raw", type=Path, default=Path("raw"))
    ap.add_argument("--out", type=Path, default=Path("llm"))
    ap.add_argument("--chm-extract", type=Path, default=None)
    args = ap.parse_args()

    raw = args.raw
    out = args.out
    out.mkdir(parents=True, exist_ok=True)

    all_symbols: list[Symbol] = []
    assemblies: dict[str, int] = {}
    for xml_path in sorted(raw.glob("*.xml")):
        assembly, symbols = parse_xml_file(xml_path)
        assemblies[assembly] = len(symbols)
        all_symbols.extend(symbols)

    with (out / "symbols.jsonl").open("w", encoding="utf-8", newline="\n") as fh:
        for sym in sorted(all_symbols, key=lambda s: s.id):
            fh.write(json.dumps(as_json(sym), ensure_ascii=False, separators=(",", ":")) + "\n")

    type_count = write_type_pages(all_symbols, out)
    chm_count = write_chm_pages(args.chm_extract, out)

    by_kind = defaultdict(int)
    by_namespace = defaultdict(int)
    for sym in all_symbols:
        by_kind[sym.kind] += 1
        if sym.namespace:
            by_namespace[sym.namespace] += 1

    manifest = {
        "project": "tflex_api",
        "source": "T-FLEX CAD 17 API documentation",
        "formats": {
            "raw": "Original copied CHM/XML files",
            "llm/symbols.jsonl": "One .NET XML documentation member per line",
            "llm/types/*.md": "Markdown pages grouped by API type/class",
            "llm/chm_pages.jsonl": "CHM HTML pages converted to compact JSONL, one page per line",
        },
        "assemblies": assemblies,
        "symbol_count": len(all_symbols),
        "type_page_count": type_count,
        "chm_page_count": chm_count,
        "symbol_kinds": dict(sorted(by_kind.items())),
        "top_namespaces": dict(sorted(by_namespace.items(), key=lambda kv: kv[1], reverse=True)[:50]),
    }
    (out / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    index = [
        "# T-FLEX CAD 17 API LLM Index",
        "",
        "This folder contains generated, LLM-friendly copies of T-FLEX CAD 17 API documentation.",
        "",
        "## Files",
        "",
        "- `symbols.jsonl` — compact machine-readable API reference, one symbol per JSON line.",
        "- `types/` — Markdown pages grouped by API type/class.",
        "- `chm_pages.jsonl` — CHM pages extracted from `TFlexAPI.chm`, one page per JSON line.",
        "- `manifest.json` — counts and source metadata.",
        "",
        "## Counts",
        "",
        f"- Symbols: {len(all_symbols)}",
        f"- Type pages: {type_count}",
        f"- CHM pages: {chm_count}",
        "",
        "## Assemblies",
        "",
    ]
    for assembly, count in sorted(assemblies.items()):
        index.append(f"- `{assembly}`: {count} symbols")
    (out / "index.md").write_text("\n".join(index).rstrip() + "\n", encoding="utf-8")

    return 0

if __name__ == "__main__":
    raise SystemExit(main())
