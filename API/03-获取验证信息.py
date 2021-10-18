# _*_ conding utf-8 _*_
__author__ = "zeng"
__data__ = "2021/10/9 7:25"

# @Filename : 03-获取验证信息.py

from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
print('=' * 30)
title = driver.title
print('title' + title)

now_url = driver.current_url
print(now_url)

driver.find_element_by_id("kw").send_keys("Selenium")
driver.find_element_by_id("su").click()
time.sleep(5)
print('=' * 30)

title = driver.title
print('title:' + title)

now_url = driver.current_url
print(now_url)

num = driver.find_element_by_class_name("nums_text").text
print(num)

driver.quit()
