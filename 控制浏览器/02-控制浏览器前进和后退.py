from selenium import webdriver
from time import sleep

# 请求浏览器
driver =webdriver.Chrome()
first_url = "http://www.baidu.com"
driver.get(first_url)


second_url="http://news.baidu.com/"
driver.get(second_url)
#后退
driver.back()
sleep(2)
#前进
driver.forward()

driver.quit()



