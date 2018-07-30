#coding:utf-8
#作者：尹霞
#描述：登陆控制层代码，包括登陆的页面元素的获取和设置，其继承子类publicControl功能

from public_control import PublicControl
class LoginControl(PublicControl):
    def __init__(self,driver,username=None,password=None):
        PublicControl.__init__(self,driver)
        self.username = username
        self.password =password
    #获取用户名
    def get_username(self):
        try:
            username_element = self.driver.find_element_by_name('username')
            return username_element.text
        except Exception as e:
            raise Exception("Login page has not 'username' element! The reason is %s"%e)
    #获取密码
    def get_paasword(self):
        try:
            password_element = self.driver.find_element_by_name('password')
            return password_element.text
        except Exception as e:
            raise Exception("Login page has not 'password' element! The reason is %s "%e)
    #设置用户名
    def set_username(self):
        try:
            username_element = self.driver.find_element_by_name('username')
            username_element.clear()
            username_element.send_keys(self.username)
        except Exception as e:
            raise Exception("Login page set 'username' element is error! The reason is %s"%e)
    #设置密码
    def set_password(self):
        try:
            password_element = self.driver.find_element_by_name('password')
            password_element.clear()
            password_element.send_keys(self.password)
        except Exception as e:
            raise Exception("Login page set 'password' element is error! The reason is %s "%e)

    #登陆失败的错误提示信息
    def error(self):
        try:
            error_element = self.driver.find_element_by_class_name('error')
            return True
        except Exception as e:
            raise Exception("Login page has not login error information! The reason is %s "%e)

    #描述：实现管理界面的退出出
    def logout(self):
        try:
            self.driver.find_element_by_link_text(u'退出').click()
        except (Exception) as e:
            raise Exception("exit the system is error,The reason is ：%s" %str(e))


