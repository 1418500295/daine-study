import random
import re
import time

import requests
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import By
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

capabilities = {
    "platformName": 'Android',
    "deviceName": '46',
    "app": r'C:.apk'
}

# Converts capabilities to AppiumOptions instance
capabilities_options = UiAutomator2Options().load_capabilities(capabilities)

driver = webdriver.Remote(command_executor='http://localhost:4723/wd/hub', options=capabilities_options)
time.sleep(5)
# 测试过程录屏
cmd = 'scrcpy --no-display --record demo.mp4'
p = subprocess.Popen(cmd,shell=True)

ele = WebDriverWait(driver, 10, 0.5).until(
    EC.presence_of_element_located((By.ID, 'id/sure')))
ele.click()
time.sleep(2)
# driver.find_element(By.XPATH,'//id/btnLeft"]').click()
# 输入手机号码
ele = WebDriverWait(driver, 10, 0.5).until(EC.presence_of_element_located((By.XPATH,
                                                                           '//" and @text="手机号码"]')))
ele.send_keys('')
# driver.find_element(By.XPATH,'//android.widget.EditText[@resource-id="liuba.client.android.telephone.international:id/et" and @text="手机号码"]').send_keys('')
# 点击获取验证码
ele = WebDriverWait(driver, 10, 0.5).until(EC.presence_of_element_located((By.XPATH,
                                                                           '//android.widget_count_down"]')))
ele.click()
# driver.find_element(By.XPATH,'//wn"]').click()
time.sleep(5)

import numpy as np

time.sleep(2)
contexts = driver.contexts
print(contexts)
# 切换至webview
for i in contexts:
    if 'international' in i:
        driver.switch_to.context(i)
# 获取验证码背景图片
print(driver.current_context)
ele = WebDriverWait(driver, 10, 0.5).until(
    EC.presence_of_element_located((By.XPATH, 'iv[1]/div[2]')))
img_e = ele.get_attribute('style')
# img_e = driver.find_element(By.XPATH, "/html/b[1]/div[2]").get_attribute('style')
c = re.compile(r'background-image: url\("(.*?)"\)')
png = re.findall(c, img_e)
url = png[0]
from PIL import Image

req = requests.get(url)
with open('./c.png', 'wb') as file:
    file.write(req.content)
# img = Image.open('./c.png')
# net = (672,390)
# res1 = img.resize(net)
# res1.save('./c.png')
# 获取缺口图片对应实物
ele = WebDriverWait(driver, 10, 0.5).until(
    EC.presence_of_element_located((By.XPATH, '[1]/div[1]')))
img_e = ele.get_attribute('style')
# img_e = driver.find_element(By.XPATH, "/html/body/div[4]/div[1]/div[1]/div[2]/div/div/div[1]/div[1]/div[1]").get_attribute('style')
c = re.compile(r'background-image: url\("(.*?)"\)')
png = re.findall(c, img_e)
url = png[0]
from PIL import Image

req = requests.get(url)
with open('./c1.png', 'wb') as file:
    file.write(req.content)

# 识别缺口图片x坐标
import cv2


def identify_gap(bg, tp, out):
    # 读取背景图片和缺口图片
    bg_img = cv2.imread(bg)  # 背景图片
    tp_img = cv2.imread(tp)  # 缺口图片

    # 识别图片边缘
    bg_edge = cv2.Canny(bg_img, 100, 200)
    tp_edge = cv2.Canny(tp_img, 100, 200)

    # 转换图片格式
    bg_pic = cv2.cvtColor(bg_edge, cv2.COLOR_GRAY2RGB)
    tp_pic = cv2.cvtColor(tp_edge, cv2.COLOR_GRAY2RGB)

    # 缺口匹配
    res = cv2.matchTemplate(bg_pic, tp_pic, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)  # 寻找最优匹配
    X = max_loc[0]  # 缺口的X轴坐标

    # 绘制方框
    th, tw = tp_pic.shape[:2]
    tl = max_loc  # 左上角点的坐标
    br = (tl[0] + tw, tl[1] + th)  # 右下角点的坐标
    cv2.rectangle(bg_img, tl, br, (0, 0, 255), 2)  # 绘制矩形
    cv2.imwrite(out, bg_img)  # 保存在本地
    return tl[0]


gap_x = identify_gap('c.png', 'c1.png', './out.jpg')

# 输出缺口的 x 坐标
print(f"缺口的 x 坐标: {gap_x}")
# 显示结果
# cv2.imshow('Detected Gap', background_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
time.sleep(2)
# 获取滑块按钮
slide = WebDriverWait(driver, 10, 0.5).until(
    EC.presence_of_element_located((By.XPATH, '/htmldiv/div[3]/div')))
# slide = driver.find_element(By.XPATH,'/html/bo3]/div')
# 获取滑块x坐标
sx = slide.location.get('x')
print("按钮坐标", sx)
newDis = int(gap_x * 340 / 672 - sx)
# 模拟人为滑动轨迹
ActionChains(driver).click_and_hold(slide).perform()

i = 1
moved = 0
mid = gap_x * 4/5
while moved < gap_x:
    if moved < mid:
        x = random.randint(20, 25)  # 每次移动3到10像素
        moved += x
        ActionChains(driver).move_by_offset(xoffset=x, yoffset=0).perform()
        print("第{}次移动后，位置为{}".format(i, moved))
        i+=1
    if mid <= moved < gap_x:
        x = random.randint(1, 4)  # 每次移动3到10像素
        moved += x
        ActionChains(driver).move_by_offset(xoffset=x, yoffset=0).perform()
        print("第{}次移动后，位置为{}".format(i, moved))
        i += 1
ActionChains(driver).release().perform()
time.sleep(2)
# 切换至native
driver.switch_to.context(contexts[0])
time.sleep(1)
# 输入验证码
ele = WebDriverWait(driver, 10, 0.5).until(EC.presence_of_element_located((By.XPATH,'"]')))
ele.send_keys('1234')
# driver.find_element(By.XPATH,'//"]').send_keys('1234')
# 点击登录
ele = WebDriverWait(driver, 10, 0.5).until(EC.presence_of_element_located(
    (By.XPATH, '//n"]')))
ele.click()
# driver.find_element(By.XPATH,'//_login"]').click()
# 点击下次再说
ele = WebDriverWait(driver, 10, 0.5).until(EC.presence_of_element_located(
    (By.XPATH, '/t"]')))
ele.click()
# driver.find_element(By.XPATH,'/t"]').click()
# 允许相关权限
ele = WebDriverWait(driver, 10, 0.5).until(
    EC.presence_of_element_located((By.ID, '')))
ele.click()
time.sleep(1)
ele = WebDriverWait(driver, 10, 0.5).until(
    EC.presence_of_element_located((By.ID, '')))
ele.click()
# driver.find_element(By.XPATH,'//_button"]').click()
# driver.find_element(By.XPATH,'//utton"]').click()
# 点击取消
ele = WebDriverWait(driver, 10, 0.5).until(EC.presence_of_element_located(
    (By.XPATH, '/el"]')))
ele.click()
# driver.find_element(By.XPATH,'ancel"]').click()
#结束录屏
os.kill(p.pid,signal.CTRL_C_EVENT)
