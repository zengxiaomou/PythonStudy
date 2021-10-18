from selenium import webdriver
import time

# 请求浏览器
driver =webdriver.Chrome()
# 指定目录
#driver =webdriver.Chrome(executable_path="D:/chromedriver")
driver.get("https://www.baidu.com/")

#1.tag标签 定位，写入值
tag=driver.find_element_by_tag_name("input")
#按钮点击
print(tag)

#暂停3秒
time.sleep(3)
#退出浏览器
driver.quit()











if __name__ == '__main__':
    TheApp = 0