

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

driver.set_window_size(800,600)
driver.find_element_by_id("kw").send_keys("selenium3")
driver.find_element_by_id("su").click()

#通过Js设置浏览器窗口的滚动条位置
js= "window.scrollTo(200,450)"
driver.execute_script(js)
time.sleep(3)
driver.quit()



