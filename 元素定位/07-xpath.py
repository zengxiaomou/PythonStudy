from selenium import webdriver
import time

# 请求浏览器
driver =webdriver.Chrome()
# 指定目录
#driver =webdriver.Chrome(executable_path="D:/chromedriver")
driver.get("https://www.baidu.com/")

#1.相对标签 定位，写入值
driver.find_element_by_xpath('//input[@class="s_ipt"]').send_keys("相对路径")

# 缩影
#按钮点击


#暂停3秒
time.sleep(3)
#退出浏览器
driver.quit()











if __name__ == '__main__':
    TheApp = 0