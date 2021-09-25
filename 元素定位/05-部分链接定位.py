from selenium import webdriver
import time

# 请求浏览器
driver =webdriver.Chrome()
# 指定目录
#driver =webdriver.Chrome(executable_path="D:/chromedriver")
driver.get("https://www.baidu.com/")

time.sleep(1)
#1.部分链接 定位
driver.find_element_by_partial_link_text("hao").click()


#暂停3秒
time.sleep(3)
#退出浏览器
driver.quit()











if __name__ == '__main__':
    TheApp = 0