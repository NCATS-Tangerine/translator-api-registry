## Metadata for a Translator Knowledge Source Catalog

### I Overview

This document outlines proposed extensions to the json format used in the[ APIList.yaml](https://github.com/NCATS-Tangerine/translator-api-registry/blob/master/API_LIST.yml) file, to capture additional descriptive metadata about Translator APIs  and their underlying data sources. Requirements for these extensions are driven by the need for a human-friendly Translator Catalog of APIs and sources, to support various users and use cases:

1. Enable **leadership** (team leaders, NCATS) to follow at a high level the evolution of data available in the Translator over time, and identify strengths and gaps in coverage.

2. Allow** domain experts** to know what types of data are available for defining CQs (and in particular to promote use of more diverse data types and sources across teams).

3. Help** notebook developers** to know where/how to find data to implement CQ notebooks, and extend them into new areas.

4. Help** external users/stakeholders** to understand scope of data/knowledge cataloged in the Translator system.

5. Inform the work of **smartAPI developers** who are wrapping and more formally defining API metadata

 

API metadata for the Translator Catalog will be collected from API developers in yaml format using the existing[ APIList.yaml](https://github.com/NCATS-Tangerine/translator-api-registry/blob/master/API_LIST.yml) file in the translator-api-registry repo.  Initially we will target high-level metadata **about each API** in the Translator system. It should pose a minimal barrier for API developers/stewards to enter metadata (i.e. require 15 minutes or less) - so we can deliver a catalog quickly.  This metadata will complement the more granular metadata captured in the smartAPI yaml config files for each API (e.g.  for the [mygene.info API](https://github.com/NCATS-Tangerine/translator-api-registry/blob/master/mygene.info/openapi_full.yml)).   Subsequent extensions to these fields may be implemented at a later date to enable description of ** each primary source** that aggregating APIs serve data from (e.g. Monarch-Biolink, Wikidata, Biothings, NSIDES).  Once populated, these yaml files will be used by scripts to automatically generate more human-friendly Translator Catalog view of this metadata (e.g. a spreadsheet view, as mocked up [here](https://docs.google.com/spreadsheets/d/160Vzcgk5eGjtqbrKZzCyyJuPRKQV_zpk4BpZRMC70PA/edit#gid=0)). 