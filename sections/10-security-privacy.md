# Security and privacy considerations {#security-privacy}

*This section is non-normative.*

An FDP publishes metadata, which is intended to be openly discoverable.
Publishers should nevertheless be aware that metadata can reveal sensitive information about the described entities, for instance the existence of a dataset about a small population or the identity of a contact person, and should apply the access rights they express with `dcterms:accessRights` to the metadata records themselves where appropriate.

The Write capability ([[#write]]) exposes the content of an FDP to modification.
Implementations providing it should protect the write operations with the authentication and authorization measures of [[#write-auth]], should validate every submitted record ([[#write-validation]]) and should treat submitted RDF as untrusted input, in particular when it is later rendered for humans or used to construct queries.

Metadata records and schemas refer to external IRIs, e.g., profiles hosted elsewhere.
Implementations that dereference such IRIs, for instance to validate a record against a remote schema, should guard against unavailable, slow or malicious remote resources.
