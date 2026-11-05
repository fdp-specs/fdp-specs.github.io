# Navigate capability # {#navigate}
The requirements in this section belong to the **Navigate** capability and are part of the FDP Core conformance class.
The Navigate capability depends on the Read capability ([[#read]]).
By providing this capability, an FDP enables client applications to discover its whole metadata content starting from the root URL, without prior knowledge of how the content is organised.
This is what allows, for instance, search engines and metadata aggregators to index the content of an FDP effortlessly.

## Overview ## {#navigate-overview}

*This section is non-normative.*

The FDP allows each deployment to define its own metadata schemas and its own structure of schemas: which classes of entities are described, and how their metadata records relate to one another.
For instance, an FDP may have the structure `FAIR Data Point` → `Catalog` → `Dataset` → `Distribution`.
Another FDP, serving metadata about ontologies, taxonomies and vocabularies, could have the structure `FAIR Data Point` → `Catalog` → `Semantic Artefact`.
As a consequence, different FDPs will in general not share the same structure, and no client can know beforehand how to navigate the content of an FDP it has not seen before.
Following every IRI in every record is not an option either, since records reference many resources that are not part of the content of the FDP.
Therefore, the FDP provides its navigation structure as it goes: each metadata record carries the information a client needs to reach the records below it, using the containment model of the Linked Data Platform (LDP) [[!LDP]].
A client needs nothing beyond the root URL, and it discovers the structure one step at a time, however the deployment has organised it.

## Navigation information ## {#navigation-information}
An FDP *MUST* describe the structure of its metadata content using LDP Direct Containers.

Every metadata record that leads to other metadata records *MUST* provide **navigation information**: for each relation that connects the described entity to member entities whose metadata records the FDP serves, an `ldp:DirectContainer` such that:

- its `ldp:membershipResource` is the IRI of the described entity.
- its `ldp:hasMemberRelation` is the relation that connects the described entity to its members, e.g., `fdp-o:metadataCatalog` for the relation between a FAIR Data Point and its catalogs, or `dcterms:hasPart` for the relation between a catalog and its members.
- its `ldp:contains` values are the IRIs of the metadata records of the members.

A metadata record that does not lead to other metadata records, i.e., a *leaf* of the content structure, has no navigation information.

The navigation information of a record *MUST* be included in the representation of the record ([[#read-records]]), so that a single request suffices to obtain both the record and the containers that lead to its members.
The IRI of each container *SHOULD* be dereferenceable, returning the description of the container.

The following table defines the schema of a container.

<pre class=include>
path: tables/table-navigation-information.html
</pre>

The container schema in SHACL:

<pre class=include-code>
path: rdf/shacl-container.ttl
highlight: turtle
</pre>

The following RDF Turtle code shows an example of a FAIR Data Point metadata record with its navigation information.

<pre class=include-code>
path: rdf/example-metadataservice.ttl
highlight: turtle
</pre>

In this example, the base IRI `https://example.fairdatapoint.org/fdp-api/` is the root URL of the FDP, and the other IRIs are written relative to it. The FDP, written as `<>`, has the relation `fdp-o:metadataCatalog` with its catalogs.
This is the parent-child relation that a client follows to navigate the metadata structure of the FDP.
The container `<catalog/>` at the bottom of the example makes the navigation structure explicit: it is the container for the FDP (the value of `ldp:membershipResource`), it relates the FDP to its contained members using the relation `fdp-o:metadataCatalog` (the value of `ldp:hasMemberRelation`), and it lists the members with `ldp:contains`.

## Traversing the content of an FDP ## {#navigate-traversal}
A client traverses the content of an FDP by retrieving the metadata record at the root URL ([[#read-root]]), retrieving the metadata record of every IRI listed in `ldp:contains` in the navigation information of each record, and repeating the procedure for each retrieved record.
Every metadata record served by an FDP *MUST* be reachable from the root URL through the navigation information, so that the traversal discovers the whole metadata content.

Clients *MUST NOT* assume a particular content structure, such as a fixed depth or a fixed sequence of classes, and *MUST* tolerate cycles in the navigation information, e.g., by keeping track of the records already visited.

## Large containers ## {#navigate-paging}
A container may list a large number of members.
An FDP *MAY* split the representation of such a container in pages, in which case it *SHOULD* follow LDP Paging [[LDP-PAGING]].

Issue: **DP-8: Paging of large containers.**
Options: (a) mandate LDP Paging for containers above a size that the FDP chooses. (b) recommend LDP Paging, as written above. (c) leave paging out of the specification and rely on the Bundle capability ([[#bundle]]) for large-scale retrieval.
Proposed default: (b).
