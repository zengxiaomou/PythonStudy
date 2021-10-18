from selenium import webdriver
import time

# 请求浏览器
driver =webdriver.Chrome()
# 指定目录
#driver =webdriver.Chrome(executable_path="D:/chromedriver")
driver.get("https://www.baidu.com/")

#1.CLASS定位
driver.find_element_by_css_selector(".s_ipt").send_keys("class")
#2.id定位
driver.find_element_by_css_selector(".#kw").send_keys("id")
#3.标签层级关系定位
driver.find_element_by_css_selector("span>input").send_keys("标签")
#4.组合定位
driver.find_element_by_css_selector("form.fm>span>input").send_keys("组合")

#5.属性定位
driver.find_element_by_css_selector("[name=wd]").send_keys("属性")


#按钮点击


#暂停3秒
time.sleep(3)
#退出浏览器
driver.quit()











if __name__ == '__main__':
    TheApp = 0