import util.shibie
import testtime
class login_go():
    def __init__(self,driver):
        self.driver = driver

    def open_url(self,url):
        self.driver.get(url)
        testtime.sleep(2)
        self.driver.maximize_window()

    def login(self,loginname,password):
        self.driver.find_element_by_name("loginname").send_keys(loginname)
        self.driver.find_element_by_name("password").send_keys(password)
        code = util.shibie.WebUntil().verfyCode(self.driver,ID="codeImg")
        self.driver.find_element_by_id('code').send_keys(code)
        testtime.sleep(2)
        while True:
            if 'Index' in self.driver.current_url:
                print('成功登陆')
                break
                testtime.sleep(2)
            elif len(code) > 4:
                print('验证码大于4位,再次识别')
                self.driver.find_element_by_id('code').clear()
                self.driver.find_element_by_id('codeImg').click()
                code = shibie.WebUntil().verfyCode(self.driver,ID="codeImg")
                self.driver.find_element_by_id('code').send_keys(code)
            else:
                print('验证码错误，即将重新识别')
                self.driver.find_element_by_id('code').clear()
                self.driver.find_element_by_id('codeImg').click()
                code = shibie.WebUntil().verfyCode(self.driver,ID="codeImg")
                self.driver.find_element_by_id('code').send_keys(code)

    def all_actions(self,url,loginname,password):
        self.open_url(url)
        self.login(loginname,password)


class noturl():
    def __init__(self,driver):
        self.driver = driver

    def login(self,loginname,password):
        self.driver.find_element_by_name("loginname").send_keys(loginname)
        self.driver.find_element_by_name("password").send_keys(password)
        code = util.shibie.WebUntil().verfyCode(self.driver,ID="codeImg")
        self.driver.find_element_by_id('code').send_keys(code)
        testtime.sleep(2)
        while True:
            if 'Index' in self.driver.current_url:
                print('成功登陆')
                break
            elif len(code) > 4:
                print('验证码大于4位,再次识别')
                self.driver.find_element_by_id('code').clear()
                self.driver.find_element_by_id('codeImg').click()
                code = util.shibie.WebUntil().verfyCode(self.driver,ID="codeImg")
                self.driver.find_element_by_id('code').send_keys(code)
            else:
                print('验证码错误，即将重新识别')
                self.driver.find_element_by_id('code').clear()
                self.driver.find_element_by_id('codeImg').click()
                code = util.shibie.WebUntil().verfyCode(self.driver,ID="codeImg")
                self.driver.find_element_by_id('code').send_keys(code)