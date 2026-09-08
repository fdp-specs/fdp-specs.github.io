# Write capability # {#write}
The requirements in this section belong to the **Write** capability and form the FDP Write conformance class.
The Write capability depends on the Read capability ([[#read]]).
By providing this capability, an FDP enables authorised client applications to publish and maintain metadata records and metadata schemas through the FDP API.

Advisement: This section is a first draft.
Its requirements are proposed for discussion and will be refined before this version of the specification is finalised.

## Overview ## {#write-overview}
*This section is non-normative.*

The write operations of an FDP follow the Linked Data Platform (LDP) [[!LDP]]: the containers that an FDP exposes as navigation information ([[#navigation-information]]) are LDP Direct Containers, and metadata records are created by posting them to a container, replaced with `PUT`, modified with `PATCH` and removed with `DELETE`.
This makes an FDP a specialised LDP server, and aligns the FDP with the Solid Protocol [[SOLID-PROTOCOL]], which builds on the same operations, and with the ongoing W3C Linked Web Storage work that succeeds it.

## Creating metadata records ## {#write-create}
A client creates a metadata record by sending an HTTP `POST` request to a container whose `ldp:hasMemberRelation` is the relation that will connect the new record to the container's membership resource.
The request body *MUST* be an RDF document in Turtle or JSON-LD describing the new entity, with a null relative IRI as the subject to be assigned by the FDP.

On a successful creation, the FDP *MUST*:

- assign an IRI to the new metadata record and return it in the `Location` header of a `201 Created` response;
- add the new IRI as an `ldp:contains` value of the container and add the membership triple connecting the membership resource to the new record through the member relation;
- create the FDP Metadata Record ([[#metadata-record]]) of the new record, setting `dcterms:issued` and `dcterms:modified` to the time of creation.

Before accepting the record, the FDP *MUST* validate it as specified in [[#write-validation]].
The FDP *MAY* honour a `Slug` header as a hint for the assigned IRI.

## Replacing and modifying metadata records ## {#write-update}
A client replaces a metadata record by sending an HTTP `PUT` request to its IRI, with the complete new record as the body.
A client modifies a metadata record by sending an HTTP `PATCH` request to its IRI.
In both cases the FDP *MUST* validate the resulting record as specified in [[#write-validation]] before applying the change, and *MUST* update `dcterms:modified` in the FDP Metadata Record.
Properties maintained by the FDP, such as the navigation information and the link to the FDP Metadata Record, *MUST NOT* be modifiable by the client.

The FDP *SHOULD* support the `If-Match` request header on `PUT` and `PATCH`, so that a client can avoid overwriting changes made by another client, and *MUST* then answer `412 Precondition Failed` when the condition is not met.

Issue: **DP-11 — PATCH format.**
LDP leaves the `PATCH` document format to the server.
Options: (a) a subset of SPARQL 1.1 Update [[SPARQL11-UPDATE]] restricted to `INSERT DATA` and `DELETE DATA`, plus `DELETE/INSERT ... WHERE` on the record's own triples; (b) N3 Patch, as mandated by the Solid Protocol; (c) LD Patch [[LD-PATCH]]; (d) no `PATCH` support, only `PUT`.
Proposed default: (a), because of its broad tooling support; the FDP would advertise the supported format in the `Accept-Patch` header.

## Deleting metadata records ## {#write-delete}
A client deletes a metadata record by sending an HTTP `DELETE` request to its IRI.
On a successful deletion, the FDP *MUST* remove the record, its navigation information and its FDP Metadata Record, remove the `ldp:contains` and membership triples that referred to it from its parent container and membership resource, and answer subsequent `GET` requests for the record as specified in [[#read-errors]].

Issue: **DP-12 — Deleting records that have members.**
Options: (a) the FDP MUST reject, with `409 Conflict`, the deletion of a record whose containers still list members; (b) the FDP MUST delete the members recursively; (c) the behaviour is chosen by the implementation and advertised.
Proposed default: (a), as it prevents accidental loss of large sub-trees.

## Managing metadata schemas ## {#write-schemas}
A profile ([[#metadata-records]]) hosted by the FDP is a resource that is created, replaced and deleted with the same operations as metadata records, with a SHACL shapes graph as the request body.
The FDP *MUST* validate that a submitted schema is a syntactically valid SHACL shapes graph that declares its target class, and *MUST* reject the deletion of a profile that is still referenced by metadata records it serves, with `409 Conflict`.

Issue: **DP-13 — Exposure of the profiles of an FDP.**
For clients to discover which profiles an FDP hosts and to create new ones, the profiles have to be reachable from the FDP metadata record.
Options: (a) the FDP metadata record provides a container of its profiles as navigation information, with a dedicated member relation to be added to the FDP ontology; (b) profiles are discovered only through the `dcterms:conformsTo` values of the records; (c) profiles are listed through the `dcat:endpointDescription` of the FDP.
Proposed default: (a).

## Validation ## {#write-validation}
Before accepting a created, replaced or modified metadata record, the FDP *MUST* validate the resulting record against the metadata schema identified by the record's profile, and *MUST* verify that the profile's target class is the class of the record.
When validation fails, the FDP *MUST* reject the request with status code `422 Unprocessable Content` [[RFC9110]] and *MUST* include in the response body the SHACL validation report [[!SHACL]] (`sh:ValidationReport`), serialised in one of the syntaxes of [[#read-records]].

Issue: **DP-17 — Profiles that a written record may reference.**
Validation requires the schema identified by the record's profile; a profile may be hosted by the FDP or elsewhere ([[#read-schemas]]), and dereferencing an arbitrary remote profile during a write operation is a performance and security risk ([[#security-privacy]]).
Options: (a) a written record may only reference profiles hosted by the FDP itself; (b) it may reference any dereferenceable profile, and the FDP MUST cache the schemas it validates against; (c) it may reference profiles on an allow-list configured by the FDP, hosted or remote.
Proposed default: (c), with (a) as the minimal configuration.

## Authentication and authorization ## {#write-auth}
The FDP *MUST* require authentication for every write operation and *MUST* enforce an authorization policy determining which authenticated agents may perform which operations on which records and schemas.
A write request without valid credentials *MUST* be answered with `401 Unauthorized`; a request by an authenticated agent that is not authorised for the operation *MUST* be answered with `403 Forbidden`.

Issue: **DP-5 — Authentication and authorization mechanism.**
Options: (a) require that a mechanism exists, without mandating one, as written above; (b) mandate a specific mechanism, e.g. OpenID Connect for authentication, possibly Solid-OIDC, and an access control vocabulary such as WAC or ACP for authorization, following the Solid Protocol; (c) recommend a mechanism while allowing others.
Proposed default: (a) for this version, with a recommendation to align with the Solid Protocol and the Linked Web Storage work as they stabilise.
