# Conformance # {#conformance}
This section defines the conformance classes of this specification and the criteria of each class.
An application is a **FAIR Data Point** if and only if it conforms to the FDP Core conformance class.
An application *MAY* additionally claim conformance to any of the other conformance classes for which it satisfies all criteria, provided that it also conforms to the classes they depend on ([[#capability-dependencies]]).

## Conformance classes ## {#conformance-classes}
### FDP Core ### {#conformance-core}
The FDP Core conformance class comprises the Read ([[#read]]) and Navigate ([[#navigate]]) capabilities.
It has no prerequisites.
An application conforms to FDP Core if it satisfies all of the following criteria:

1. Its root URL provides its own metadata record, conforming to the FAIR Data Point metadata schema ([[#fair-data-point-metadata]]), as specified in [[#read-root]].
2. Every metadata record is retrievable in at least RDF Turtle and JSON-LD, with RDF Turtle as the default, as specified in [[#read-records]].
3. Every metadata record states the class of the described entity, and the most specific class of the content model it specialises, as specified in [[#content-model]].
4. Every metadata record references its profile. Every profile is described with the Profiles Vocabulary and provides, as a validation resource, a metadata schema in SHACL whose target class is a class of the content model, as specified in [[#metadata-records]] and [[#read-schemas]].
5. Every metadata record has a retrievable FDP Metadata Record, as specified in [[#metadata-record]] and [[#read-metadata-records]].
6. Every metadata record of a catalog, if any, conforms to the catalog metadata schema ([[#catalog-metadata]]).
7. Every metadata record that leads to other metadata records provides navigation information, as specified in [[#navigation-information]].
8. Every metadata record is reachable from the root URL through the navigation information, as specified in [[#navigate-traversal]].
9. Requests that cannot be served are answered as specified in [[#read-errors]].

### FDP Write ### {#conformance-write}
The FDP Write conformance class comprises the Write capability ([[#write]]).
Its prerequisite is FDP Core.
An application conforms to FDP Write if it satisfies all of the following criteria:

1. Metadata records can be created, replaced, modified and deleted as specified in [[#write-create]], [[#write-update]] and [[#write-delete]].
2. Metadata schemas hosted by the application can be managed as specified in [[#write-schemas]].
3. Every written record is validated against its metadata schema, and rejected with a validation report when invalid, as specified in [[#write-validation]].
4. The FDP Metadata Record of every written record is maintained as specified in [[#write-create]] and [[#write-update]].
5. Write operations are authenticated and authorised as specified in [[#write-auth]].

### FDP Bundle Retrieval ### {#conformance-bundle-retrieval}
The FDP Bundle Retrieval conformance class comprises the retrieval half of the Bundle capability ([[#bundle]]).
Its prerequisite is FDP Core.
An application conforms to FDP Bundle Retrieval if it satisfies all of the following criteria:

1. The bundle of its own metadata record is retrievable as specified in [[#bundle-retrieval]], in the representations specified in [[#bundle-format]].
2. The bundle endpoints are discoverable as specified in [[#bundle-format]].

### FDP Bundle Submission ### {#conformance-bundle-submission}
The FDP Bundle Submission conformance class comprises the submission half of the Bundle capability ([[#bundle]]).
Its prerequisites are FDP Core and FDP Write.
An application conforms to FDP Bundle Submission if it satisfies all of the following criteria:

1. Bundles are accepted, validated and applied as specified in [[#bundle-submission]].
2. Every submission is answered with a report as specified in [[#bundle-submission]].

## Claiming conformance ## {#claiming-conformance}
An FDP declares the conformance classes it claims in its own metadata record, with the property `fdp-o:conformsToFdpSpec` ([[#fair-data-point-metadata]]).

Issue: **DP-6: Values of `fdp-o:conformsToFdpSpec`.**
Version 1.2 required a single value: a URL containing the version of the specification the FDP conforms to.
With several conformance classes, one value no longer suffices.
Options: (a) one value per claimed conformance class, being the IRI of the class in a versioned copy of this document, e.g. `https://specs.fairdatapoint.org/v2.0/#conformance-core`. (b) one value, the versioned URL of the specification, implying only FDP Core, and a separate property for the additional classes. (c) one value per class, using IRIs defined in the FDP ontology.
Proposed default: (a).

## Client conformance ## {#client-conformance}
A **FAIR Data Point client** is an application that consumes the metadata content of FDPs, such as a harvester, a search engine or a metadata editor.
This specification does not define a conformance class for clients, but a client that follows this specification:

- starts from the root URL of an FDP and discovers its content through the navigation information, as specified in [[#navigate-traversal]], without assuming a particular content structure.
- accepts RDF Turtle and *SHOULD* accept JSON-LD.
- ignores properties and classes it does not understand, rather than rejecting the record.
- honours the caching and conditional request mechanisms of [[#read-records]].
