from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.webdriver import TouchActions


# 关闭w3c标准 安全模式，非真人操作，模拟操作
opt = webdriver.ChromeOptions()
opt.add_experimental_option('w3c', False)

#driver = webdriver.Chrome(chrome_options=opt)
driver = webdriver.Chrome(options=opt)

driver.get('http://www.jq22.com/yanshi4976')
#driver.get('https://www.jq22.com/yanshi3714')

sleep(5)

driver.switch_to.frame("iframe")
driver.find_element_by_id("appDate").click()


dwwos = driver.find_elements_by_class_name("dwwo")
action =webdriver.TouchActions(driver)
year =dwwos[0]
month =dwwos[1]
day =dwwos[2]

# 滑动年
action.scroll_from_element(year,0,100).perform()
# 滑动月
action.scroll_from_element(month,0,-8).perform()
# 滑动日
action.scroll_from_element(day,0,30).perform()



sleep(3)

driver.quit()
