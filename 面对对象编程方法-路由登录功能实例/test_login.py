#coding:utf-8
#用例层代码，调用login_business函数
__author__ = 'yinxia'
import unittest,time
from selenium import webdriver
from login_business import LoginBusiness

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver = webdriver.Firefox()
        self.driver.get('http://192.168.11.1')
        self.driver.implicitly_wait(10)

    def test01(self):
        username='100msh'
        password='password'
        LoginBusiness1 = LoginBusiness(self.driver)#调用逻辑类方法
        LoginBusiness1.login01(username,password)
        time.sleep(2)
        assert u"总览" in self.driver.title ,u"输入正确的用户名登录失败"

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
