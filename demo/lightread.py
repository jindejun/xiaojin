##轻阅读正式环境任务下发

# coding = utf-8
from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
driver = webdriver.Chrome()
driver.get('http://r.zhongzhuoxin.com')
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element_by_id('loginname').send_keys('admin')
driver.find_element_by_id('password').send_keys('adminzzx')
driver.find_element_by_id('code').send_keys('wnyzm')
driver.find_element_by_id('to-recover').click()
time.sleep(3)
#进入任务管理
driver.find_element_by_css_selector('#sidebar-collapse > i').click()
driver.find_element_by_css_selector('#lm29 > a > span').click()
time.sleep(1)
driver.find_element_by_css_selector('#z46 > a').click()
#将iframe切换到任务管理页，添加任务
driver.switch_to.frame(driver.find_element_by_id('mainFrame'))
driver.switch_to.frame(driver.find_element_by_id('page_z46'))
driver.find_element_by_css_selector('#Form > table > tbody > tr > td:nth-child(3) > a').click()
#切换到首页iframe
driver.switch_to.default_content()
#切换到添加任务页面iframe
driver.switch_to.frame(driver.find_element_by_id('_DialogFrame_0'))
driver.find_element_by_css_selector('#NAME').send_keys(u'测试1115')
driver.find_element_by_css_selector('#MMS_ID').send_keys('6106')
driver.find_element_by_css_selector('#GWNUMBER').click()
driver.find_element_by_css_selector('#GWNUMBER > option:nth-child(2)').click()
driver.find_element_by_css_selector('#TASK_TYPE').click()
driver.find_element_by_css_selector('#TASK_TYPE > option:nth-child(2)').click()
# driver.find_element_by_css_selector('#MOBILE_GROUP').click()
# driver.find_element_by_css_selector("#MOBILE_GROUP>[value='308']").click()
s = driver.find_element_by_css_selector('#MOBILE_GROUP')
Select(s).select_by_value('3314')
group = driver.find_element_by_css_selector("#MOBILE_GROUP>[value='3314']").text
# print(group)
js = 'document.getElementById("SEND_TIME").removeAttribute("readonly")'
driver.execute_script(js)
driver.find_element_by_id('SEND_TIME').send_keys('2018-11-15 17:04')
time.sleep(1)
driver.find_element_by_id('SEND_TIME').click()
js1 = 'document.getElementById("REISSUE_TIME").removeAttribute("readonly")'
driver.execute_script(js1)
driver.find_element_by_id('REISSUE_TIME').send_keys('2018-11-15 17:06')
time.sleep(1)
driver.find_element_by_id('REISSUE_TIME').click()
##启用灰名单
# s1 = driver.find_element_by_css_selector('#IS_GRAY')
# Select(s1).select_by_value('1')
driver.find_element_by_css_selector('#TASK_DESC').send_keys('test')
time.sleep(1)
try:
    if u'测试号码组' in group:
        driver.find_element_by_css_selector('#table_report > tbody > tr:nth-child(11) > td > a.btn.btn-mini.btn-primary').click()
except Exception as e:
    print(u'号码组异常或任务名已存在')
#切回首页
driver.switch_to.default_content()
time.sleep(2)
driver.find_element_by_css_selector('#z51 > a').click()

#切换到任务审核iframe,审核通过
time.sleep(3)
driver.switch_to.frame(driver.find_element_by_id('mainFrame'))
driver.switch_to.frame(driver.find_element_by_id('page_z51'))
driver.find_element_by_css_selector('#table_report > tbody > tr:nth-child(1) > td:nth-child(16) > div > div > button > i').click()
driver.find_element_by_css_selector('#table_report > tbody > tr:nth-child(1) > td:nth-child(16) > div > div > ul > li:nth-child(3) > a').click()
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[2]/div[2]/a[2]').click()
#查看任务状态
driver.refresh()
time.sleep(2)
driver.switch_to.default_content()
driver.find_element_by_css_selector('#sidebar-collapse > i').click()
driver.find_element_by_css_selector('#lm29 > a > span').click()
time.sleep(1)
driver.find_element_by_css_selector('#z46 > a').click()
driver.switch_to.frame(driver.find_element_by_id('mainFrame'))
driver.switch_to.frame(driver.find_element_by_id('page_z46'))
text = driver.find_element_by_xpath(".//*[@id='table_report']/tbody/tr[1]/td[10]").text
if u'待发送' == text:
    print('任务审核通过，待发送')
else:
    print('任务状态异常，当前状态为：%s' %text)

time.sleep(2)
driver.quit()