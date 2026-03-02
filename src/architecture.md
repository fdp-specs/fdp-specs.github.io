# Architecture

From the usage scenarios, we have identified a need for a metadata provisioning infrastructure that we call FAIR Data Point (FDP).
The FDP has the following goals:

- Allow owners/creators/publishers to expose the metadata of their digital objects in a way that follows the FAIR Data Principles.
- Allow consumers/users to discover information about digital objects they are interested in.
- Provide meaningful information about digital objects for both humans and software agents.

Based on these goals, Figure 3.1 depicts the general architecture of an FDP.
In this architecture, the FDP exposes its functionality to the users through an application programming interface (API).
In our reference implementation, besides the FDP itself we developed an FDP web client, which connects to the FDP API and allows human users to interact with the application through a web-based interface.

<figure>
    <img alt="High-level architecture of the FAIR Data Point" src="/images/FDParchitecture.png">
    <figcaption class="no-marker">**Figure 3.1** High-level architecture of the FAIR Data Point.</figcaption>
</figure>

Figure 3.1 also depicts the FDP's internal components, namely the Metadata Provider, Access Control, Metadata Schemas and the RDF Metadata Store.

- **Metadata Provider** - responsible for the provisioning of the metadata content available in the FDP;
- **Access Control** - reponsible for controlling the access to the metadata content. 
    In general, metadata can be openly accessible for reading, but it is expected that only a select number of people have access to add, delete or edit the metadata content.
    Moreover, in some situations, metadata or part of the metadata may also have access restrictions for reading.
    The Access Control component makes sure that these restrictions are enforced;
- **RDF Metadata Source** - The FDP *MUST* present its metadata content as `RDF`, and, more specifically, in at least `turtle` and `JSON-LD` syntaxes.
    Therefore, these metadata can be stored in an RDF Metadata Source.
    The FDP reference implementation supports native in-memory or on-disk storage, as well as the connection with existing triple stores such as GraphDB, Allegro Graph, Blazegraph, etc.
    If one is extending an existing application based on this FDP specification, the RDF metadata can be provided using different implementation strategies.
    For instance, metadata stored in other representation formats can be dynamically converted to RDF through a conversion component that serves as the RDF Metadata Source.
- **Metadata Schemas** - the FDP exposes metadata about different types of digital objects, e.g., repositories, content catalogs, and datasets, among others.
    These metadata should comply with schemas defined by their related communities.
    In the FDP, the metadata schemas *MUST* be represented in `SHACL`.
    The FDP reference implementation is shipped with four basic metadata schemas:
    for the FDP itself as a metadata service, for catalogs, for datasets, and for datasets' distributions.
    These schemas allow the FDP to check and validate metadata content that is added.
    Addition of metadata schemas for other types of digital objects and extensions of the base schemas are also supported by the FDP reference implementation.
