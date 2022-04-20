import pytest,unittest
# import pytest_dependency
import requests,json
# pytest实现依赖测试
class TestAll():

    def test0(self):
        params = {
            "height":"185",
            "weight":"174"
        }
        rs = requests.get("http://localhost:8889/v1/getFirst",json=params)
        print(rs.json())

    def test1(self):
        payload = {
            "name": "daine",
            "age": "26"
        }
        rs = requests.get(url="http://localhost:8889/v1/getDemo",params=payload)
        print(rs.json())

    def test2(self):
        data = {
            "name":"james",
            "age":"23"
        }
        rs = requests.post("http://localhost:8889/postDemo",json=data)
        print(rs.json())

    def test3(self):
        data = {
            "name":"daine",
            "sex":"male"
        }
        rs = requests.post("http://localhost:8889/postSecond",data=data)
        print(rs.json())


    # def test2(self):
    # def test2(self):
    #     print("222222")
    #     assert 3 == 3

if __name__ == '__main__':
    # pytest.main(["test_01.py::TestAll::test2"])
    pytest.main(['-s'])

    
    
    
            base64编码后上传文件：  data = {'base64Data':'data:image/png;base64,'+base64.b64encode(open(image_path,'rb').read()).decode()}
            files格式上传文件：   files = {'file':open(image_path,'rb')}

