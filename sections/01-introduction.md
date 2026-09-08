# Introduction {#introduction}

*This section is non-normative.*

The FAIR Data Point (FDP) is a metadata service that provides access to metadata following the FAIR principles [[FAIR-principles]] [[FDP]].
An FDP, on one side, allows the owners and publishers of digital objects to expose the metadata of these objects in a FAIR manner and, on the other side, allows consumers of digital objects to discover information (metadata) about the offered objects.
Commonly, an FDP is used to expose metadata of datasets, but metadata of other types of entities can also be exposed, such as ontologies, repositories, analysis algorithms, websites, and even non-digital entities such as organisations and people.

Many different repositories and their digital objects should interoperate in order to allow increasingly complex questions to be answered.
These repositories and their content should be interoperable in order for client applications to autonomously interact with them and (re)use their content.
However, interoperability happens at different levels, including syntactic and semantic interoperability.
The FDP aims at addressing these interoperability issues by providing:

- A common interface to access information (metadata) about (digital) entities;
- A common representation format [[!RDF11-PRIMER]] to express the metadata in a machine-actionable manner;
- A common approach to inform clients how to navigate through the metadata structure of an FDP;
- A common representation format [[!SHACL]] to represent the schema of each metadata record.

The main goal of the FDP is to establish a common method for metadata provisioning and access and, as a consequence, to provide client applications with a predictable way of accessing and interacting with metadata content.
An FDP has the following goals:

- Allow owners, creators and publishers to expose the metadata of their digital objects in a way that follows the FAIR principles;
- Allow consumers and users to discover information about digital objects they are interested in;
- Provide meaningful information about digital objects for both humans and software agents.

## Purpose and scope {#purpose}

The purpose of this specification is to define the expected behaviour of a FAIR Data Point, i.e., the behaviour an application must exhibit in order to be considered an FDP.
The specification is implementation-agnostic: it is primarily intended as a reference for developers willing to add FDP functionality to their existing applications or to develop their own FAIR Data Point implementation.
It does not prescribe how a particular FDP implementation should be internally designed or engineered.
Documentation about particular implementations, such as the <a href="https://github.com/FAIRDataTeam/FAIRDataPoint">FDP Reference Implementation (FDP-RI)</a>, is provided by the respective implementation projects.

This version of the specification organises the behaviour of an FDP in **capabilities**: Read, Navigate, Write and Bundle (see [[#capabilities]]).
Each capability is a coherent set of behaviours that an FDP offers to third-party applications, and each has a corresponding conformance class (see [[#conformance]]).
An application is a FAIR Data Point if it conforms to the Core conformance class, which comprises the Read and Navigate capabilities.
The remaining capabilities are optional.

In order to better understand this specification, knowledge of RDF, LDP, SHACL and REST APIs is required.

## Open decision points {#decision-points}

This draft deliberately leaves a number of design decisions open for review.
They are marked in the text as numbered **decision points** (DP-*n*) in issue blocks, each stating the question, the options considered and, where there is one, a proposed default.
The normative text surrounding a decision point is written for the proposed default, so that the document remains complete and readable; the issue block describes what would change under the other options.
All decision points are collected in the Issues Index at the end of this document.
Comments are welcome in the <a href="https://github.com/fdp-specs/fdp-specs.github.io/issues">issue tracker</a>.

## Document conventions {#document-conventions}

Conformance requirements are expressed with a combination of descriptive assertions and RFC 2119 terminology.
The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in the normative parts of this document are to be interpreted as described in RFC 2119. [[!RFC2119]]

All of the text of this specification is normative except sections explicitly marked as non-normative, examples, notes and issue blocks.

The SHACL shapes in this document validate the structure of a single metadata record; in SHACL, a property shape without `sh:minCount` allows the property to be absent and one without `sh:maxCount` allows any number of values.
Requirements that span several records, such as the class of the members listed in a container, or that concern HTTP behaviour, are not expressed in the shapes and are tested by inspecting the responses of the FDP.

Each requirement belongs to one capability.
The capability a section belongs to is stated at the start of the section, and the conformance section ([[#conformance]]) lists, per conformance class, the sections whose requirements apply.

The following namespace prefixes are used throughout this document.

<table class="def">
    <caption>Namespace prefixes</caption>
    <thead>
        <tr><th>Prefix</th><th>Namespace IRI</th><th>Vocabulary</th></tr>
    </thead>
    <tbody>
        <tr><td><code>rdf</code></td><td><code>http://www.w3.org/1999/02/22-rdf-syntax-ns#</code></td><td>RDF</td></tr>
        <tr><td><code>rdfs</code></td><td><code>http://www.w3.org/2000/01/rdf-schema#</code></td><td>RDF Schema</td></tr>
        <tr><td><code>xsd</code></td><td><code>http://www.w3.org/2001/XMLSchema#</code></td><td>XML Schema datatypes</td></tr>
        <tr><td><code>dcat</code></td><td><code>http://www.w3.org/ns/dcat#</code></td><td>Data Catalog Vocabulary [[!VOCAB-DCAT-3]]</td></tr>
        <tr><td><code>dcterms</code></td><td><code>http://purl.org/dc/terms/</code></td><td>DCMI Metadata Terms</td></tr>
        <tr><td><code>foaf</code></td><td><code>http://xmlns.com/foaf/0.1/</code></td><td>Friend of a Friend</td></tr>
        <tr><td><code>vcard</code></td><td><code>http://www.w3.org/2006/vcard/ns#</code></td><td>vCard Ontology</td></tr>
        <tr><td><code>ldp</code></td><td><code>http://www.w3.org/ns/ldp#</code></td><td>Linked Data Platform [[!LDP]]</td></tr>
        <tr><td><code>sh</code></td><td><code>http://www.w3.org/ns/shacl#</code></td><td>Shapes Constraint Language [[!SHACL]]</td></tr>
        <tr><td><code>fdp-o</code></td><td><code>https://w3id.org/fdp/fdp-o#</code></td><td>FAIR Data Point Ontology</td></tr>
    </tbody>
</table>
