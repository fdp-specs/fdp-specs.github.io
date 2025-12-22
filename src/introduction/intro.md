# Introduction

FAIR Data Point (FDP) is a metadata service that provides access to metadata following the FAIR principles [[FAIR-principles]].
FDP uses a REST API for creating, storing and serving FAIR metadata.
FDP is software that, from one side, allows digital objects owners/publishers to expose the metadata of their digital objects in a FAIR manner and, from the other side, allows digital objects' consumers to discover information (metadata) about offered digital objects.
Commonly, the FAIR Data Point is used to expose metadata of datasets but metadata of other types of digital objects can also be exposed such as ontologies, repositories, analysis algorithms, websites, etc.

Many different repositories and their digital objects should interoperate in order to allow increasingly complex questions to be answered.
These repositories and their content should be interoperable in order for client applications to autonomously (re)use them.
However, interoperability happens at different levels, including syntactical and semantical interoperabilities.
The FDP aims at addressing these interoperability issues by providing:

- A common interface to access information (metadata) about digital objects;
- A common representation format [[RDF11-PRIMER]] to express the metadata in a machine-actionable manner;
- A common approach to inform to clients how to navigate through the FDP's metadata structure;
- A common representation format [[SHACL]] to represent each metadata record's schema.

The main goal of the FDP is to establish a common method for metadata provisioning and accessing and, as a consequence, provide to client applications a predictable way of accessing and interacting with metadata content.
To fulfill this goal, this document contains a set of specifications to help developers to extend the functionality of their applications so these applications can also behave as a FAIR Data Point.

## Purpose

The purpose of this document is to specify the FAIR Data Point.
This document includes requirements, architecture and design of the FDP as well as the metadata schemas used.
This specification is primarily intended to be a reference for developers willing to add the FDP functionality into their existing applications or develop their own FAIR Data Point implementation.
In order to better understand this specification, knowledge of RDF, LDP, SHACL and REST APIs is required. 
