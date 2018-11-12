# coding=utf-8
import time
from selenium import webdriver
from util.V3loginclass import login_go,noturl
driver = webdriver.Chrome()
login = login_go(driver)
login.all_actions('http://web.zzx9.cn','automation','Automation')
#点击任务管理
driver.find_elements_by_class_name('panel-with-icon')[3].click()
driver.find_element_by_xpath('//*[@id="nav"]/div[4]/div[2]/ul/li[2]/div/a/span[2]').click()
time.sleep(2)
driver.find_elements_by_class_name('tabs-close')[0].click()
driver.switch_to.frame(driver.find_element_by_tag_name('iframe'))
#添加任务
time.sleep(1)
driver.find_elements_by_class_name('l-btn-icon-left')[2].click()
driver.find_element_by_xpath('//*[@id="addftask"]/div[1]/input').send_keys('自动化测试任务下发')
driver.find_element_by_css_selector('#upmmsId').send_keys('867986')
driver.find_element_by_css_selector('#d1').click()
driver.switch_to.default_content()
driver.switch_to.frame(1)
#选择下发时间
time.sleep(1)
driver.find_element_by_css_selector('#dpTime > table > tbody > tr:nth-child(1) > td:nth-child(1) > input:nth-child(4)').click()
driver.find_element_by_css_selector('#dpTimeUp').click()#点击一次为5分钟后下发
# driver.find_element_by_css_selector('#dpTimeUp').click()#点击两次为10分钟后下发
driver.find_element_by_css_selector('#dpOkInput').click()
#此处选择完日期需要切换回首页iframe然后切到任务iframe
driver.switch_to.default_content()
driver.switch_to.frame(driver.find_element_by_tag_name('iframe'))
driver.find_element_by_xpath('//*[@id="addftask"]/div[5]/span/span/a').click()
time.sleep(2)
driver.find_element_by_css_selector('#_easyui_tree_1 > span.tree-checkbox.tree-checkbox0').click()
driver.find_element_by_css_selector('#addftask > div:nth-child(8) > textarea').send_keys(u'自动化测试')
driver.find_element_by_xpath('//*[@id="addftask"]/div[5]/span/span/a').click()
# driver.find_element_by_css_selector('#addtask').click()
driver.find_element_by_css_selector('#dlg-buttons > a:nth-child(1) > span > span.l-btn-text').click()
#提交任务
driver.switch_to.default_content()
driver.switch_to.frame(driver.find_element_by_tag_name('iframe'))
time.sleep(2)
tijiao = driver.find_element_by_css_selector('#datagrid-row-r1-2-0 > td:nth-child(16) > div > a > span > span.l-btn-text').text
# print(tijiao)
if u'提交' in tijiao:
    driver.find_element_by_css_selector('#datagrid-row-r1-2-0 > td:nth-child(16) > div > a > span > span.l-btn-text').click()
else:
    driver.find_element_by_css_selector('#datagrid-row-r1-2-1 > td:nth-child(16) > div > a > span > span.l-btn-text').click()
driver.find_element_by_css_selector('body > div.panel.window.messager-window > div.messager-body.panel-body.panel-body-noborder.window-body > div.messager-button > a:nth-child(1) > span > span').click()
#判断新建的任务为第一条还是第二条
line1 = driver.find_element_by_css_selector('#datagrid-row-r1-2-0 > td:nth-child(16) > div > a > span > span.l-btn-text').text
line2 = driver.find_element_by_css_selector('#datagrid-row-r1-2-1 > td:nth-child(16) > div > a > span > span.l-btn-text').text
# print(line1)
# print(line2)
time.sleep(1)
if u'待审批' == line1 or line2:
    print(u'任务创建成功，状态为待审批！')
else:
    print(u'任务创建失败')
time.sleep(2)
#退出登录
driver.switch_to.default_content()
driver.find_element_by_css_selector('#indexLayout > div.panel.layout-panel.layout-panel-north > div > div > a:nth-child(2) > span > span.l-btn-text').click()


#登录管理员审批任务
driver.implicitly_wait(10)
login = noturl(driver)
login.nourl_all_actions('newadmin','newadmin')
#进入审批管理
driver.find_elements_by_class_name('panel-with-icon')[2].click()
driver.find_element_by_css_selector('#nav > div:nth-child(3) > div.panel-body.accordion-body > ul > li:nth-child(3) > div > a > span.nav').click()
driver.find_elements_by_class_name('tabs-close')[0].click()
adminiframe = driver.find_element_by_tag_name('iframe')
driver.switch_to.frame(adminiframe)
#任务审批通过
driver.find_element_by_css_selector('#datagrid-row-r1-2-0 > td:nth-child(15) > div > a:nth-child(1) > span > span.l-btn-text').click()
driver.find_element_by_css_selector('body > div.panel.window.messager-window > div.messager-body.panel-body.panel-body-noborder.window-body > div.messager-button > a:nth-child(1) > span > span').click()
time.sleep(2)
#退出登录
driver.switch_to.default_content()
driver.find_element_by_css_selector('#indexLayout > div.panel.layout-panel.layout-panel-north > div > div > a:nth-child(2) > span > span.l-btn-text').click()


#登录回普通用户确认任务状态
driver.implicitly_wait(10)
login = noturl(driver)
login.nourl_all_actions('automation','Automation')
#进入普通用户任务管理
driver.find_elements_by_class_name('panel-with-icon')[3].click()
driver.find_element_by_xpath('//*[@id="nav"]/div[4]/div[2]/ul/li[2]/div/a/span[2]').click()
time.sleep(2)
driver.find_elements_by_class_name('tabs-close')[0].click()
driver.switch_to.frame(driver.find_element_by_tag_name('iframe'))
line1 = driver.find_element_by_css_selector('#datagrid-row-r1-2-0 > td:nth-child(16) > div > a > span > span.l-btn-text').text
line2 = driver.find_element_by_css_selector('#datagrid-row-r1-2-1 > td:nth-child(16) > div > a > span > span.l-btn-text').text
# print(line1)
# print(line2)
time.sleep(1)
if u'结束' == line1 or line2:
    print(u'管理员审批通过，等待下发！')
else:
    print(u'任务创建失败')
time.sleep(3)
driver.quit()