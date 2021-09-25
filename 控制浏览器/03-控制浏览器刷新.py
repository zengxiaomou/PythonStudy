from selenium import webdriver
from time import sleep

# 请求浏览器
driver =webdriver.Chrome()
first_url = "http://www.baidu.com"
driver.get(first_url)

sleep(3)
driver.refresh()
sleep(5)

driver.quit()



