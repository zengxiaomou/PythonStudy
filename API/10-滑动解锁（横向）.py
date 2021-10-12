from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import UnexpectedAlertPresentException

# 关闭w3c标准 安全模式，非真人操作，模拟操作
opt = webdriver.ChromeOptions()
opt.add_experimental_option('w3c', False)

#driver = webdriver.Chrome(chrome_options=opt)
driver = webdriver.Chrome(options=opt)

driver.get('https://www.helloweba.net/demo/2017/unlock/')
driver.implicitly_wait(5)

dragget =driver.find_elements_by_class_name("slide-to-unlock-handle")[0]


action =ActionChains(driver)

#按下鼠标左键执行
action.click_and_hold(dragget).perform()

for index in range(200):
    try:
        action.move_by_offset(2,0).perform() #平行移动鼠标
    except UnexpectedAlertPresentException as e :
        break
    action.reset_actions() #清除
    time.sleep(0.2)
#打印警告框提示
success_text =driver.switch_to.alert.text
print(success_text)


driver.quit()
