#coding=utf-8
#作者：曾祥卫
#时间：2016.10.31
#描述：淘宝页面的控制层类,包括登陆的页面元素的获取和设置，其继承子类publicControl功能
#包括：用户名，密码，登录，购物车，收藏夹，已买到的宝贝等按钮

############################################
#xpath淘宝节点路径
#淘宝网首页
node_Twp = ".//*[@id='J_SiteNavHome']"
#我的淘宝
node_Mt = ".//*[@id='J_SiteNavMytaobao']"
#购物车
node_Sc = ".//*[@id='mc-menu-hd']"
#收藏夹
node_Fav = ".//*[@id='J_SiteNavFavor']"
#商品分类
node_Cc = ".//*[@id='J_SiteNavCatalog']"
############################################


from public.public_control import PublicControl

class TaobaoControl(PublicControl):
    def __init__(self,driver,username=None,password=None):
        #继承PublicControl类的属性和方法
        PublicControl.__init__(self,driver)
        #自己TaobaoControl类的属性，username:登录用户名，password：登录密码
        self.username = username
        self.password =password

    #点击PC密码登录
    def PC_submit(self):
        try:
            #通过id元素定位
            #PC_submit_element = self.driver.find_element_by_id('J_Quick2Static')
            #或者通过link text元素
            PC_submit_element = self.driver.find_element_by_link_text(u"密码登录")
            PC_submit_element.click()
            self.driver.implicitly_wait(20)
        except Exception as e:
            raise Exception("page has not found 'PC_submit' element! The reason is %s"%e)

    #输入用户名
    def set_username(self):
        try:
            username_element = self.driver.find_element_by_id('TPL_username_1')
            username_element.clear()
            username_element.send_keys(self.username)
        except Exception as e:
            raise Exception("Login page set 'username' element is error! The reason is %s"%e)

    #设置密码
    def set_password(self):
        try:
            password_element = self.driver.find_element_by_id('TPL_password_1')
            password_element.clear()
            password_element.send_keys(self.password)
        except Exception as e:
            raise Exception("Login page set 'password' element is error! The reason is %s "%e)

    #点击登录
    def SubmitStatic(self):
        try:
            Submit_element = self.driver.find_element_by_id('J_SubmitStatic')
            Submit_element.click()
            self.driver.implicitly_wait(20)
        except Exception as e:
            raise Exception("Login page set 'SubmitStatic' element is error! The reason is %s "%e)


    #点击淘宝网首页
    def Taobao_web_page(self):
        #PublicControl.menu1(self,".//*[@id='J_SiteNavHome']/div/a/span")
        PublicControl.menu1(self,"%s/div/a/span"%node_Twp)

    #点击我的淘宝
    def My_taobao(self):
        #PublicControl.menu1(self,".//*[@id='J_SiteNavMytaobao']/div[1]/a/span")
        PublicControl.menu1(self,"%s/div[1]/a/span"%node_Mt)

    #点击购物车
    def Shopping_Cart(self):
        PublicControl.menu1(self,"%s/span[2]"%node_Sc)

    #点击收藏夹
    def Favorites(self):
        PublicControl.menu1(self,"%s/div[1]/a/span[2]"%node_Fav)

    #点击商品分类
    def Commodity_classification(self):
        PublicControl.menu1(self,"%s/div/a/span"%node_Cc)

    #点击我的淘宝-已购买的宝贝
    def Already_bought_baby(self):
        PublicControl.menu2(self,"%s/div[1]/a/span"%node_Mt,"%s/div[2]/div/a[1]"%node_Mt)

    #点击收藏夹-收藏的宝贝
    def Collection_of_baby(self):
        PublicControl.menu2(self,"%s/div[1]/a/span[2]"%node_Fav,"%s/div[2]/div/a[1]"%node_Fav)

    #点击收藏夹-收藏的店铺
    def Collection_of_shops(self):
        PublicControl.menu2(self,"%s/div[1]/a/span[2]"%node_Fav,"%s/div[2]/div/a[2]"%node_Fav)


    #收藏夹内搜索输入框内输入关键词
    def Search_Favorites(self,keyword):
         try:
            Search_element = self.driver.find_element_by_id('fav-q')
            Search_element.clear()
            Search_element.send_keys(keyword)
         except Exception as e:
            raise Exception("Favorites page set 'Search' element is error! The reason is %s"%e)

    #收藏夹内点击搜店铺
    def Submit_Collection_of_shops(self):
         try:
            Submit_element = self.driver.find_element_by_class_name("fav-btn-search-s")
            Submit_element.click()
            self.driver.implicitly_wait(20)
         except Exception as e:
            raise Exception("Favorites page set 'Submit_Collection_of_shops' element is error! The reason is %s"%e)

    #收藏夹内点击店铺名
    def click_shop(self):
         try:
            click_element = self.driver.find_element_by_class_name("shop-name-link")
            click_element.click()
            self.driver.implicitly_wait(20)
         except Exception as e:
            raise Exception("Favorites page set 'click shop' element is error! The reason is %s"%e)


'''

    #点击登录
    def submit(self):
        try:
            submit_element = self.driver.find_element_by_class_name('btn-login ml1')
            submit_element.click()
            self.driver.implicitly_wait(10)
        except Exception as e:
            raise Exception("page has not found 'submit' element! The reason is %s"%e)

    #点击注册
    def register(self):
        try:
            register_element = self.driver.find_element_by_class_name('ml2')
            register_element.click()
            self.driver.implicitly_wait(10)
        except Exception as e:
            raise Exception("page has not found 'register' element! The reason is %s"%e)

    #点击开店
    def shop(self):
        try:
            shop_element = self.driver.find_element_by_class_name('ml3')
            shop_element.click()
            self.driver.implicitly_wait(10)
        except Exception as e:
            raise Exception("page has not found 'shop' element! The reason is %s"%e)











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

'''
__author__ = 'zeng'
