# _*_ conding utf-8 _*_
__author__ = "zeng"
__data__ = "2021/10/9 7:46"

# @Filename : 05-显示等待.py


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

#显示等待
element=WebDriverWait(driver, 5, 0.5).until(EC.visibility_of_element_located((By.ID,'kw')))
element.send_keys("selenium")
time.sleep(2)



driver.quit()
