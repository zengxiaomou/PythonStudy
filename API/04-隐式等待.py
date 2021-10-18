# _*_ conding utf-8 _*_
__author__ = "zeng"
__data__ = "2021/10/9 7:35"
# @Filename : 04-隐式等待.py

from selenium import webdriver
from time import ctime
from selenium.common.exceptions import NoSuchElementException


driver = webdriver.Chrome()
#隐式等待
driver.implicitly_wait(10)

driver.get("http://www.baidu.com")
try:
    print(ctime())
    driver.find_element_by_id('kw').send_keys("selenium")
except NoSuchElementException as e:
    print(e)
finally:
    print(ctime())
    driver.quit()

