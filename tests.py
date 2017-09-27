import unittest
import os.path
import json
import pprint

import requests
import yaml


def get_api_metadata_by_url(url, as_string=False):
    try:
        res = requests.get(url)
    except requests.exceptions.Timeout:
        return {"success": False, "error": "URL request is timeout."}
    except requests.exceptions.ConnectionError:
        return {"success": False, "error": "URL request had a connection error."}
    if res.status_code != 200:
        return {"success": False, "error": "URL request returned {}.".format(res.status_code)}
    else:
        if as_string:
            return res.text
        else:
            try:
                metadata = res.json()
            # except json.JSONDecodeError:   # for py>=3.5
            except ValueError:               # for py<3.5
                try:
                    metadata = yaml.load(res.text)
                except (yaml.scanner.ScannerError,
                        yaml.parser.ParserError):
                    return {"success": False,
                            "error": "Not a valid JSON or YAML format."}
            return metadata


def get_api_metadata_by_path(file_path):
    if os.path.exists(file_path):
        with open(file_path) as in_f:
            try:
                metadata = json.load(in_f)
            except ValueError:
                in_f.seek(0)
                try:
                    metadata = yaml.load(in_f)
                except (yaml.scanner.ScannerError,
                        yaml.parser.ParserError):
                    return {"success": False,
                            "error": "Not a valid JSON or YAML format."}
        return metadata
    else:
        return {"success": False, "error": "Invalid metadata file path."}


def get_api_metadata(metadata_src):
    if isinstance(metadata_src, str) and metadata_src:
        if metadata_src.startswith('http') or metadata_src.startswith('ftp'):
            return get_api_metadata_by_url(metadata_src)
        else:
            return get_api_metadata_by_path(metadata_src)
    else:
        return {"success": False, "error": "Invalid metadata field value."}


def validate_api_metadata(metadata_src):
    VALIDATE_API = 'http://dev.smart-api.info/api/validate'
    if metadata_src.startswith('http') or metadata_src.startswith('ftp'):
        metadata_url = metadata_src
    else:
        metadata_url = "https://raw.githubusercontent.com/NCATS-Tangerine/translator-api-registry/master/"
        metadata_url += metadata_src

    res = requests.get(VALIDATE_API, {'url': metadata_url})
    valid = res.json()
    return valid


class TestAPIRegistry(unittest.TestCase):
    def setUp(self):
        with open("./API_LIST.yml") as in_f:
            self.api_d = yaml.load(in_f)

    def test_api_list(self):
        self.assertTrue("APIs" in self.api_d)
        api_li = self.api_d["APIs"]
        for api in api_li:
            self.assertTrue("metadata" in api,
                            "Missing \"metadata\" in this API entry:\n" + pprint.pformat(api))

    def test_api_metadata(self):
        api_li = self.api_d["APIs"]
        for api in api_li:
            metadata = get_api_metadata(api['metadata'])
            api_title = api.get('info', {}).get('title', '')
            self.assertFalse(metadata.get('success', None) is False,
                             "Fail to retrieve metadata:\n" +
                             "\tAPI: {0}\n\tError: {1}".format(api_title, metadata['error']))
            self.assertTrue(metadata.get('tags', None),
                            "Missing required \"tags\" field in the metadata content.\n" +
                            "\tAPI: {}".format(api_title))
            self.assertTrue('translator' in [t['name'] for t in metadata['tags']],
                            "Requires \"translator\" as one of tags in the metadata content.\n" +
                            "\tAPI: {}".format(api_title))

            valid = validate_api_metadata(api['metadata'])
            self.assertTrue(valid.get('valid', False),
                            "Validation Error.\n" +
                            "\tAPI: {0}\n\tError: {1}".format(api_title, valid.get('error', '')))


if __name__ == '__main__':
    unittest.main()
