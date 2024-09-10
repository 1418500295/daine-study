import base64
import random
import re
import time

import cv2
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get("https://accounts.douban.com/passport/login")
driver.find_element(By.XPATH, '//*[@id="account"]/div[2]/div[2]/div/div[2]/div[1]/div[3]/div/div/div').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="ui-dialog-id-global_phone"]/ul/li[26]/span[2]').click()
time.sleep(1)
ele = driver.find_element(By.XPATH, '//*[@id="account"]/div[2]/div[2]/div/div[2]/div[1]/div[3]/div/input')
ele.click()
ele.send_keys("")
driver.find_element(By.XPATH, '//*[@id="account"]/div[2]/div[2]/div/div[2]/div[1]/div[4]/div/div/a').click()
time.sleep(7)
ele_xpath = '//*[@id="tcaptcha_iframe_dy"]'
driver.switch_to.frame(driver.find_element(By.XPATH,ele_xpath))
img_e = driver.find_element(By.ID, "slideBg").get_attribute('style')
c = re.compile(r'background-image: url\("(.*?)"\)')
png = re.findall(c,img_e)
url = png[0]

req = requests.get(url)
with open('./test.png','wb')as file:
    file.write(req.content)


def get_tracks(distance):
    """
    拿到移动轨迹，模仿人的滑动行为，先匀加速，后匀减速
    匀变速运动公式：
    v = v0 + at
    s = v0t + 1/2a*t*t
    """

    # 初速度
    v = 0
    # 单位时间为0.3秒统计移动轨迹，即0.3秒内的移动位移
    t = 0.3
    # 位置/移动轨迹列表，列表内的一个元素代表0.3秒内的位移
    tracks = []
    # 当前的位移
    current = 0

    # 当距离 < mid值时开始匀加速，当距离 > mid值时开始匀减速
    mid = distance * 4/5

    # current移动位移，小于滑块的距离
    while current < distance:
        if current < mid:
            # 匀加速
            a = 2

        else:
            # 匀减速
            a = -3

        # 初速度
        v0 = v
        # 0.3秒内的位移
        s = v0*t + 1/2 * a * (t**2)
        # 当前位置
        current += s
        # 添加到轨迹列表
        tracks.append(round(s))
        # 速度已经到达v， 该速度作为下次的初速度
        v = v0 + a*t

        # 每0.3秒移动的位移所有元素移动轨迹
    return tracks

import cv2
import numpy as np


# 1. 加载图像
background_img = cv2.imread('./test.png')  # 背景图像（带缺口）
# slider_img = cv2.imread('slider_image.jpg')  # 滑块图像

# 2. 图像预处理
gray_bg = cv2.cvtColor(background_img, cv2.COLOR_BGR2GRAY)  # 背景图像转灰度
# gray_slider = cv2.cvtColor(slider_img, cv2.COLOR_BGR2GRAY)  # 滑块图像转灰度

# 3. 边缘检测
edges_bg = cv2.Canny(gray_bg, 50, 150)  # 背景图像边缘检测

# 4. 轮廓检测
contours, _ = cv2.findContours(edges_bg, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 5. 找到最大轮廓（通常是缺口）
max_contour = max(contours, key=cv2.contourArea)

# 6. 获取缺口的 x 坐标
x, y, w, h = cv2.boundingRect(max_contour)
gap_x = x

# 7. 在原图上绘制轮廓和矩形框
cv2.rectangle(background_img, (x, y), (x + w, y + h), (0, 255, 0), 2)

# 输出缺口的 x 坐标
print(f"缺口的 x 坐标: {gap_x}")

# 显示结果
# cv2.imshow('Detected Gap', background_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
time.sleep(2)

slide = driver.find_element(By.XPATH,'//*[@id="tcOperation"]/div[6]')
sx = slide.location.get('x')
print("按钮坐标",sx)
newDis = int(gap_x*340/672-sx)
ActionChains(driver).click_and_hold(slide).perform()
i = 0
moved = 0
while moved < newDis:
    x = random.randint(3, 10)  # 每次移动3到10像素
    moved += x
    ActionChains(driver).move_by_offset(xoffset=x, yoffset=0).perform()
    print("第{}次移动后，位置为{}".format(i, sx))
    i += 1
ActionChains(driver).release().perform()

time.sleep(5)


