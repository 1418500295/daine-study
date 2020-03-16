import os

import pytest
import requests,json

# class RunCase:
#
#     def test_01(self):
#         print("test_01")
#
#     def test_02(self):
#         print("test_02")
#
# if __name__ == '__main__':
#     pytest.main()

url = "http://localhost:8889/v1/getDemo"

data = {
    "name": "daine",
    "age": "26"
}
res = requests.get(url,data)

print(os.path.dirname(os.getcwd()))







