# FAIR Data Point specification suite

Repository for the specifications of the FAIR Data Point (FDP). To see the HTML version, go to https://specs.fairdatapoint.org

Since version 2.0 the specifications are organised as a suite of documents, each defining one conformance class:

| Document | Source | Conformance class |
|---|---|---|
| Umbrella (suite overview, terminology, conformance model) | `index.bs` | — |
| FDP Core (mandatory) | `core/index.bs` | `…/v2.0/conformance/core` |
| FDP Records Management | `records/index.bs` | `…/v2.0/conformance/records` |
| FDP Schema Management | `schemas/index.bs` | `…/v2.0/conformance/schemas` |
| FDP Bulk Ingestion | `bulk/index.bs` | `…/v2.0/conformance/bulk` |

The FDP Discovery Participation module (the FDP-side obligations of the FAIR Discovery protocol) is in preparation and will be added as a further module.

Included assets (metadata tables, SHACL schemas, example RDF) live in `core/src/` — Bikeshed only allows includes from the spec's own folder or subfolders; images in `images/`. Documents are written in [Bikeshed](https://speced.github.io/bikeshed/); to build locally:

```
uv sync
uv run bikeshed spec index.bs
uv run bikeshed spec core/index.bs
uv run bikeshed spec records/index.bs
uv run bikeshed spec schemas/index.bs
uv run bikeshed spec bulk/index.bs
```

Previous versions of the specification are preserved under `v1.0/`, `v1.1/` and `v1.2/`.
