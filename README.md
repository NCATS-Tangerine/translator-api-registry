[![Build Status](https://travis-ci.org/NCATS-Tangerine/translator-api-registry.svg?branch=master)](https://travis-ci.org/NCATS-Tangerine/translator-api-registry)

# translator-api-registry
This repo hosts the API metadata for the Translator project

## How to add your API

1. First, each API should create a separate folder to host its metadata. The folder "_example_api" provides basic template for adding API metadata, so you can start with copying "_example_api" folder and renaming it to your API name.
2. Second, fill in the metadata about your API according to the instruction. Also please refer to the existing examples like "[mygene.info](mygene.info)" and "[myvariant.info](myvariant.info)" APIs.
3. Add an entry to [API_LIST.yml](API_LIST.yml) file following the existing example. This is the master list of the APIs available in this repo. Our SmartAPI application will import all the API metadata based on this file.

If you have the permission, commit your changes to this repo. Otherwise, feel free to submit a pull-request. Please check the "build status" badge above, and make sure it's green after your changes. We run some basic tests in this "[tests.py](tests.py)" for each commit.

## API_LIST.yml file
This is a YAML file at the root of this repo to keep track of all APIs available in this repo. Our SmartAPI application will import all the API metadata based on this file and render an API registry web frontend.

For each API, you just need to add a text block like this:

    - metadata: mygene.info/openapi_minimum.yml
      translator:
          - returnjson: true
            notes: ""

* ***metadata*** field

  The value of this field should be either the URL or the relative path pointing to the API metadata. The API metadata should follow [OpenAPI specifications](https://www.openapis.org/), in either JSON or YAML format. Specifically, we support OpenAPI v3 specification documented [here](https://github.com/OAI/OpenAPI-Specification/blob/OpenAPI.next/versions/3.0.0.md), plus the SmartAPI extensions documented [here](https://github.com/WebsmartAPI/OpenAPI-Specification/blob/OpenAPI.next/versions/3.0.md).

* ***translator*** field

  This serves as the placeholder for any translator project specific API properties, e.g. adding some API-specific notes.

  * How to propose a new translator.* field?

    As we expand our list of APIs, we will need to expand our metadata fields as we needed. To do so, you can:
      * discuss it with us at our slack channel (#arch-working-group)
      * open an issue in this repo
      * submit a pull-request for your modified [API_LIST.yml](API_LIST.yml) file

## How to pick URIs for annotating input parameters or the response data object?
Typically for a JSON-based REST API, we use URIs to annotate both the acceptable parameter value types and the fields from the response data object, both in  [OpenAPI](https://www.openapis.org/) metdata files and JSON-LD context files. You can find some examples for "[mygene.info](mygene.info)" and "[myvariant.info](myvariant.info)" APIs.

To help you decide which URIs to use, we maintain a "[ID_MAPPING.csv](ID_MAPPING.csv)" file to keep records of all URIs we will use. Feel free to add URIs for additional field types. Please make sure not to break the csv format, as that will break github's nice csv rendering and search features.

In general, we like to use the URIs from these repositories (also in that priority order)：
  1. Identifiers.org
  2. purl.uniprot.org (?)
  3. [please add]
