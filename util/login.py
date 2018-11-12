# coding=utf-8
from selenium import webdriver
import util.shibie
import time
driver = webdriver.Chrome()
driver.get('http://web.zzx9.cn')
driver.maximize_window()
driver.find_element_by_name("username").send_keys('putong')
driver.find_element_by_name("password1").send_keys('putong')
while True:
    ## 长度大于4重新来
    driver.find_element_by_id('randImage').click()
    rand = util.shibie.WebUntil().verfyCode(driver,ID="randImage")
    # print(len(rand))
    if len(rand) > 6 or len(rand) == 0:
        continue
    if ' ' in rand:
        continue
    ## 清空验证码，输入验证码
    driver.find_element_by_id('rand').clear()
    driver.find_element_by_id('rand').send_keys(rand)
    time.sleep(3)
    if 'Index' in driver.current_url:
        print('成功登陆')
        break
    ## 处理验证码错误
    else:
        print('验证码错误，即将重新识别')
        time.sleep(2)
        driver.find_element_by_xpath('html/body/div[4]/div[1]/a').click()#关闭验证码错误弹窗
        driver.find_element_by_name("username").send_keys('putong')
        driver.find_element_by_name("password1").send_keys('putong')