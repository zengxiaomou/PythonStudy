# _*_ conding utf-8 _*_
__author__ = "zeng"
__data__ = "2021/10/8 21:03"

# @Filename : 01-鼠标操作.py


from selenium import webdriver
import time
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.maximize_window()
# 定位要悬停元素
above = driver.find_element_by_id("s-usersetting-top")
# 悬停操作
ActionChains(driver).move_to_element(above).perform()
# 定位到搜索

a1 = driver.find_element_by_link_text("搜索设置")
a1.click()

time.sleep(5)
driver.quit()
