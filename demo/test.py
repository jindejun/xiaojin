from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
driver.find_element_by_id('kw').send_keys('秦始皇')
time.sleep(3)
driver.find_element_by_id('su').click()
driver.find_element_by_css_selector('#content_left > div > h3 > a').click()