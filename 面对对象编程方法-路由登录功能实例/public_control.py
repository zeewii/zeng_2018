#coding:utf-8
#作者：尹霞
#描述：公用控制层代码，包括页面共有元素的获取和设置，可是为基础类
class PublicControl:
    def __init__(self,driver):
        self.driver = driver

    def apply(self):
        try:
            apply_element = self.driver.find_element_by_class_name('cbi-button-apply')
            apply_element.click()
            self.driver.implicitly_wait(10)
        except Exception as e:
            raise Exception("it hasn't apply button. The reason is %s"%e)

    def reset(self):
        try:
            reset_element = self.driver.find_element_by_class_name('cbi-button-reset')
            reset_element.click()
            self.driver.implicitly_wait(10)
        except Exception as e:
            raise Exception("it hasn't apply button. The reason is %s"%e)