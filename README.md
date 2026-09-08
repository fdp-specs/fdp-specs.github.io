# FAIR Data Point specifications

Repository for the specifications of the FAIR Data Point (FDP). To see the HTML version, go to https://specs.fairdatapoint.org

The FDP specification describes the behaviour an application must exhibit in order to be considered a FAIR Data Point.
It is implementation-agnostic: documentation of the [FDP Reference Implementation (FDP-RI)](https://github.com/FAIRDataTeam/FAIRDataPoint), one particular implementation of the specification, lives in the FDP-RI repositories.

## Structure

The specification is a single [Bikeshed](https://speced.github.io/bikeshed/) document, [`index.bs`](index.bs), organised by FDP *capabilities* (Read, Navigate, Write, Bundle), each with its own conformance class.
For ease of editing, the sections are kept in separate files:

| Directory | Content |
| --- | --- |
| [`sections/`](sections/) | One Markdown file per section, included from `index.bs` in order |
| [`tables/`](tables/) | HTML tables of the metadata schemas |
| [`rdf/`](rdf/) | Normative SHACL shapes and Turtle examples, included verbatim in the document |
| [`images/`](images/) | Figures |
| `v1.0/`, `v1.1/`, `v1.2/` | Published previous versions |

Open design decisions are marked in the text as numbered decision points (`DP-n`) in issue blocks and collected in the Issues Index at the end of the document.

## Building locally

The project uses [uv](https://docs.astral.sh/uv/) to manage the Bikeshed toolchain:

```sh
uv run bikeshed spec index.bs
```

The generated `index.html` is committed to the repository and served by GitHub Pages.
