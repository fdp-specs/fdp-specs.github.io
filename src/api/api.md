# API
The API of the FDP follows the REST HATEOAS (Hypermedia as the Engine of Application State) guidelines by providing information so that the client is able to discover the available actions and access the resources it needs.
Therefore, the client application is able to navigate through the API and its content from the information available from the content returned in each API call.
This navigation information is provided through the Linked Data Platform (LDP) section as described in [[#navigation-information]].

Since the FDP allows client applications to dynamically discover how to navigate its content, the clients only need to have the URL of the root of the FDP API, and that URL *MUST* provide the metadata of the FDP itself, i.e., the `MetadataService` metadata.
