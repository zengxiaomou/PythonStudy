from selenium import webdriver
from time import sleep

# 请求浏览器
driver =webdriver.Chrome()
driver.get("http://www.baidu.com")

a1 = driver.find_element_by_class_name("lh").text
print(a1)

a2=driver.find_element_by_id("kw")
a2.clear()
a2.send_keys("selemium")
a2.submit()
print(a2.size)
sleep(3)
driver.quit()



