import requests
import unittest
import json
class RunCase(unittest.TestCase):

    def test_01(self):
        url = "http://localhost:8889/postDemo"
        headers = {
            "content-type": "application/json"
        }
        data = {
            "name": "james",
            "age": "23"
        }
        response = requests.post(url=url, data=json.dumps(data), headers=headers)
        print(response)

if __name__ == '__main__':
    unittest.main()