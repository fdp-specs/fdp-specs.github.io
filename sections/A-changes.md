# Changes since version 1.2 # {#changes}
*This appendix is non-normative.*

- The specification is organised in **capabilities** (Read, Navigate, Write, Bundle) with a **conformance class** for each ([[#capabilities]], [[#conformance]]).
    The former compliance criteria became the criteria of the FDP Core conformance class.
- The record-level properties `fdp-o:metadataIdentifier`, `fdp-o:metadataIssued` and `fdp-o:metadataModified` were removed from the metadata schemas.
    Meta-metadata is now carried by the **FDP Metadata Record** (`fdp-o:MetadataRecord`, also typed `dcat:CatalogRecord` for DCAT resources), see [[#metadata-record]].
- The requirement that every FDP exposes at least one catalog was relaxed. The catalog schema applies when catalogs are exposed ([[#catalog-metadata]], DP-4).
- The requirement that the target class of a metadata schema is a subclass of `dcat:Resource` was replaced by the requirement that it is a class of the content model, which includes `dcat:Distribution` and custom classes ([[#metadata-records]]).
- Metadata records must state the most specific class of the content model that they specialise ([[#content-model]], DP-3).
- The profile reference (`dcterms:conformsTo`) on metadata records is now required, resolving an inconsistency between the former compliance criteria and the schemas.
- Profiles are defined: a profile is described with the W3C Profiles Vocabulary and carries the SHACL metadata schema as a validation resource ([[#metadata-records]]).
- String-valued properties have explicit datatypes in the tables and shapes: `rdf:langString` for language-tagged text such as titles and descriptions, `xsd:string` otherwise.
- The `dct:` prefix was replaced by `dcterms:`, and the DCAT property names `dcat:endpointURL` and `dcat:endpointDescription` were corrected, following the DCAT namespaces and spelling.
- The SHACL schemas were made consistent with the tables and were corrected: missing prefixes, an invalid empty `sh:maxCount`, a duplicated property shape, an undefined shape reference and invalid `sh:nodeKind` values were fixed.
    Cross-record constraints (`sh:node` and `sh:class` on the IRIs of member records) were replaced by `sh:nodeKind sh:IRI`, since the members' triples are not part of the record being validated. The expected classes of members are stated in the tables.
- The container schema for the navigation information was generalised from the FAIR Data Point's catalog container to any container ([[#navigation-information]]).
- The metadata model figure was redrawn for DCAT 3 and the classes introduced in this version.
- The document type changed from an unofficial draft to a W3C Community Group Draft Report.
- The Write and Bundle capabilities are new and are published as first drafts, with open decision points.
