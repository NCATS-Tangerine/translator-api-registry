TYPE_ID_MAPPING = {
    "ChemicalSubstance": "CHEBI",
    "Cell": "CL",
    "BiologicalProcess": "GO",
    "CellularComponent": "GO",
    "MolecularActivity": "GO",
    "PhenotypicFeature": "HP",
    "Disease": "MONDO",
    "Gene": "NBIGene",
    "Protein": "PR",
    "SequenceFeature": "SO",
    "AnatomicalEntity": "UBERON",
    "OrganismTaxon": "NCBITaxon"
}


def generate_individual_x_bte_operation(input_type, output_type):
    return {
        input_type + '-' + output_type: [
            {
                "inputs": [
                    {
                        "id": TYPE_ID_MAPPING[input_type],
                        "semantic": input_type
                    }
                ],
                "outputs": [
                    {
                        "id": TYPE_ID_MAPPING[output_type],
                        "semantic": output_type
                    }
                ],
                "parameters": {
                    "q": "subject." + TYPE_ID_MAPPING[input_type] + ':"{inputs[0]}"',
                    "fields": "object,association",
                    "size": 1000
                },
                "predicate": "related_to",
                "response_mapping": {
                    "$ref": '#/components/x-bte-response-mapping/' + output_type
                },
                "source": "Text Mining KP",
                "supportBatch": False
            }
        ]
    }


def generate_x_bte_operations():
    res = {}
    for k in TYPE_ID_MAPPING.keys():
        for v in TYPE_ID_MAPPING.keys():
            res.update(generate_individual_x_bte_operation(k, v))
    return res


def generate_x_bte_operations_refs():
    res = []
    for k in TYPE_ID_MAPPING.keys():
        for v in TYPE_ID_MAPPING.keys():
            res.append({
                "$ref": "#/components/x-bte-kgs-operations/" + k + '-' + v
            })
    return {
        "x-bte-kgs-operations:": res
    }


def generate_individual_x_bte_response_mapping(output_type):
    return {
        output_type: {
            "ngd": "hits.association.ngd",
            TYPE_ID_MAPPING[output_type]: "hits.object." +
            TYPE_ID_MAPPING[output_type]
        }
    }


def generate_x_bte_response_mappings():
    res = {}
    for k in TYPE_ID_MAPPING.keys():
        res.update(generate_individual_x_bte_response_mapping(k))
    return res


def to_yaml(json_doc, output_file):
    import yaml
    with open(output_file, 'w') as file:
        documents = yaml.dump(json_doc, file)
