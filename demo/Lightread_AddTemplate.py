##轻阅读正式环境添加数字短信模板

# coding = utf-8
from selenium import webdriver
import time
import os
driver = webdriver.Chrome()
driver.get('http://r.zhongzhuoxin.com')
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element_by_id('loginname').send_keys('zhiyin')
driver.find_element_by_id('password').send_keys('Zhi_Yin211')
driver.find_element_by_id('code').send_keys('wnyzm')
driver.find_element_by_id('to-recover').click()
time.sleep(3)
#进入数字短信管理
driver.find_element_by_css_selector('#sidebar-collapse > i').click()
driver.find_element_by_css_selector('#lm24 > a > span').click()
time.sleep(1)
driver.find_element_by_css_selector('#z25 > a').click()
driver.switch_to.frame(driver.find_element_by_id('mainFrame'))
driver.switch_to.frame(driver.find_element_by_id('page_z25'))
driver.find_element_by_css_selector('.btn.btn-small.btn-success').click()
driver.switch_to.default_content()
driver.switch_to.frame(driver.find_element_by_id('_DialogFrame_0'))
title = u'自动化测试模板'
driver.find_element_by_css_selector('#TITLE').send_keys(title)
driver.find_element_by_css_selector('#SEND_TIME').click()
# driver.find_element_by_css_selector('.table-condensed > tbody > tr:nth-child(5) > td:nth-child(3)').click()
driver.find_element_by_css_selector('.active.day').click()#任务下发时间为当天
driver.find_element_by_css_selector('#HF_URL').click()
driver.find_element_by_css_selector('#HF_URL').send_keys('http://woqu.wo.cn/h5/h/6389')
driver.find_element_by_css_selector('#CHOIC>option[value="9"]').click()
driver.find_element_by_css_selector('#SMS_CONTENT').send_keys('自动化测试模板内容')
driver.find_element_by_css_selector('#text').send_keys('自动化测试模板内容')
driver.find_element_by_xpath(".//*[@id='table_report']/tbody/tr[2]/td/a").click()
driver.find_element_by_css_selector('#myDropzone > div').click()
os.system('D:\\AutoIt\\AutoIt3\\upload.exe')
time.sleep(3)
driver.find_element_by_css_selector('#table_report > tbody > tr:nth-child(8) > td > a.btn.btn-mini.btn-primary').click()
driver.switch_to.default_content()
driver.switch_to.frame(driver.find_element_by_id('mainFrame'))
driver.switch_to.frame(driver.find_element_by_id('page_z25'))
text = driver.find_element_by_css_selector('#table_report > tbody > tr > td:nth-child(4)').text
if text in title:
    print(u'数字短信创建成功')
else:
    print(u'数字短信创建失败')
time.sleep(2)
driver.quit()