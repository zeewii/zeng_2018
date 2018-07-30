#coding:utf-8
#描述：本模块是测试路由器H351修改配置后重启丢配置的问题是设计的自动化脚本
#作者：曾祥卫

import unittest
import time

from selenium import webdriver

from public import public
from network.wifidog import wifidog_business,general_control
from login import login_control
from data import data


class TestReboot(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        #将浏览器最大化
        self.driver.maximize_window()


    def test(self):
        i = 0
        while True:
            ping = public.get_ping('192.168.11.1')
            #如果能够ping通路由，则表示未失败
            if ping == 0:
                #打开reboot.txt文件，写入pass
                f = open('reboot.txt','a')
                f.writelines('第%d次测试pass\n'%i)
                f.close()
                D = data.default_web_user_password()
                try:
                    #打开路由页面，确认路由页面是否能显示
                    self.driver.get('http://%s:8088'%D[0])
                    time.sleep(5)
                    self.driver.find_element_by_name('username')
                except:
                    #不能显示路由页面，则登录ssh重启路由
                    wifidog_business.reboot(self)
                finally:
                    #登录路由页面
                    self.driver.get('http://%s:8088'%D[0])
                    login_control.set_user(self,D[1],D[2])
                    login_control.submit(self)
                    time.sleep(3)
                    #进入门户认证，修改网关ID
                    general_control.wifidog_menu(self)
                    general_control.set_rand_gatewayId(self)
                    general_control.apply(self)
                    time.sleep(60)
                    #再次重启路由
                    wifidog_business.reboot(self)
            #不能ping通则打开reboot.txt文件写入fail，退出循环
            else:
                f = open('reboot.txt','a')
                f.writelines('第%d次测试fail\n'%i)
                f.closed()
                break
            i +=1

    #退出清理工作
    def tearDown(self):
        self.driver.quit()

if __name__=='__main__':
    unittest.main()
