#coding:utf-8
#作者：曾祥卫
#时间：2016.10.31
#用例层代码，调用taobao_business函数

import unittest,time
from selenium import webdriver
from taobao_bussiness import TaobaoBusiness
from data_zeng import data

taobao_data = data.data_taobao()

class TestTaobao(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get(taobao_data['address'])
        self.driver.implicitly_wait(10)
    #
    # #首先登录淘宝
    # def test_login(self):
    #     #逻辑类对象，建一个实例
    #     TaobaoBusiness1 = TaobaoBusiness(self.driver)
    #     #调用实例的登录淘宝的方法
    #     TaobaoBusiness1.login(taobao_data['username'],taobao_data['password'])
    #     assert u"我的淘宝" in self.driver.title ,u"登录失败"
    #     print u"登录淘宝成功"
    #
    # #
    # ############以下为进入一级菜单的方法#############
    # #
    #
    # #打开我的淘宝
    # def test_My_taobao(self):
    #     #逻辑类对象，建一个实例
    #     TaobaoBusiness1 = TaobaoBusiness(self.driver)
    #     #调用实例的登录淘宝的方法
    #     TaobaoBusiness1.login(taobao_data['username'],taobao_data['password'])
    #     #点击我的淘宝
    #     TaobaoBusiness1.My_taobao()
    #     assert u"我的淘宝" in self.driver.title ,u"进入我的淘宝失败"
    #     print u"进入我的淘宝成功"
    #
    # #打开购物车
    # def test_Shopping_Cart(self):
    #     #逻辑类对象，建一个实例
    #     TaobaoBusiness1 = TaobaoBusiness(self.driver)
    #     #调用实例的登录淘宝的方法
    #     TaobaoBusiness1.login(taobao_data['username'],taobao_data['password'])
    #     #点击购物车
    #     TaobaoBusiness1.Shopping_Cart()
    #     assert u"购物车" in self.driver.title ,u"进入我的购物车失败"
    #     print u"进入我的购物车成功"
    #
    # #打开收藏夹
    # def test_Favorites(self):
    #     #逻辑类对象，建一个实例
    #     TaobaoBusiness1 = TaobaoBusiness(self.driver)
    #     #调用实例的登录淘宝的方法
    #     TaobaoBusiness1.login(taobao_data['username'],taobao_data['password'])
    #     #点击收藏夹
    #     TaobaoBusiness1.Favorites()
    #     assert u"收藏夹" in self.driver.title ,u"进入我的收藏夹失败"
    #     print u"进入我的收藏夹成功"
    #
    # #打开商品分类
    # def test_Commodity_classification(self):
    #     #逻辑类对象，建一个实例
    #     TaobaoBusiness1 = TaobaoBusiness(self.driver)
    #     #调用实例的登录淘宝的方法
    #     TaobaoBusiness1.login(taobao_data['username'],taobao_data['password'])
    #     #点击商品分类
    #     TaobaoBusiness1.Commodity_classification()
    #     assert u"行业市场" in self.driver.title ,u"进入商品分类失败"
    #     print u"进入商品分类成功"
    #
    # #
    # ############以下为进入二级菜单的方法#############
    # #
    #
    # #打开已购买的宝贝
    # def test_Already_bought_baby(self):
    #     #逻辑类对象，建一个实例
    #     TaobaoBusiness1 = TaobaoBusiness(self.driver)
    #     #调用实例的登录淘宝的方法
    #     TaobaoBusiness1.login(taobao_data['username'],taobao_data['password'])
    #     #点击我的淘宝-已购买的宝贝
    #     TaobaoBusiness1.Already_bought_baby()
    #     assert u"已买到的宝贝" in self.driver.title ,u"进入已买到的宝贝失败"
    #     print u"进入已买到的宝贝成功"
    #
    # #打开收藏的宝贝
    # def test_Collection_of_baby(self):
    #     #逻辑类对象，建一个实例
    #     TaobaoBusiness1 = TaobaoBusiness(self.driver)
    #     #调用实例的登录淘宝的方法
    #     TaobaoBusiness1.login(taobao_data['username'],taobao_data['password'])
    #     #点击收藏夹-收藏的宝贝
    #     TaobaoBusiness1.Collection_of_baby()
    #     assert u"收藏夹" in self.driver.title ,u"进入收藏的宝贝失败"
    #     print u"进入收藏的宝贝成功"
    #
    # #打开收藏的店铺
    # def test_Collection_of_shops(self):
    #     #逻辑类对象，建一个实例
    #     TaobaoBusiness1 = TaobaoBusiness(self.driver)
    #     #调用实例的登录淘宝的方法
    #     TaobaoBusiness1.login(taobao_data['username'],taobao_data['password'])
    #     #点击收藏夹-收藏的店铺
    #     TaobaoBusiness1.Collection_of_shops()
    #     assert u"收藏夹" in self.driver.title ,u"进入收藏的店铺失败"
    #     print u"进入收藏的店铺成功"



    #进入收藏的某个店铺
    def test_goin_Collection_of_shop(self):
        #逻辑类对象，建一个实例
        TaobaoBusiness1 = TaobaoBusiness(self.driver)
        #调用实例的登录淘宝的方法
        TaobaoBusiness1.login(taobao_data['username'],taobao_data['password'])
        result = TaobaoBusiness1.goin_Collection_of_shop(taobao_data['shopname'])
        assert taobao_data['shopname'] in result ,u"进入收藏的店铺:%s失败"%taobao_data['shopname']
        print u"进入收藏的店铺:%s成功"%taobao_data['shopname']


    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
