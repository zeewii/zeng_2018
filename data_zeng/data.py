#coding=utf-8
#描述:本模块用来调用数据，方便测试用例来调用
#作者：曾祥卫


import xlrd

#打开数据路径
file = xlrd.open_workbook('../data_zeng/data.xlsx')

#描述：调取运行ftp时所需要的数据
#输入：目录下/data/data.xlsx-ftp
#输出：以列表形式输出ftp时所需要的数据
def ftp_data():
    try:
        #定义一个列表
        data = []
        #获取文件中的对应的表
        sh=file.sheet_by_name('ftp')
        #取host
        data.append(sh.cell_value(2,1))
        #取用户名
        data.append(sh.cell_value(3,1))
        #取密码
        data.append(sh.cell_value(4,1))
        #取下载文件名
        data.append(sh.cell_value(5,1))
        #取上传文件名
        data.append(sh.cell_value(6,1))
        #将值返回给函数
        return data
    except IOError,e:
        print u"文件信息错误,具体信息：\n%s"%e


#描述：调取运行taobao时所需要的数据
#输入：目录下/data/data.xlsx-taobao
#输出：以字典的形式输出basic中数据
def data_taobao():
    try:
        #定义一个字典
        basic = {}
        #获取对应的表-basic_conf
        table = file.sheet_by_name('taobao')
        #获取表中设备版本
        basic['address'] = table.cell_value(2,1)
        basic['username'] = table.cell_value(3,1)
        basic['password'] = table.cell_value(4,1)
        basic['shopname'] = table.cell_value(5,1)
        return basic
    except IOError,e:
        print u"文件信息错误,具体信息：\n%s"%e


def zeng_1():
    try:
        #打开data.xlsx取测试所需数据
        xlsFile = xlrd.open_workbook('../data_zeng/data.xlsx')
        #获取文件中的对应的表
        sh=xlsFile.sheet_by_name('mac')
        #取测试所需的值
        result = sh.col_values(0)[0:100]
        return result
    except IOError,e:
        print u"文件信息错误,具体信息：\n%s"%e






__author__ = 'zeng'
