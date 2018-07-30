#coding:utf-8
# __author__ = 'yinxia'
from login_control import LoginControl

class LoginBusiness():
    def __init__(self,driver):
        self.driver = driver

    def login01(self,user,pwd):
        LoginControl1 = LoginControl(self.driver,user,pwd)
        LoginControl1.set_username()
        LoginControl1.set_password()
        LoginControl1.apply()
