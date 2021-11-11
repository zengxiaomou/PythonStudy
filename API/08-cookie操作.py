# _*_ conding utf-8 _*_


# @Filename : 08-cookie操作.py


from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

cookies = driver.get_cookies()
print(cookies)

# 添加cookie
driver.add_cookie({'name': 'zeng', 'value': '真的恶作剧'})

cookies = driver.get_cookies()
print("新cookie:", cookies)

# 遍历指定的cookies
for cookie in driver.get_cookies():
    print("%s->%s" % (cookie['name'], cookie['value']))

print("=="*20)
#删除cookie
driver.delete_cookie("zeng")
for cookie in driver.get_cookies():
    print("%s->%s" % (cookie['name'], cookie['value']))

driver.quit()
