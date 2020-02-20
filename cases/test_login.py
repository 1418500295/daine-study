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

url = "http://localhost:8889/get/with/cookies"

headers = {
    "Cookie": "login=true;base=localhost"
}

result = requests.get(url,headers=headers)
print(result.text)
