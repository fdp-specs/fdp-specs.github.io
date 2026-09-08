# Metadata model # {#metadata-model}
The requirements in this section apply to every metadata record served by an FDP.
They belong to the Read capability ([[#read]]) and are therefore part of the FDP Core conformance class.

The FAIR principles give special attention to metadata.
In fact, all principles relate to metadata in at least one aspect.
The most common definition of metadata is that it is data that provides information about other data.
Here we extend this notion to define metadata as data about other entities.
This metadata includes descriptions of the origin, structure, provenance, rights and obligations, or other characteristics of the described entities.

The FAIR Data Point's metadata approach follows this notion of supporting the creation and publication of metadata about different types of entities.
In the seminal paper presenting the FAIR principles [[FAIR-principles]], we have that computational agents should "*be capable of autonomously and appropriately acting when faced with the wide range of types, formats, and access-mechanisms/protocols that will be encountered during their self-guided exploration of the global data ecosystem*".
This requirement indicates that, to properly follow the FAIR principles, the FAIR Data Point not only supports the publication of FAIR-compliant metadata about datasets, but also about the service itself, as it should also follow the principles.

Consequently, the first entity to provide metadata about is the FDP itself.
When a client interacts with a service, it should know what it is dealing with.
Therefore, the FDP provides metadata about itself and, from that point on, the client can navigate its metadata content to discover the other metadata records.

## Content model ## {#content-model}
The FDP uses the W3C Data Catalog Vocabulary (DCAT) as the basis for its metadata content.
This version of the FDP specification adopts DCAT version 3 [[!VOCAB-DCAT-3]].
Figure 4.1 depicts the DCAT 3 classes and properties used by the FDP and the FDP extensions to the DCAT model.

<figure>
    <img src="images/FDPmetadatadiagram.svg" width="1580" height="1080" style="max-width:100%;height:auto" alt="Class diagram of the FDP metadata model: the DCAT 3 classes Resource, Catalog, Dataset, DatasetSeries, Distribution, DataService and CatalogRecord with their properties, the related vocabularies (foaf:Agent, skos:Concept, skos:ConceptScheme, vcard:Kind, dcat:Relationship), and the FDP ontology classes FAIRDataPoint, MetadataService and MetadataRecord with their relations to the DCAT classes.">
    <figcaption class="no-marker">**Figure 4.1** The FDP metadata model, based on DCAT 3. Cyan: DCAT 3 and other standard vocabularies. Green: FDP ontology. Only the classes and properties used in this specification are shown.</figcaption>
</figure>

A DCAT `Resource` represents an entity that can be described by a metadata record.
Since `Resource` is defined as an abstract class, it is not intended to be used directly.
One of its subclasses, such as `Dataset` or `DataService`, or a custom subclass, is used instead.
`Dataset` represents a collection of data, while `DataService` represents a service, accessible through an interface (API), that serves datasets.
`Catalog`, a subclass of `Dataset`, represents an aggregation of metadata records about digital objects. For instance, a `Catalog` may contain references to the metadata records of `Datasets`.
A `Distribution` represents an accessible form of a dataset, such as a downloadable file or an API endpoint.

Note: In DCAT, `Distribution` is *not* a subclass of `Resource`: a distribution is described as part of its dataset and is not catalogued in its own right.
In an FDP, however, every entity for which a metadata record is served, including distributions, is a first-class metadata record with its own IRI, its own schema and its own FDP Metadata Record (see [[#metadata-record]]).
This is why the FDP content model, defined below, is not limited to subclasses of `dcat:Resource`.

The FDP extends the DCAT model by adding the concept of a `FAIRDataPoint` as a specific subclass of data service that serves metadata catalogs and metadata records.
The DCAT extensions and other FDP-specific concepts and relations are defined in the FDP ontology (namespace prefix `fdp-o`).
In the FDP ontology, the FAIR Data Point is represented by a subclass of `MetadataService`, which in turn is a subclass of `dcat:DataService`.
What distinguishes a `MetadataService` from other data services is what it serves: where a `dcat:DataService` serves datasets (`dcat:servesDataset`), a `MetadataService` serves metadata records (`fdp-o:servesMetadata`, see [[#metadata-record]]).
In Figure 4.1, each class only lists the properties that are not already inherited from its superclasses. The class `fdp-o:MetadataRecord` and its relation to `dcat:CatalogRecord` are specified in [[#metadata-record]].

With the definition of the FDP as a specialisation of metadata service that serves metadata catalogs, the relation between the `MetadataService` and `dcat:Catalog` is represented by the predicate `fdp-o:metadataCatalog`.
Following the DCAT approach of providing qualified relations between resources, `fdp-o:metadataCatalog` is defined as a sub-property of `dcat:Relationship`, having `fdp-o:MetadataService` as its domain and `dcat:Catalog` as its range.

The **content model** of an FDP is the set of classes whose instances the FDP describes with metadata records.
It consists of:

- `fdp-o:FAIRDataPoint`, the class of the FDP itself.
- the DCAT classes `dcat:Catalog`, `dcat:Dataset`, `dcat:DatasetSeries`, `dcat:DataService` and `dcat:Distribution`.
- any further class for which the FDP provides a metadata schema (see [[#extending-the-content-model]]).

An FDP *MUST* serve the metadata record of itself, i.e., of an instance of `fdp-o:FAIRDataPoint` conforming to [[#fair-data-point-metadata]].
Metadata records of instances of every other class of the content model are optional.

Issue: **DP-4: Catalogs no longer mandatory.**
Version 1.2 required every FDP to expose at least one `dcat:Catalog`, directly related to the FDP through `fdp-o:metadataCatalog`.
Since the navigation information ([[#navigate]]) already tells a client which relation leads from a record to its members, the core does not need to hardcode the catalog as the first level of the content structure, and a minimal FDP that only publishes its own metadata is still useful, e.g., when newly deployed.
Options: (a) keep at least one catalog mandatory, as in version 1.2. (b) catalogs are optional, but when an FDP exposes catalogs they must conform to [[#catalog-metadata]]. (c) catalogs are optional and their schema is left entirely to the deployment.
Proposed default: (b), as reflected in this draft.

Every metadata record *MUST* state the class of the described entity with `rdf:type`.
In addition, when that class is a specialisation of a class of the content model, the record *MUST* also state the most specific class of the content model that it specialises, so that clients can interpret the record without inference over the ontologies.
For example, the metadata record of an FDP states both `fdp-o:FAIRDataPoint` and `dcat:DataService`.

Issue: **DP-3: Explicit DCAT parent classes.**
Without the rule above, a client only learns that an `fdp-o:FAIRDataPoint` is also a `dcat:DataService` (and a `dcat:Resource`) through inference over the FDP ontology, which plain SHACL validation and plain SPARQL queries do not perform.
The FDP Reference Implementation already states the parent classes explicitly.
Options: (a) records MUST state the most specific DCAT class in addition to the specialised class, as written above. (b) records MUST state the complete chain of parent classes up to `dcat:Resource`. (c) records SHOULD state the parent classes. (d) leave it to inference.
Proposed default: (a).

## Metadata records and profiles ## {#metadata-records}
A **metadata record** is the RDF description of one entity of the content model.
It is identified by the IRI of the described entity and is retrievable by dereferencing that IRI, as specified in [[#read]].

This specification mandates as few properties as possible in its metadata schemas: only what a client needs to identify, interpret and navigate a record.
Communities and deployments add further constraints, such as additional mandatory properties or controlled vocabularies, through the profiles their records conform to.

Each metadata record *MUST* reference, with `dcterms:conformsTo`, the **profile** it conforms to.
A profile is a named set of constraints on metadata records, identified by an IRI and described with the W3C Profiles Vocabulary [[!DX-PROF]]:

- the profile IRI identifies an instance of `prof:Profile`.
- the profile description *SHOULD* state, with `prof:isProfileOf`, the specifications or base profiles it constrains, e.g., DCAT or a community profile of DCAT.
- the profile description *MUST* include at least one resource descriptor (`prof:hasResource`, an instance of `prof:ResourceDescriptor`) with the role `role:validation` whose artifact (`prof:hasArtifact`) is the **metadata schema**, a SHACL shapes graph [[!SHACL]].
- the profile description *MAY* include further resource descriptors, e.g., with the role `role:guidance` for human-readable documentation.

Dereferencing the profile IRI *MUST* return the profile description, and dereferencing the artifact IRI of a validation resource *MUST* return the metadata schema (see [[#read-schemas]]).
SHACL is the only schema language of this specification. Other shape languages are out of scope.
Version 1.2 of this specification only recommended the profile reference while its schemas required it. This version resolves the inconsistency in favour of the requirement.

A metadata schema *MUST* declare, with `sh:targetClass`, a class of the content model of the FDP as the class of the entities it describes.
An FDP *MUST* provide a profile, and thereby a metadata schema, for every class of its content model of which it serves metadata records.

The following table defines the schema of a profile description.

<pre class=include>
path: tables/table-profile.html
</pre>

The profile description schema in SHACL:

<pre class=include-code>
path: rdf/shacl-profile.ttl
highlight: turtle
</pre>

Example of the profile description referenced by the FAIR Data Point metadata record of [[#navigation-information]]:

<pre class=include-code>
path: rdf/example-profile.ttl
highlight: turtle
</pre>
The schemas for the `fdp-o:FAIRDataPoint` and `dcat:Catalog` classes are defined in [[#fair-data-point-metadata]] and [[#catalog-metadata]]. Schemas for other classes are discussed in [[#extending-the-content-model]].

The normative shapes and the examples of this specification are published under the persistent namespace `https://w3id.org/fdp/specs-examples/`, which redirects to the files served together with this specification.
The IRI `https://w3id.org/fdp/specs-examples/v2.0/<file>` identifies the file as published with version 2.0 of this specification, and `https://w3id.org/fdp/specs-examples/<file>` the file as published with the latest version.
Each shape is identified by the IRI of its file followed by a fragment, e.g., `https://w3id.org/fdp/specs-examples/v2.0/shacl-fdp.ttl#FAIRDataPointShape`.
The shapes `AgentShape` and `ContactPointShape` are repeated in each file that needs them, so that every file is self-contained, and therefore have a file-specific IRI in each.

## FDP Metadata Record: meta-metadata ## {#metadata-record}
Two levels of description have to be distinguished: the metadata *about the entity* (e.g., the title, publisher and license of a dataset) and the metadata *about the metadata record itself* (e.g., when the record was created and last modified in this FDP, and by whom).
Previous versions of this specification mixed both levels by placing record-level properties (`fdp-o:metadataIdentifier`, `fdp-o:metadataIssued`, `fdp-o:metadataModified`) on the described entity.
This version separates them.

Every metadata record served by an FDP *MUST* have an associated **FDP Metadata Record**, an instance of `fdp-o:MetadataRecord`, that describes the registration of the entity in the FDP.
The FDP Metadata Record is itself a resource with its own IRI, retrievable as specified in [[#read-metadata-records]].
It is linked to the metadata record it describes with `fdp-o:isMetadataOf`, and the metadata record links back to it with `fdp-o:hasMetadata`.
The FDP Metadata Records served by an FDP are the values of its `fdp-o:servesMetadata` relation, which is what makes the FDP a `MetadataService` (see [[#content-model]]). This relation is not enumerated in the FDP metadata record, whose FDP Metadata Records are reached through the navigation information instead.

When the described entity is an instance of `dcat:Resource`, the FDP Metadata Record *MUST* additionally be typed as `dcat:CatalogRecord`, *MUST* additionally state `foaf:primaryTopic` with the same value as `fdp-o:isMetadataOf`, and, if the entity is a member of a catalog, the catalog *SHOULD* refer to it with `dcat:record`.
This makes the FDP Metadata Records of catalogued resources directly usable by DCAT-based harvesters and by DCAT application profiles.
Entities that are not DCAT resources, such as distributions or entities of custom classes, have an FDP Metadata Record without the `dcat:CatalogRecord` type, since DCAT restricts catalog records to catalogued resources.

Note: The FDP ontology already models this concept as `fdp-o:Metadata`, with the relations `fdp-o:isMetadataOf`, `fdp-o:hasMetadata` and `fdp-o:servesMetadata`, and with the deprecated date properties in its domain. `fdp-o:MetadataRecord` is the successor of `fdp-o:Metadata` under a clearer name. The ontology will be updated together with this version of the specification: `fdp-o:MetadataRecord` declared equivalent to `fdp-o:Metadata`, `fdp-o:isMetadataOf` and `fdp-o:hasMetadata` declared sub-properties of `foaf:primaryTopic` and `foaf:isPrimaryTopicOf`, and the record-level date properties deprecated.

The following table defines the schema of the FDP Metadata Record.

<pre class=include>
path: tables/table-metadata-record.html
</pre>

Issue: **DP-2: Location of the FDP Metadata Record.**
Options: (a) the FDP Metadata Record is a separate dereferenceable resource, linked from the metadata record with `fdp-o:hasMetadata` and advertised in the HTTP response with a `Link` header, as written in this draft. (b) the FDP Metadata Record is embedded in the representation of the metadata record, as a second subject in the same RDF document, and has no separate URL. (c) both: embedded in the representation and also dereferenceable.
Proposed default: (a), because it keeps one subject per response, allows caching and conditional requests to be driven by the record's `dcterms:modified`, and lets bundles ([[#bundle]]) carry records and their meta-metadata uniformly.

Issue: **DP-18: Relation of the FDP Metadata Record to the FDP ontology and to DCAT.**
The FDP ontology already has `fdp-o:Metadata` as a subclass of Dataset, linked to the described resource by `fdp-o:isMetadataOf` and `fdp-o:hasMetadata` and served by a `MetadataService` through `fdp-o:servesMetadata`. Three questions follow.
Which link properties: (a) the FDP ontology properties `fdp-o:isMetadataOf` and `fdp-o:hasMetadata`, declared sub-properties of `foaf:primaryTopic` and `foaf:isPrimaryTopicOf`, with `foaf:primaryTopic` stated explicitly when the record is a `dcat:CatalogRecord`, as written in this draft. (b) the FOAF properties only. (c) the FDP ontology properties only, relying on inference for DCAT tooling.
Which class: (a) `fdp-o:MetadataRecord` as the renamed successor of `fdp-o:Metadata`, as written. (b) keep the name `fdp-o:Metadata`.
Whether the record is a dataset: (a) `fdp-o:MetadataRecord` is not a subclass of `dcat:Dataset`, as written, so that records do not need records of their own and do not clash with the DCAT distinction between catalog records and catalogued resources. (b) `fdp-o:MetadataRecord` is a subclass of `dcat:Dataset`, as `fdp-o:Metadata` was, which makes `fdp-o:servesMetadata` a sub-property of `dcat:servesDataset` and a `MetadataService` a `DataService` by construction, at the cost of exempting records from the rule that every resource has a record.
Proposed default: (a) for all three.

The FDP Metadata Record schema in SHACL:

<pre class=include-code>
path: rdf/shacl-metadata-record.ttl
highlight: turtle
</pre>

Example of the FDP Metadata Record of a FAIR Data Point:

<pre class=include-code>
path: rdf/example-metadata-record.ttl
highlight: turtle
</pre>

## FAIR Data Point metadata ## {#fair-data-point-metadata}
The metadata record of the FDP itself is the only mandatory record of an FDP and the entry point for every client.
It describes the FDP as a `dcat:DataService`, and it is the root from which the navigation information ([[#navigate]]) leads to the other records.

<pre class=include>
path: tables/table-fdp-metadata.html
</pre>

Issue: **DP-7: Contact point on the FAIR Data Point.**
`dcat:contactPoint` with a `vcard:Kind` value is the only property in the FDP schema that requires the vCard vocabulary.
Options: (a) keep it, with the `ContactPointShape` below. (b) drop it in favour of the publisher's contact information. (c) keep it without constraining the shape of the value.
Proposed default: (a), because DCAT 3 defines `dcat:contactPoint` as the standard way of giving contact information for a resource and DCAT-based tooling expects a vCard value. The shape only requires an e-mail address, which is the minimum a client needs to act on the contact point.

The FAIR Data Point metadata schema in SHACL:

<pre class=include-code>
path: rdf/shacl-fdp.ttl
highlight: turtle
</pre>

## Catalog metadata ## {#catalog-metadata}
An FDP *MAY* organise the metadata records of other entities in catalogs.
When an FDP serves metadata records of instances of `dcat:Catalog`, these records *MUST* conform to the following schema (see DP-4 in [[#content-model]]).

<pre class=include>
path: tables/table-catalog-metadata.html
</pre>

The catalog metadata schema in SHACL:

<pre class=include-code>
path: rdf/shacl-catalog.ttl
highlight: turtle
</pre>

## Extending the content model ## {#extending-the-content-model}
Beyond the FAIR Data Point and Catalog schemas, the metadata structure of an FDP varies from deployment to deployment.
As the FDP is most commonly used to provide metadata of datasets, implementations typically also provide, following the DCAT model, metadata schemas for `dcat:Dataset` and `dcat:Distribution`.
An FDP *MAY* replace or complement these with schemas for further classes of its content model, including classes that are not part of DCAT, e.g., semantic artefacts, software or documents, as illustrated in [[#publishing-other-types-of-content]].
Every such schema is subject to the requirements of [[#metadata-records]]: it is identified by a profile IRI, it is expressed in SHACL and it declares its target class.

Note: The relations between metadata records of different classes are not fixed by this specification.
For instance, an FDP may organise its content as `FAIR Data Point` → `Catalog` → `Dataset` → `Distribution`, while another FDP serving metadata about ontologies may organise it as `FAIR Data Point` → `Catalog` → `Semantic Artefact`.
Whatever the organisation, each metadata record that leads to other metadata records provides the navigation information specified in [[#navigate]], so that clients can traverse the content without prior knowledge of its structure.
