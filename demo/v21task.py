# coding=utf-8
import time
from selenium import webdriver
import shibie
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://web.zzx9.cn")
# driver.get("http://v21_web.cnklog.com/")
driver.implicitly_wait(10)
#普通用户登录
driver.find_element_by_name("username").send_keys("automation")
driver.find_element_by_name("password1").send_keys("Automation")
#识别验证码
rand = shibie.WebUntil().verfyCode(driver,ID="randImage")
driver.find_element_by_id('rand').send_keys(rand)
time.sleep(2)
while True:
    if 'Index' in driver.current_url:
        print('普通用户>>成功登陆')
        break
    elif len(rand) > 4:
        print('普通用户>>验证码大于4位,再次识别')
        driver.find_element_by_id('rand').clear()
        driver.find_element_by_id('randImage').click()
        rand = shibie.WebUntil().verfyCode(driver,ID="randImage")
        driver.find_element_by_id('rand').send_keys(rand)
    else:
        print('普通用户>>验证码错误，即将重新识别')
        driver.find_element_by_id('rand').clear()
        driver.find_element_by_id('randImage').click()
        rand = shibie.WebUntil().verfyCode(driver,ID="randImage")
        driver.find_element_by_id('rand').send_keys(rand)
#点击任务管理
driver.find_elements_by_class_name('panel-with-icon')[3].click()
driver.find_element_by_xpath('//*[@id="nav"]/div[4]/div[2]/ul/li[2]/div/a/span[2]').click()
time.sleep(2)
driver.find_elements_by_class_name('tabs-close')[0].click()
driver.switch_to.frame(driver.find_element_by_tag_name('iframe'))
#添加任务
driver.find_elements_by_class_name('l-btn-icon-left')[2].click()
driver.find_element_by_xpath('//*[@id="addftask"]/div[1]/input').send_keys('线下自动化测试任务下发')
driver.find_element_by_css_selector('#upmmsId').send_keys('867986')
driver.find_element_by_css_selector('#d1').click()
driver.switch_to.default_content()
driver.switch_to.frame(1)
#选择下发时间
driver.find_element_by_css_selector('#dpTime > table > tbody > tr:nth-child(1) > td:nth-child(1) > input:nth-child(4)').click()
driver.find_element_by_css_selector('#dpTimeUp').click()#点击一次为5分钟后下发
# driver.find_element_by_css_selector('#dpTimeUp').click()#点击两次为10分钟后下发
driver.find_element_by_css_selector('#dpOkInput').click()
#此处选择完日期需要切换回首页iframe然后切到任务iframe
driver.switch_to.default_content()
driver.switch_to.frame(driver.find_element_by_tag_name('iframe'))
driver.find_element_by_xpath('//*[@id="addftask"]/div[5]/span/span/a').click()
time.sleep(2)
driver.find_element_by_css_selector('#_easyui_tree_1 > span.tree-title').click()
driver.find_element_by_css_selector('#addftask > div:nth-child(8) > textarea').send_keys(u'自动化测试')
driver.find_element_by_xpath('//*[@id="addftask"]/div[5]/span/span/a').click()
# driver.find_element_by_css_selector('#addtask').click()
driver.find_element_by_css_selector('#dlg-buttons > a:nth-child(1) > span > span.l-btn-text').click()
#提交任务
driver.switch_to.default_content()
driver.find_element_by_xpath('//*[@id="nav"]/div[4]/div[2]/ul/li[2]/div/a/span[2]').click()
time.sleep(3)
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
driver.find_element_by_name("username").send_keys('newadmin')
driver.find_element_by_name("password1").send_keys("newadmin")
#识别验证码
rand = shibie.WebUntil().verfyCode(driver,ID="randImage")
driver.find_element_by_id('rand').send_keys(rand)
time.sleep(2)
while True:
    if 'Index' in driver.current_url:
        print('管理员>>成功登陆')
        break
    elif len(rand) > 4:
        print('管理员>>验证码大于4位,再次识别')
        driver.find_element_by_id('rand').clear()
        driver.find_element_by_id('randImage').click()
        rand = shibie.WebUntil().verfyCode(driver,ID="randImage")
        driver.find_element_by_id('rand').send_keys(rand)
    else:
        print('管理员>>验证码错误，即将重新识别')
        driver.find_element_by_id('rand').clear()
        driver.find_element_by_id('randImage').click()
        rand = shibie.WebUntil().verfyCode(driver,ID="randImage")
        driver.find_element_by_id('rand').send_keys(rand)
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
driver.find_element_by_name("username").send_keys("automation")
driver.find_element_by_name("password1").send_keys("Automation")
#识别验证码
rand = shibie.WebUntil().verfyCode(driver,ID="randImage")
driver.find_element_by_id('rand').send_keys(rand)
time.sleep(2)
while True:
    if 'Index' in driver.current_url:
        print('普通用户>>成功登陆')
        break
    elif len(rand) > 4:
        print('普通用户>>验证码大于4位,再次识别')
        driver.find_element_by_id('rand').clear()
        driver.find_element_by_id('randImage').click()
        rand = shibie.WebUntil().verfyCode(driver,ID="randImage")
        driver.find_element_by_id('rand').send_keys(rand)
    else:
        print('普通用户>>验证码错误，即将重新识别')
        driver.find_element_by_id('rand').clear()
        driver.find_element_by_id('randImage').click()
        rand = shibie.WebUntil().verfyCode(driver,ID="randImage")
        driver.find_element_by_id('rand').send_keys(rand)
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