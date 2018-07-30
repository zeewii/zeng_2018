#coding=utf-8
#作者：曾祥卫
#时间：2016.10.31
#描述：淘宝页面的业务层类，包括想对应的业务操作

from taobao_control import TaobaoControl
import time


class TaobaoBusiness(TaobaoControl):
    def __init__(self,driver):
        #继承TaobaoControl类的属性和方法
        TaobaoControl.__init__(self,driver)
        self.driver = driver

    #登录淘宝
    def login(self,username,password):
        #通过控制层对象TaobaoControl建一个实例,并指定该实例的属性：username,password
        LoginControl = TaobaoControl(self.driver,username,password)
        #点击PC密码登录
        LoginControl.PC_submit()
        #输入用户名
        LoginControl.set_username()
        #设置密码
        LoginControl.set_password()
        #点击登录
        LoginControl.SubmitStatic()

    #进入收藏的某个店铺
    def goin_Collection_of_shop(self,shopname):
        #点击收藏夹-收藏的店铺----继承TaobaoControl类的方法
        TaobaoControl.Collection_of_shops(self)
        #获得当前页面的句柄
        nowhandle = self.driver.current_window_handle
        #收藏夹内搜索输入框内输入关键词----继承TaobaoControl类的方法
        TaobaoControl.Search_Favorites(self,shopname)
        #收藏夹内点击搜店铺----继承TaobaoControl类的方法
        TaobaoControl.Submit_Collection_of_shops(self)
        #收藏夹内点击店铺名
        TaobaoControl.click_shop(self)
        #time.sleep(30)
        #获得页面的句柄
        allhandle = self.driver.window_handles
        for handle in allhandle:
            #如果句柄不等于先前页面的句柄，则切换到当前页面
            if handle != nowhandle:
                self.driver.switch_to_window(handle)
                self.driver.maximize_window()
                #返回当前页面的标题
                return self.driver.title














__author__ = 'zeng'
