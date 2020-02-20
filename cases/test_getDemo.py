import requests
import unittest
import json
class RunCase(unittest.TestCase):

    def test_01(self):
        url = "http://localhost:8889/v1/getFirst"
        data = {
            "height": "185",
            "weight": "174"
        }
        result = requests.get(url=url,params=json.dumps(data))
        print(result)

if __name__ == '__main__':
    unittest.main()