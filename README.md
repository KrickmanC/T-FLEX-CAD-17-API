# tflex_api

LLM-friendly copy of the T-FLEX CAD 17 API documentation prepared from a local installation.

## Tags

`t-flex-cad` `tflex` `cad-api` `open-api` `dotnet-api` `chm` `xml-docs` `jsonl` `markdown` `llm` `rag`

## Contents

- `raw/` — original copied documentation files from `C:\Program Files\T-FLEX CAD 17\Program`:
  - `TFlexAPI.chm`
  - `TFlexAPI.xml`
  - `TFlexAPI3D.xml`
  - `TFlexAPIData.xml`
  - `TFlexCommandAPI.xml`
- `llm/symbols.jsonl` — compact machine-readable API reference, one XML documentation member per JSON line.
- `llm/types/` — Markdown pages grouped by API type/class and assembly.
- `llm/chm_pages.jsonl` — CHM pages extracted from `TFlexAPI.chm`, one page per JSON line.
- `llm/index.md` — generated index for LLM usage.
- `llm/manifest.json` — generated counts and source metadata.
- `scripts/convert_tflex_docs.py` — repeatable converter from `raw/` plus extracted CHM HTML into `llm/`.

## Generated Dataset

Current generated counts:

- API symbols: 17,929
- Type/class Markdown pages: 2,452
- CHM JSONL pages: 19,350

Assemblies:

- `TFlexAPI`: 9,271 symbols
- `TFlexAPI3D`: 6,692 symbols
- `TFlexAPIData`: 119 symbols
- `TFlexCommandAPI`: 1,847 symbols

## Recommended LLM Usage

Use `llm/symbols.jsonl` for search, retrieval, indexing, and tool calls. Use `llm/types/*.md` when the model needs a whole class/type context. Use `llm/chm_pages.jsonl` for explanatory CHM content.

A `symbols.jsonl` record contains fields such as:

```json
{"id":"M:...","kind":"method","assembly":"TFlexAPI","namespace":"...","type":"...","name":"...","signature":"...","summary":"...","params":{},"returns":null}
```

## Regeneration

1. Put source files into `raw/`.
2. Extract CHM HTML with Windows Help:

```powershell
hh.exe -decompile .tmp_chm_extract raw\TFlexAPI.chm
```

3. Run the converter:

```powershell
python scripts\convert_tflex_docs.py --raw raw --out llm --chm-extract .tmp_chm_extract
```

4. Remove `.tmp_chm_extract` after conversion.

## Source

This repository was initialized from the public T-FLEX CAD 17 API documentation materials published in `dwnmf/tflex_api`.
