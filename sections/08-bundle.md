# Bundle capability # {#bundle}
The requirements in this section belong to the **Bundle** capability and form the FDP Bundle Retrieval and FDP Bundle Submission conformance classes (see DP-1 in [[#capability-dependencies]]).
Bundle retrieval depends on the Read and Navigate capabilities. Bundle submission depends on the Write capability.
By providing this capability, an FDP enables bulk harvesting and indexing of its metadata content, bulk publication of metadata and the migration of metadata content between FDPs.

Advisement: This section is a first draft.
Its requirements are proposed for discussion and will be refined before this version of the specification is finalised.

## Overview ## {#bundle-overview}
*This section is non-normative.*

In the core capabilities, client applications interact with metadata records individually, navigating from one record to the next.
A **bundle** is a set of metadata records, together with their FDP Metadata Records and navigation information, exchanged in a single interaction.
The bundle of the FDP metadata record therefore comprises the whole metadata content of the FDP.

## Bundle representation ## {#bundle-format}
The bundle of a metadata record comprises the record itself, its FDP Metadata Record ([[#metadata-record]]), its navigation information ([[#navigation-information]]) and, recursively, the bundles of all the members listed in its navigation information.
A bundle *MUST* be an RDF document containing the triples of all metadata records, FDP Metadata Records and containers it comprises.
An FDP *MUST* support bundles in Turtle and JSON-LD and *MAY* support TriG [[TRIG]] or JSON-LD named graphs, with one named graph per metadata record.

Issue: **DP-14: Discovery and representation of bundles.**
Options for discovery: (a) the FDP advertises a bundle endpoint for each record that has members through an HTTP `Link` header on the record, with a relation type to be registered (provisionally the extension relation type `https://w3id.org/fdp/rel/bundle`), and through a property in the FDP metadata record. (b) bundles are obtained from the record IRI itself with a request parameter or a dedicated media type profile.
Options for representation: (i) a single RDF graph, which is lossless since records have disjoint subjects. (ii) an RDF dataset with one named graph per record, which preserves record boundaries explicitly.
Proposed default: (a) and (i), with (ii) optional.

## Bundle retrieval ## {#bundle-retrieval}
An FDP providing bundle retrieval *MUST* serve the bundle of its own metadata record, i.e., its whole metadata content, and *SHOULD* serve the bundle of every metadata record that has members.
Retrieval of a bundle is an HTTP `GET` request on the bundle endpoint, subject to the content negotiation rules of [[#read-records]].

The FDP *SHOULD* support incremental retrieval, returning only the records whose FDP Metadata Record has a `dcterms:modified` value later than an instant given by the client.

Issue: **DP-15: Incremental retrieval and deleted records.**
Incremental retrieval is only complete if a client can also learn which records were deleted since the given instant.
Options: (a) the FDP keeps a tombstone FDP Metadata Record for deleted records for a period it chooses, and includes them in incremental bundles. (b) incremental bundles only carry created and modified records and clients periodically perform a full retrieval. (c) incremental retrieval is not specified.
Proposed default: (a).

## Bundle submission ## {#bundle-submission}
An FDP providing bundle submission *MUST* accept an HTTP `POST` request with a bundle as its body on the bundle endpoint of a record that has members, and *MUST* create or replace the metadata records contained in the bundle as members of that record, applying the rules of [[#write]] to each of them, including validation ([[#write-validation]]) and authorization ([[#write-auth]]).
FDP Metadata Records and navigation information contained in a submitted bundle are informative: the FDP *MUST* generate the FDP Metadata Records and the navigation information of the created or replaced records itself, as specified in [[#write-create]] and [[#write-update]], and *MAY* use the submitted values of `dcterms:issued` to record the original creation time.

The response *MUST* be a report listing, for every metadata record in the bundle, whether it was created, replaced or rejected, and, for rejected records, the SHACL validation report or the reason for rejection.

Issue: **DP-16: Atomicity of bundle submission.**
Options: (a) a bundle is applied atomically: if any record is rejected, no record is created or replaced. (b) a bundle is applied record by record, and the report states the outcome of each. (c) the client chooses between (a) and (b) with a request parameter.
Proposed default: (c), with (b) as the default behaviour.
