# translator-api-registry
This repo hosts the API metadata for the Translator project

## How to add your API

1. First, each API should create a separate folder to host its metadata. The folder "_example_api" provides basic template for adding API metadata, so you can start with copying "_example_api" folder and renaming it to your API name.
2. Second, fill in the information about your API according to the instruction. Also please refer to the existing examples like "[mygene.info](mygene.info)" and "[myvariant.info](myvariant.info)" APIs. 

## metadata.yaml file
This is a required metadata file in YAML format, referring to "[_example_api/metadata.yaml](_example_api/metadata.yaml)" for more details. At minimal, you should provide two fields:
  * *api* : for the name of your API
  * *openapi*: the API metadata following [OpenAPI specifications](https://www.openapis.org/), in either JSON or YAML format.

If you provide a path to your *openapi* metadata, you typically put the actual metadata file under the same api folder. If you provide a web URL, you don't have to put a copy of your metadata here.

## How to propose a new field for metadata.yaml file?
As we expand our list of APIs, we will need to expand our metadata fields as we needed. To do so, you can:
* discuss it with us at our slack channel (#arch-working-group)
* open an issue in this repo
* submit a pull-request for your modified "[_example_api/metadata.yaml](_example_api/metadata.yaml)" file
 
## How to pick URIs for annotating response data object?
Typically for a JSON-based REST API, we use URIs to annotate the fields from the response data object, both in "metadata.yaml" file and JSON-LD context files. You can find some examples for "[mygene.info](mygene.info)" and "[myvariant.info](myvariant.info)" APIs.

To help you decide which URIs to use, we maintain a "[ID_MAPPING.csv](ID_MAPPING.csv)" file to keep records of all URIs we will use. Feel free to add URIs for additional field types. Please make sure not to break the csv format, as that will break github's nice csv rendering and search features.

In general, we like to use the URIs from these repositories (also in that priority order)：
  1. Identifiers.org
  2. purl.uniprot.org (?)
  3. [please add]

