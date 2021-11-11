# _*_ conding utf-8 _*_
__author__ = "zeng"
__data__ = "2021/10/10 16:50"
# @Filename : 06-定位一组元素.py


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()

time.sleep(2)
texts = driver.find_elements_by_xpath("//div[@id='2']/h3/a")
print(len(texts))
time.sleep(2)

for i in texts:
    print(i.text)

driver.quit()
