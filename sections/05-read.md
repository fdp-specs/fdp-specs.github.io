# Read capability # {#read}
The requirements in this section belong to the **Read** capability and are part of the FDP Core conformance class.
By providing this capability, an FDP enables client applications to retrieve and interpret its metadata records, metadata schemas and FDP Metadata Records.

## Overview ## {#read-overview}
*This section is non-normative.*

The API of the FDP follows the REST HATEOAS (Hypermedia as the Engine of Application State) guidelines by providing information so that the client is able to discover the available actions and access the resources it needs.
The client application is therefore able to navigate through the API and its content from the information available in the content returned in each API call.
A client only needs the URL of the root of the FDP API: that URL provides the metadata of the FDP itself, and, when the FDP provides the Navigate capability ([[#navigate]]), the navigation information contained in each record leads the client to all other records.

## Root URL ## {#read-root}
The root URL of the FDP API *MUST* return the metadata record of the FDP itself, i.e., a record of an instance of `fdp-o:FAIRDataPoint` conforming to [[#fair-data-point-metadata]].
The IRI of the FDP as a described entity *SHOULD* be the root URL of its API, and the value of `dcat:endpointURL` in the FDP metadata record *MUST* be the root URL.

## Retrieving metadata records ## {#read-records}
Every metadata record *MUST* be retrievable by an HTTP GET request on the IRI of the described entity.

The FDP *MUST* support at least the RDF 1.1 Turtle [[!TURTLE]] and JSON-LD [[!JSON-LD11]] syntaxes for every metadata record, selected through HTTP content negotiation on the `Accept` header.
When the request carries no `Accept` header, or an `Accept` header that does not express a preference among supported formats, the FDP *MUST* return RDF Turtle.
The FDP *MAY* support other syntaxes, such as RDF/XML, N-Triples or HTML for human consumption.
When none of the requested media types is supported, the FDP *MUST* respond with status code `406 Not Acceptable`.

The representation of a metadata record *MUST* contain all the triples of the record, i.e., all triples whose subject is the IRI of the described entity, together with the description of any blank node reachable from it.
When the FDP provides the Navigate capability, the representation *MUST* also contain the navigation information of the record, as specified in [[#navigation-information]].

The response *SHOULD* carry an HTTP `Link` header with relation type `profile` [[RFC6906]] whose target is the profile IRI of the record, i.e., the value of its `dcterms:conformsTo` property.
The response *SHOULD* carry an HTTP `Link` header with relation type `describedby` whose target is the IRI of the FDP Metadata Record of the record (see DP-2 in [[#metadata-record]]).

The FDP *SHOULD* support conditional requests on metadata records: the response *SHOULD* carry `ETag` and `Last-Modified` headers, the latter derived from the `dcterms:modified` value of the FDP Metadata Record, and the FDP *SHOULD* honour `If-None-Match` and `If-Modified-Since` request headers.

## Retrieving metadata schemas ## {#read-schemas}
Every profile IRI referenced by a metadata record served by the FDP *MUST* be dereferenceable.
An HTTP GET request on a profile IRI *MUST* return the metadata schema as a SHACL shapes graph [[!SHACL]], serialised in RDF Turtle by default, and *SHOULD* also support JSON-LD.
Profiles *MAY* be hosted by the FDP itself or elsewhere, e.g., a shared profile registry; in both cases the requirements of this section apply to what the profile IRI returns.

## Retrieving FDP Metadata Records ## {#read-metadata-records}
The IRI of every FDP Metadata Record ([[#metadata-record]]) *MUST* be dereferenceable, with the same syntax and content negotiation requirements as metadata records ([[#read-records]]), and the FDP *SHOULD* support conditional requests on FDP Metadata Records in the same way.

## Error responses ## {#read-errors}
A request for an IRI that the FDP does not serve *MUST* be answered with status code `404 Not Found`.
A request for a metadata record that has been deleted *SHOULD* be answered with status code `410 Gone`.
Requests for unsupported representations are answered with `406 Not Acceptable`, as specified in [[#read-records]].

Issue: **DP-10 — Format of error responses.**
Options: (a) error responses use the Problem Details format [[RFC9457]] (`application/problem+json`); (b) error responses are RDF documents describing the error, in the same syntaxes as metadata records; (c) the format of error bodies is left unspecified.
Proposed default: (a), as it is widely supported by HTTP tooling and independent of the RDF syntax negotiated for the records.
