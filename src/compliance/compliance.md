# FDP Specification Compliance

The aim of this specification is to guide developers in implementing their own FAIR Data Points or in extending existing applications with the FDP behaviours, thus exposing their metadata in a FAIR way.

In order to verify whether and application behaves as a FAIR Data Point according to these specifications, the following characteristics must be present:

- Its root API URL *MUST* provide the `MetadataService` metadata;
- The metadata content *MUST* be presented in, at least, RDF Turtle and JSON-LD syntaxes.
    Other formats such as XML, JSON and other RDF syntaxes are allowed through content negotiation but the default media type for the HTTP(S) request *MUST* be RDF Turtle.
- Each metadata record *SHOULD* have a reference to its own profile which, in its turn, *MUST* point to the metadata schema expressed in [[!SHACL]];
- The metadata schema expressed in [[!SHACL]] *MUST* have as its target class a sub-class of `dcat:Resource`;
- The information about how to navigate the metadata content structure of the FDP *MUST* be provided in each metadata record using the Linked Data Platform (LDP) containment structure (`ldp:hasMemberRelation`) - see [[#navigation-information]].
