# _*_ conding utf-8 _*_
__author__ = "zeng"
__data__ = "2021/10/8 21:20"

# @Filename : 02-键盘操作.py

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

search = driver.find_element_by_id("kw")
# 在输入框输入内容
search.send_keys("seleniumm")
time.sleep(2)
# 删除多输入
search.send_keys(Keys.BACK_SPACE)
time.sleep(2)

# 输入空格+
search.send_keys(Keys.SPACE)
time.sleep(2)
search.send_keys("教程")

# 输入组合框 ctrl+a
search.send_keys(Keys.CONTROL, 'a')
time.sleep(2)
# 输入组合框 ctrl+x
search.send_keys(Keys.CONTROL, 'x')
time.sleep(2)
# 输入组合框 ctrl+v
search.send_keys(Keys.CONTROL, 'v')
time.sleep(2)
# 回车
search.send_keys(Keys.ENTER)
time.sleep(2)

driver.quit()
