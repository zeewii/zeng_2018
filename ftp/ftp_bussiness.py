#coding=utf-8
#描述：本模块为ftp业务层函数
#作者：曾祥卫

import ftp_control

#描述：定义函数循环传输文件
#输入：host-主机名，loginname-登录用户名，loginpassword-登录密码，
     # getfilename-上传文件名，putfilename-上传文件名，n-循环次数
def cycle_ftp(host,loginname,loginpassword,getfilename,putfilename,n):
    i = 0
    while i < n:
        print '第%d次循环传输文件开始\n'%i
        #打开ftp_log.txt记录测试情况
        file = open('ftp_log.txt','a')
        file.writelines('第%d次循环传输文件开始\n'%i)
        file.close()
        try:
            #登录ftp并下载文件后退出
            ftp_control.get(host,loginname,loginpassword,getfilename)
            #登录ftp并上传文件后退出
            ftp_control.put(host,loginname,loginpassword,putfilename)
        #捕捉异常并打印异常信息
        except Exception,e:
            print "第%d次循环传输文件失败，原因如下:%s\n"%(i,e)
            #如果有异常打开ftp_log.txt记录测试情况
            file = open('ftp_log.txt','a')
            file.writelines("第%d次循环传输文件失败，原因如下:%s\n"%(i,e))
            file.close()
            #有异常跳出循环
            #break
        finally:
            i +=1
    #循环传输文件完成,打开ftp_log.txt记录完成
    file = open('ftp_log.txt','a')
    file.writelines('循环传输文件完成！')
    file.close()




__author__ = 'zeng'
