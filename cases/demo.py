import json
import os
import subprocess
import time

import requests

# url = "http://localhost:8889/postDemo"
# headers = {
#     "content-type": "application/json"
# }
# data = {
#     "name": "james",
#     "age": "23"
# }
# response = requests.post(url=url, data=json.dumps(data), headers=headers)
# print(response.text)
# print(os.path.dirname(os.getcwd()))
# print(os.path.join(os.getcwd(),"demo.py"))
# print(os.path.abspath(__file__))
# print(os.path.split(__file__))
# os.mkdir("ceshi")

# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.common.keys import Keys
# from selenium import webdriver
#
# path = r"C:\Users\ASUS\PycharmProjects\daine-study\chromedriver.exe"
# driver = webdriver.Chrome(path)
# # driver.get("https://g.58.com/")
# driver.maximize_window()
# driver.get("https://ke.qq.com/")
# driver.get("file:///C:/Users/ASUS/sublimeText/daine_js/1.2.html")



# hot_city = driver.find_elements_by_css_selector(".city-list .country")
# for one in hot_city:
#     print(one.text)
#
# png_element = driver.find_element_by_css_selector(".last img[alt=\"综合\"]")
# png_element.click()
# handles = driver.window_handles
# current_handle = driver.current_window_handle
# # driver.switch_to.window(handles[-1])
# for handle in handles:
#     driver.switch_to.window(handle)
#     if "我们过的是" in driver.title:
#         print(driver.title)
#         break
# new_window_message = driver.find_element_by_css_selector(".cp1")
# if "driver.quit()我们过的是" in new_window_message.text:
#     print("测试通过")
#
# driver.quit()
"""
js = "document.documentElement.scrollTop=1000"
driver.execute_script(js)
time.sleep(3)
js2 = "document.documentElement.scrollTop=0"
driver.execute_script(js2)

"""

# element = driver.find_element_by_css_selector(" a[title=\"分类\"]")
# js = "setTimeout(function(){debugger;},3000)"
# driver.execute_script(js)
# ActionChains(driver).move_to_element(element).perform()
# time.sleep(2)
# driver.find_element_by_css_selector(".mod-nav__wrap-nav-hot a[title=\"前端开发\"]").click()
# time.sleep(2)
# driver.quit()



"""   
project_path = os.path.dirname(os.getcwd())
print(project_path)
file_path = project_path + "/my_screenshot/"
if not os.path.exists(file_path):
    os.mkdir(file_path)
image_name = time.strftime("%Y%m%d-%H%M%S", time.localtime())
file_name = file_path + image_name + '.png'


driver.save_screenshot(file_name)
"""

import yaml
import _json
from enum import Enum
# import threading
# class RunAll():
#     def run(self,num):
#         for i in range(num):
#             time.sleep(1)
#             print("在跑步")
#
#     def sing(self,num):
#          for i in range(num):
#             time.sleep(1)
#             print("在唱歌")
#
# if __name__ == '__main__':
#     t_run = threading.Thread(target=RunAll().run,args=(10,))
#     t_run.start()
#     t_sing = threading.Thread(target=RunAll().sing,args=(4,))
#     t_sing.start()

import threading
# with open("daine.txt","r",encoding='utf-8')as f:
#     data = f.readline()
#     while data:
#         data = f.readline()
#         print(data)

# from enum import Enum
#
# class Demo(Enum):
#     name = "daine"
#     age = 12
#
# if __name__ == '__main__':
#
#     print(Demo.name.value)

data = {
    "name":"daine",
    "age":"26"
}
import httpx,asyncio

resp = httpx.get("http://localhost:8889/v1/getDemo",params=data)
print(resp.json())

a = {
    "name":"james",
    "age":"23"
}
print(httpx.post("http://localhost:8889/postDemo",json=a).json())
b = {
    "name":"daine",
    "sex":"male"
}
print(httpx.post("http://localhost:8889/postSecond",data=b).json())
print("11111")
async def main():
    async with httpx.AsyncClient() as client:
        resp = await client.post('http://localhost:8889/postSecond',
                                 data=b)
        result = resp.json()
        print(result)


asyncio.run(main())










































