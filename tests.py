import unittest

import yaml


class TestAPIRegistry(unittest.TestCase):
    def test_api_list(self):
        with open("./API_LIST.yml") as in_f:
            api_d = yaml.load(in_f)
        self.assertTrue("APIs" in api_d)
        api_li = api_d["APIs"]
        for api in api_li:
            self.assertTrue("metadata" in api)

if __name__ == '__main__':
    unittest.main()
