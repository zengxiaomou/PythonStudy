# _*_ conding utf-8 _*_



from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://email.163.com/")
time.sleep(2)
#iframe 嵌套
#switch_to，切换进入
#start-with:匹配一个属性开始位置的关键字
driver.switch_to.frame(driver.find_element_by_xpath("//iframe[starts-with(@id,'x-URS-iframe')]"))

driver.find_element_by_name("email").send_keys('zeng')
driver.find_element_by_name("password").send_keys("zeng")

time.sleep(3)
#切换回来
driver.switch_to.default_content()
driver.quit()



