# coding=utf-8
import time
from selenium import webdriver
from util.V3loginclass import login_go
driver = webdriver.Chrome()
login = login_go(driver)
login.all_actions('http://web.zzx9.cn','automation','Automation')
time.sleep(2)
#关闭首页
driver.find_elements_by_class_name('panel-with-icon')[2].click()
driver.find_elements_by_class_name('nav')[3].click()
driver.find_elements_by_class_name('tabs-close')[0].click()
#通过iframe切换至数字模板库页
driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
driver.find_element_by_id('datagrid-row-r1-1-0').click()
driver.find_element_by_css_selector('.l-btn-icon.icon-redo').click()#点击发送
driver.switch_to.frame(driver.find_element_by_css_selector('#uploadIfram'))
driver.find_element_by_css_selector('#mobiless > input').send_keys('13260276178')
driver.find_element_by_css_selector('#uploadOneDiv>input').click()
driver.find_element_by_css_selector('#playList > a > span > span').click()
driver.refresh()
driver.switch_to.default_content()
driver.find_elements_by_class_name('panel-with-icon')[4].click()
driver.find_elements_by_class_name('nav')[9].click()
time.sleep(35)
driver.find_element_by_class_name('tabs-close').click()
iframe2 = driver.find_element_by_tag_name('iframe')
driver.switch_to.frame(iframe2)
text1 = driver.find_elements_by_class_name('datagrid-cell-c1-smsFlag')[0].text
time.sleep(5)
if u'成功' in text1:
    print('successful')
else:
    print('failed')
driver.quit()