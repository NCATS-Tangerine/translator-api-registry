## Translator API Catalog

As the Translator incorporrates more knowledge sources, there is a need for a human-friendly catalog of APIs in the system to support various users and use cases:

1. Enable **leadership** (team leaders, NCATS) to follow at a high level the evolution of data available in the Translator over time, and identify strengths and gaps in coverage.
2. Allow **domain experts** to know what types of data are available for defining CQs (and in particular to promote use of more diverse data types and sources across teams).
3. Help **notebook developers** to know where/how to find data to implement CQ notebooks, and extend them into new areas.
4. Help **external users/stakeholders** to understand scope of data/knowledge cataloged in the Translator system.
5. Inform the work of **smartAPI developers** who are wrapping and more formally defining API metadata

At present, the [APIList.yaml](https://github.com/NCATS-Tangerine/translator-api-registry/blob/master/API_LIST.yml) file in the translator-api-registry repo is set up to collect structured, Translator-specific metadata about each registered API. We will make extensions to this yaml format by creating additional fields and value sets in support of the use cases above.

API metadata for the Translator Catalog will be contributed by API developers using this yaml-based format, and live in the [APIList.yaml](https://github.com/NCATS-Tangerine/translator-api-registry/blob/master/API_LIST.yml) file.  Once populated, these API metadata yaml files will be consumed by scripts to automatically generate more human-friendly Translator Catalog view of this metadata (e.g. a spreadsheet view, as mocked up [here](https://docs.google.com/spreadsheets/d/160Vzcgk5eGjtqbrKZzCyyJuPRKQV_zpk4BpZRMC70PA/edit#gid=0)). 

Initially we will target high-level metadata **about each API** in the Translator system. It should pose a minimal barrier for API developers/stewards to enter metadata (i.e. require 15 minutes or less) - so we can deliver a catalog quickly.  This metadata will complement the more granular metadata captured in the smartAPI yaml config files for each API (e.g. for the [mygene.info API](https://github.com/NCATS-Tangerine/translator-api-registry/blob/master/mygene.info/openapi_full.yml)). Subsequent extensions to the metadata extension fields may be implemented at a later date to enable description of **each primary source** that aggregating APIs serve data from (e.g. Monarch-Biolink, Wikidata, Biothings, NSIDES). 

### INSTRUCTIONS FOR CREATING AN API METADATA RECORD CAN BE FOUND IN ISSUE [#8](https://github.com/NCATS-Tangerine/translator-api-registry/issues/8).
