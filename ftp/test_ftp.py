#coding=utf-8
#描述：本模块为测试ftp传输文件模块
#作者：曾祥卫

import ftp_bussiness
from data_zeng import data



#调出测试所需数据
d = data.ftp_data()

#配置参数开始测试
ftp_bussiness.cycle_ftp(d[0],d[1],d[2],d[3],d[4],2)