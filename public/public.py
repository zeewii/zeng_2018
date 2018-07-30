#coding:utf-8
#描述：存放公共函数
#作者：曾祥卫
import uuid
import os
import commands
import random

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

#描述:ping
#输入:str-ip地址或域名
#输出:ping结果1-真，反之
def get_ping(str):

    try:
        ping = "ping %s -c 4"%str
        result = os.system(ping)
        return result
    except Exception,e:
        print u"ping命令执行失败。原因如下：%s"%e

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
        print u"Client端在终端输入命令失败，原因如下：\n%s"%e

#描述：新建或打开文件，并写入内容
#输入：filename-文件名(也可以是文件的路径),content-写入的内容(列表)
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

#描述：打开文件，替换第几行的内容
#输入：filename-文件名(也可以是文件的路径),row-需要替换的第几行(从第0行开始),content-写入的内容（字符串或列表）
#输出：无
def modify_file2(filename,row,content):
    #打开文件filename，以可读写的模式打开
    file = open(filename,'r+')
    try:
        file.seek(row)
        #把内容content写入文件filename
        file.write(content)
    finally:
        #关闭文件
        file.close()


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