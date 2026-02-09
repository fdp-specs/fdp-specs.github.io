# Metadata

The FAIR principles give special attention to metadata.
In fact, all principles relate to metadata in at least one aspect.
Metadata can be defined as data that provides information about other data.
Here we extend this notion to define metadata as information about other digital objects.
This information includes descriptions of the origin, structure, provenance, rights and obligations, or other characteristics of digital objects.
The FAIR Data Point's metadata approach follows this idea of supporting the creation of metadata about different types of digital objects.
The first object to provide metadata about is the FDP itself.
When a client interacts with a service, it should know what it is dealing with.
Therefore, the FDP provides metadata about itself and, from that point on, the client can navigate its metadata content to discover the other metadata records.

The FDP uses the W3C's Data Catalog Vocabulaire (DCAT) version 2 [[vocab-dcat-2 obsolete]] model as the basis for its metadata content.
Figure 2 depicts the FDP extensions to the DCAT model.

<figure>
    <img src="images/FDPmetadatadiagram.png">
    <figcaption>FDP extensions to the DCAT model</figcaption>
</figure>

A DCAT `Resource` represents entities that can be described by a metadata record.
Since `Resource` is defined as an abstract class, it is not intended to be used directly.
We should use one of its subclasses, such as `Dataset` or `Data Service` instead.
`Dataset` represents a collection of data while `Data Service` represents a service, accessible through an interface (API), that serves datasets.
`Catalog`, a subclass of `Dataset`, represents aggregations of metadata records about digital objects.
For instance, a `Catalog` may contain references to the metadata records of `Datasets`.

The FDP extends the DCAT model by adding the concept of a `FAIRDataPoint` as a specific type of data service that serves metadata catalogs and metadata records.
The DCAT extensions and other FDP-specific concepts and relations are defined in the FDP ontology (using the namespace prefix `fdp-o`).
In the FDP ontology, the FAIR Data Point is represented by a sub-class of the concept of `MetadataService`.
Figure 4.1 only depicts the properties that are not already inherited from `Data Service` and `Resource`.

With the definition of the FDP as a type of metadata service that serves metadata catalogs, the relation between the `MetadataService` and `dcat:Catalog` is represented by the predicate `fdp-o:metadataCatalog`.
Following the DCAT approach of providing qualified relations between resources, the `fdp-o:metadataCatalog` is defined as a sub-property of `dcat:Relationship` having `fdp-o:MetadataService` as its domain and `dcat:Catalog` as its range.

Advisement: An implementation of the FDP specifications *MUST* minimally provide the metadata records of the `MetadataService`, and the metadata records of the other types of resources *MUST* be grouped in at least one `Catalog`.

## Navigation information

Since the FDP supports the provisioning of metadata about different types of digital objects and the relations among these metadata records can be customized, each FDP installation may have a different structure.
For instance, the FDP reference implementation is pre-loaded with the structure of metadata about `FAIR Data Point` → `Catalog` → `Dataset` → `Distribution`.
Another FDP could have a different metadata structure, e.g., `FAIR Data Point` → `Catalog` → `Semantic Artefact`.
With this flexibility, a client application would not know how to navigate the FDP metadata content unless it follows all URIs in the metadata, which may be extensive.
Therefore, the FDP *MUST* describe its own navigation structure.
This navigation information *MUST* be provided by using the Linked Data Platform (LDP) containment predicates `ldp:contains` or `ldp:hasMemberRelation`.
This information *MUST* be present in every metadata record that leads to other metadata records.

The following RDF turtle code shows an example of a MetadataService metadata record with navigation information.
<pre class=include-code>
path: src/metadata/example-metadataservice.ttl
highlight: turtle
</pre>

In the metadata record, the FDP (`f:app`) has the relation `fdp-o:metadataCatalog` with its catalogs.
This is the parent-child relation that should be followed by a client that wants to navigate the FDP metadata structure.
To explicitly inform the navigation structure, we have the code segment at the bottom of this example metadata record informing that we have a container, identified as `https://purl.org/fairdatapoint/app/catalog/`, which is the container for the `https://purl.org/fairdatapoint/app` (the object of the `ldp:membershipResource`) and it relates to its contained members using the relation `fdp-o:metadataCatalog`.

## Metadata schemas

The FAIR Data Point supports user defined metadata schemas.
This follows the acknowledgment that every application scenario may require different sets of properties to properly describe a given digital object.
Moreover, the metadata records may have some relevant relationships that connect one to other.
For instance, it seems straightforward to argue that a FAIR Data Point, as a metadata service, may have a number of catalogs that are used to organise the metadata records of other types of digital object, for instance, datasets.

Therefore, to improve interoperability and provide a minimal level of predictability and organisation of different FDPs, the metadata structure of the FDP starts with the metadata of itself (as a metadata service), followed by the catalogs that it contains, and each catalog contains the metadata of given types of digital objects.

Below we present the metadata schemas of the two types of digital object that are mandatory for each FDP: the `FAIR Data Point` and the `Catalog`.

NOTE: In the FDP Ontology the `FAIR Data Point` is defined as a subclass of `MetadataService`, which is a sub-class of `dcat:DataService`.

### FAIR Data Point metadata

<pre class=include>
path: src/metadata/tables/table-fdp-metadata.html
</pre>

The navigation information for the FAIR Data Point metadata record is defined below:

<pre class=include>
path: src/metadata/tables/table-navigation-information.html
</pre>

Below we have the FAIR Data Point metadata schema defined in `SHACL`.

<pre class=include-code>
path: src/metadata/shacl-fdp.ttl
highlight: turtle
</pre>

### Catalog metadata

<pre class=include>
path: src/metadata/tables/table-catalog-metadata.html
</pre>

Below we have a catalog metadata schema defined in `SHACL`.

<pre class=include-code>
path: src/metadata/shacl-catalog.ttl
highlight: turtle
</pre>

Since only the `MetadataService` and `Catalog` metadata are mandatory in an FDP, from the catalog on, the metadata structure of the FDP will vary from deployment to deployment.
However, as the FDP is most commonly used to provide metadata of datasets, the FDP reference implementation follows the DCAT model and bundles two more metadata schemas, namely, the `Dataset` and `Distribution` metadata schemas.
If the administrator of the FDP wishes, he/she can just remove these two schemas and define custom schemas, as long as they are subclasses of the DCAT Resource class.

If other types of digital objects beside `dcat:Dataset` are used in the FAIR Data Point, the catalog metadata should contain the navigation information from the catalog to the digital object metadata, similar to that defined for the FAIR Data Point and catalog in [[#fair-data-point-metadata]].
