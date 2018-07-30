#coding:utf-8
#描述：公用控制层代码，包括页面共有元素的获取和设置，可是为基础类
#作者：曾祥卫
#时间：2016.10.31

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import uuid,os,commands,random
import subprocess,time,pexpect
import locale

class PublicControl:
    def __init__(self,driver):
        self.driver = driver


    #描述:进入系统一级菜单
    #输入:xpath1:一级菜单
    #输出:None
    def menu1(self,xpath1):
        self.driver.implicitly_wait(10)
        try:
            #定位一级菜单
            first = self.driver.find_element_by_xpath(xpath1)
            #找到一级菜单，并点击
            first.click()
        except Exception as e:
            print "The page redirect fail,the reason is ：%s" %e

    #描述:进入系统二级菜单
    #输入:xpath1:一级菜单，xpath2：二级菜单
    #输出:None
    def menu2(self,xpath1,xpath2):
        self.driver.implicitly_wait(10)
        try:
            #定位一级菜单
            first = self.driver.find_element_by_xpath(xpath1)
            #移动鼠标到一级菜单上
            ActionChains(self.driver).move_to_element(first).perform()
            #找到二级菜单，并点击
            self.driver.find_element_by_xpath(xpath2).click()
        except Exception as e:
            print "The page redirect fail,the reason is ：%s" %e






