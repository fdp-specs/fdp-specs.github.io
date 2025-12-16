# Overall Description

The basis for any infrastructure is its suitability to the issues it should address. Therefore, the first step is to identify these issues. One common approach for this identification is to investigate current practices that could benefit from a supporting infrastructure. Once we analyse these practices, we can elicit the requirements for the infrastructure. In this document we list a number of data usage scenarios that represent regular practices in data-intensive domains. These usage scenarios have been gathered through interactions with a variety of representative stakeholders in different domains. These stakeholders represent data producers, data consumers and providers of both infrastructure and services for supporting data activities.

## Usage Scenarios

From the different semantic interoperability projects we have been and are involved in, the following usage scenarios have been identified. These usage scenarios do not represent one particular situation in a real project but depict data interoperability-related situations that we experienced in a number of different projects. From these scenarios we derived a set of requirements for metadata storage and accessibility infrastructure and they also guided the design and development of the solution.

### Data discovery

A researcher needs to find datasets containing data about a given subject, e.g., proteins that are activated in specific tissues, polution level in a given region, or infrared observation of a particular galaxy; integrate the discovered data with other pre-selected datasets and analyse them. In another situation, the researcher needs to know which biobanks carry a given type of biosample (e.g., blood samples) from patients possessing a specific disease (e.g., Alzheimer's disease) taken from a patient registry whose onset age was lower than 45 years old. These data users need to use a straightforward search application that allows them to find the required information. However, the search application first needs to have indexed information about existing datasets wherever their location.

### Data access

Once a data user/consumer finds the desired datasets, including the information about their licenses and access protocols, the user wants to access the data, retrieving it, or sending an algorithm to analyse the data. In many situations the data user will integrate many different datasets. To carry out these integrations, the user needs to know in which formats the data can be accessed, and which access methods are available. This information comes in the form of metadata. In order to facilitate the usage of metadata, the method with which the metadata will be accessed should be common in all different metadata sources and a common representation technology should be used for the metadata.

### (Meta)Data publication

An organization is running a project in which data is being created. The data will be analyzed during the project but may also be useful for other users. The group would therefore like to publish the data in a way that allows potential users to retrieve information about the datasets (metadata), allows data search engines to index the metadata, and allows users to acces the data. Some of the produced datasets have an open license but others have more restrictive licenses. All these metadata should be available so that potential data users would have enough information to assess whether the data described in the metadata fits their needs.

### Publishing other types of content

An organization is running a project in which different types of deliverables will be created. One group is developing a piece of software, another group is working on a controlled vocabulary, while a third group will generate a number of reference documents. The organization would like to publish information about these materials so others could discover and reuse them.
