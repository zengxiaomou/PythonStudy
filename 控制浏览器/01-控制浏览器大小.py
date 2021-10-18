from selenium import webdriver
from time import sleep

# 请求浏览器
driver =webdriver.Chrome()
driver.get("http://www.baidu.com")

print("设置浏览器宽480")
driver.set_window_size(480, 800)
sleep(3)
#最大化
driver.maximize_window()
driver.quit()