'''
#描述:进入系统二级菜单
#输入:self
#输出:None
def menu(self,link1,link2):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        first = driver.find_element_by_link_text(link1)
        ActionChains(driver).move_to_element(first).perform()
        driver.find_element_by_link_text(link2).click()
    except (NoSuchElementException,Exception) as e:
        reboot_router()
        print u"页面跳转到%s-%s失败,原因如下：%s" %link1,link2,e


#描述:点击页面的保存&应用
#输入:self
#输出:None
def apply(self):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        apply = driver.find_element_by_name("cbi.apply")
        apply.click()
    except (NoSuchElementException,Exception) as e:
        print u"点击“保存&应用”失败,原因如下：%s" %str(e)
		

#描述:点击复位按钮
#输入:self
#输出:None
def reset(self):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        reset = driver.find_element_by_class_name('cbi-button-reset')
        reset.click()
    except (NoSuchElementException,Exception) as e:
        print u"点击“复位”失败,原因如下：%s" %str(e)

#描述:获取本地mac地址
#输入:
#输出:mac-字符串类型，本地mac
def get_localmac():
    try:
        tmp = uuid.UUID(int=uuid.getnode()).hex[-12:]
        mac = ":".join([tmp[e:e+2] for e in range(0,11,2)])
        return mac
    except Exception,e:
        print u"获取本机mac地址失败。原因如下：%s"%e

#描述：获取本地IP
#作者：孔志兵
#输出：本机的IP地址
def get_localIp():
    try:
        language = locale.getdefaultlocale()#获取系统语言
        result = subprocess.check_output('ifconfig eth0',shell=True)
        result = result.split('\n')
        if 'en_US' in language:
            ip =  (result[1].strip('inet addr:'))[0:14]
        else:
            ip =  (result[1].strip('inet 地址:'))[0:14]
        return ip
    except Exception,e:
        print u'获取本机IP地址失败，原因如下:%s' %e

#描述:ping IP地址
#作者：孔志兵
#输入:str-ip地址或域名
#输出:ping结果1-真，反之
def get_ping(str):

    try:
        ping = "ping %s -c 4"%str
        result = os.system(ping)
        return result
    except Exception,e:
        print u"ping命令执行失败。原因如下：%s"%e

#描述:该函数用以在后台判断某个进程在不在
#作者：孔志兵
#输入:某个进程
#输出:True-存在，反之
def telnet_ps(process):
    try:
        i =0
        while(i<5):
            result = telnet.telnet_cmd4("ps")
            if process in result:
                return True
            time.sleep(20)
            i+=1
        return False
    except Exception,e:
        raise Exception( u"从telnet获取%s进程信息失败，原因如下：%s" %process %e)

#描述：Client端在终端输入命令,命令结果返回给函数
#输入：self,cmd-client在终端输入的命令
#输出：output-在终端显示的结果
def client_cmd(cmd):
    try:
        #Client端在终端输入命令,命令结果返回给函数
        status,output = commands.getstatusoutput(cmd)
        return output
    #捕捉异常并打印异常信息
    except Exception,e:
        raise Exception( u"Client端在终端输入命令失败，原因如下：\n%s"%e)

#描述：新建或打开文件，并写入内容
#输入：filename-文件名(也可以是文件的路径),写入的内容,content-写入的内容
#输出：无
def modify_file(filename,content):
    #文件filename没有存在则新建文件，如果存在则会首先清空然后写入
    file = open(filename,'w')
    try:
        #把内容content写入文件filename
        file.writelines(content)
    finally:
        #关闭文件
        file.close()

#描述：打开文件，修改文件的第几行内容
#输入：filename-文件名,写入的内容,row-第几行，content-写入的内容
#输出：无
def modify_file2(filename,row,content):
    try:
        #打开文件内容，转换为列表
        file = open(filename)
        a = file.readlines()
        file.close()
        #修改列表对应序列的内容
        a[row-1] = content
        #再把列表写进文件中
        file = open(filename,'w')
        file.writelines(a)
        file.close()
    #捕捉异常并打印异常信息
    except Exception,e:
        raise Exception( u"修改文件内容失败，原因如下：\n%s"%e)



#描述：禁用网卡,然后再启用网卡
#输入：self
#输出：None
def networkcard_disable_enable():
    try:
        password = data.data_basic()
        #禁用eth0网卡
        down = pexpect.spawn('sudo ifconfig eth0 down')
        down.expect(':')
        down.sendline(password['hostpwd'])
        time.sleep(15)

        #启用eth0网卡
        up = pexpect.spawn('sudo ifconfig eth0 up')
        up.expect(':')
        up.sendline(password['hostpwd'])
        time.sleep(15)
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"禁用网卡,然后再启用网卡失败，原因如下：\n%s"%e

#描述：通过telnet登录路由后台,输入reboot重启路由,并等待60s
#输入：self
#输出：None
def reboot_router():
    try:
        #在路由器中输入reboot
        telnet.telnet_cmd4('reboot')
        time.sleep(60)
        networkcard_disable_enable()
    #捕捉异常并打印异常信息
    except Exception,e:
        raise Exception( u"reboot重启路由失败，原因如下：\n%s"%e)
				
		
		
#描述：禁用无线网卡,然后再启用无线网卡
#输入：self
#输出：None
def wlan_disable_enable(wlan):
    try:
        password = data.data_basic()
        #禁用无线网卡
        down = pexpect.spawn('sudo ifconfig %s down'%wlan)
        down.expect(':')
        down.sendline(password['hostpwd'])
        time.sleep(15)

        #启用无线网卡
        up = pexpect.spawn('sudo ifconfig %s up'%wlan)
        up.expect(':')
        up.sendline(password['hostpwd'])
        time.sleep(15)
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"禁用无线网卡,然后再启用无线网卡失败，原因如下：\n%s"%e

#取随机mac
def randomMAC():
    mac = [ 0x00, 0x0c,
        random.randint(0x00, 0x7f),
        random.randint(0x00, 0x7f),
        random.randint(0x00, 0xff),
        random.randint(0x00, 0xff) ]
    return ':'.join(map(lambda x: "%02x" % x, mac))

#取随机ip地址
def randomip():
    a = random.randint(1,254)
    b = random.randint(1,254)
    c = random.randint(1,254)
    d = random.randint(1,254)
    ip = '%s.%s.%s.%s'%(a,b,c,d)
    return ip


'''
