import util.shibie
import time
class login_go():
    def __init__(self,driver):
        self.driver = driver

    def open_url(self,url):
        self.driver.get(url)
        time.sleep(2)
        self.driver.maximize_window()

    def login(self,username,password):
        self.driver.find_element_by_name("username").send_keys(username)
        self.driver.find_element_by_name("password1").send_keys(password)
        while True:
            ## 长度大于4重新来
            self.driver.find_element_by_id('randImage').click()
            rand = util.shibie.WebUntil().verfyCode(self.driver,ID="randImage")
            # print(len(rand))
            if len(rand) > 6 or len(rand) == 0:
                continue
            if ' ' in rand:
                continue
    ## 清空验证码，输入验证码
            self.driver.find_element_by_id('rand').clear()
            self.driver.find_element_by_id('rand').send_keys(rand)
            time.sleep(3)
            if 'Index' in self.driver.current_url:
                print('成功登陆')
                break
    ## 处理验证码错误
            else:
                print('验证码错误，即将重新识别')
                self.driver.find_element_by_xpath('html/body/div[4]/div[1]/a').click()#关闭验证码错误弹窗
                self.driver.find_element_by_name("username").send_keys(username)
                self.driver.find_element_by_name("password1").send_keys(password)

    def all_actions(self,url,username,password):
        self.open_url(url)
        self.login(username,password)


class noturl():
    def __init__(self,driver):
        self.driver = driver

    def login(self,username,password):
        self.driver.find_element_by_name("username").send_keys(username)
        self.driver.find_element_by_name("password1").send_keys(password)
        while True:
    ## 长度大于4重新来
            self.driver.find_element_by_id('randImage').click()
            rand = util.shibie.WebUntil().verfyCode(self.driver,ID="randImage")
            # print(len(rand))
            if len(rand) > 6 or len(rand) == 0:
                continue
            if ' ' in rand:
                continue
            ## 清空验证码，输入验证码
            self.driver.find_element_by_id('rand').clear()
            self.driver.find_element_by_id('rand').send_keys(rand)
            time.sleep(3)
            if 'Index' in self.driver.current_url:
                print('成功登陆')
                break
    ## 处理验证码错误
            else:
                print('验证码错误，即将重新识别')
                self.driver.find_element_by_xpath('html/body/div[4]/div[1]/a').click()#关闭验证码错误弹窗
                self.driver.find_element_by_name("username").send_keys(username)
                self.driver.find_element_by_name("password1").send_keys(password)

    def nourl_all_actions(self,username,password):
        self.login(username,password)