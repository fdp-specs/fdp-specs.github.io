# Capabilities {#capabilities}

*This section is non-normative, except for [[#capability-dependencies]].*

The behaviour of a FAIR Data Point is organised in **capabilities**.
A capability is a coherent set of behaviours that an FDP offers to third-party applications.
By providing a capability, an FDP enables a class of interactions: for instance, by providing the Read capability an FDP enables client applications to retrieve its metadata records in the way specified in this document.
Each capability is specified in its own section of this document, and each has a corresponding conformance class, defined in [[#conformance]].

This specification defines four capabilities:

: Read ([[#read]])
:: The FDP serves its metadata records in a common representation format, with content negotiation, and each record refers to the schema it conforms to.
    By providing this capability an FDP enables client applications to retrieve and interpret individual metadata records.

: Navigate ([[#navigate]])
:: The FDP describes the structure of its metadata content using the Linked Data Platform containment model, so that a client can discover all metadata records starting from the root of the FDP.
    By providing this capability an FDP enables client applications, such as harvesters and search engines, to traverse and index its whole metadata content without prior knowledge of its structure.

: Write ([[#write]])
:: The FDP accepts the creation, modification and deletion of metadata records and metadata schemas through its API.
    By providing this capability an FDP enables authorised client applications to publish and maintain metadata.

: Bundle ([[#bundle]])
:: The FDP exchanges bundles of metadata records in a single interaction, both for retrieval and for submission.
    By providing this capability an FDP enables bulk harvesting, bulk publication and the migration of metadata content between FDPs.

## Dependencies between capabilities {#capability-dependencies}

Capabilities build on each other.
An FDP that provides a capability *MUST* also provide the capabilities it depends on, as listed in the following table and depicted in Figure 3.1.

<table class="def">
    <caption>Capability dependencies</caption>
    <thead>
        <tr><th>Capability</th><th>Depends on</th><th>Conformance class</th></tr>
    </thead>
    <tbody>
        <tr><td>Read</td><td>—</td><td rowspan="2">FDP Core</td></tr>
        <tr><td>Navigate</td><td>Read</td></tr>
        <tr><td>Write</td><td>Read</td><td>FDP Write</td></tr>
        <tr><td>Bundle retrieval</td><td>Read, Navigate</td><td>FDP Bundle Retrieval</td></tr>
        <tr><td>Bundle submission</td><td>Write</td><td>FDP Bundle Submission</td></tr>
    </tbody>
</table>

<figure>
<svg xmlns="http://www.w3.org/2000/svg" width="520" height="300" viewBox="0 0 520 300" role="img" aria-label="Dependency diagram of the FDP capabilities">
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#444"/>
    </marker>
  </defs>
  <rect x="20" y="20" width="480" height="150" rx="8" fill="none" stroke="#888" stroke-dasharray="6 4"/>
  <text x="32" y="40" font-size="12" fill="#666" font-family="sans-serif">FDP Core</text>
  <rect x="60" y="55" width="160" height="44" rx="6" fill="#e8f0fe" stroke="#345"/>
  <text x="140" y="83" text-anchor="middle" font-size="15" font-family="sans-serif">Read</text>
  <rect x="60" y="115" width="160" height="44" rx="6" fill="#e8f0fe" stroke="#345"/>
  <text x="140" y="143" text-anchor="middle" font-size="15" font-family="sans-serif">Navigate</text>
  <rect x="300" y="115" width="160" height="44" rx="6" fill="#fff4e0" stroke="#753"/>
  <text x="380" y="143" text-anchor="middle" font-size="15" font-family="sans-serif">Write</text>
  <rect x="60" y="220" width="160" height="44" rx="6" fill="#eaf6ea" stroke="#375"/>
  <text x="140" y="248" text-anchor="middle" font-size="15" font-family="sans-serif">Bundle retrieval</text>
  <rect x="300" y="220" width="160" height="44" rx="6" fill="#eaf6ea" stroke="#375"/>
  <text x="380" y="248" text-anchor="middle" font-size="15" font-family="sans-serif">Bundle submission</text>
  <line x1="140" y1="115" x2="140" y2="99" stroke="#444" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="300" y1="137" x2="222" y2="86" stroke="#444" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="140" y1="220" x2="140" y2="161" stroke="#444" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="380" y1="220" x2="380" y2="161" stroke="#444" stroke-width="1.5" marker-end="url(#arrow)"/>
  <text x="270" y="290" text-anchor="middle" font-size="12" fill="#666" font-family="sans-serif">an arrow from A to B reads "A depends on B"</text>
</svg>
<figcaption class="no-marker">**Figure 3.1** Dependencies between the FDP capabilities</figcaption>
</figure>

Issue: **DP-1 — Bundle as one or two conformance classes.**
Bundle retrieval only depends on the Core capabilities, whereas bundle submission depends on Write.
Should Bundle be a single conformance class, requiring an FDP to provide both retrieval and submission, or two classes, so that a harvest-oriented FDP can claim bundle retrieval without implementing Write?
Options: (a) one class, FDP Bundle; (b) two classes, FDP Bundle Retrieval and FDP Bundle Submission.
Proposed default: (b), as reflected in this draft.

## Relation to the conformance classes {#capabilities-and-conformance}

An application is a FAIR Data Point if it conforms to the **FDP Core** conformance class, i.e., if it provides the Read and Navigate capabilities.
Read alone is deliberately not sufficient: serving individual records with content negotiation is what any linked data publisher does, while the navigation information is what makes the whole metadata content of an FDP discoverable in a predictable way.
An FDP may additionally claim conformance to any of the other conformance classes for which it satisfies the requirements.
The conformance classes and their criteria are defined in [[#conformance]].

## Implementations {#implementations}

This specification describes the expected behaviour of a FAIR Data Point and is independent of any particular implementation.
The <a href="https://github.com/FAIRDataTeam/FAIRDataPoint">FDP Reference Implementation (FDP-RI)</a> is one particular implementation of this specification, developed and maintained by the FAIR Data Team.
Documentation about the FDP-RI, including its internal architecture and deployment instructions, is available at the <a href="https://fairdatapoint.readthedocs.io/">FDP-RI documentation</a>.
