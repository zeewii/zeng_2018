#coding=utf-8
#描述：本模块为测试ftp传输文件模块
#作者：曾祥卫

import pexpect

#判断是否能够连接ftp成功
def check_ftp_connect(host):
        try:
            # 为 ssh 命令生成一个 spawn 类的子程序对象.
            child = pexpect.spawn('ftp', timeout=10)
            #期望具有提示输入用户名的字符出现
            child.expect(['ftp>', pexpect.TIMEOUT])
            child.sendline("open {}".format(host))
            i = child.expect(["(?i)Name",'(?i)No route to host', '(?i)Connection refused', pexpect.TIMEOUT])
            if i == 0:
                print(u"能够连接成功")
                print(child.before, child.after)
                child.close(force=True)
                return True
            else:
                print(u"不能够连接成功")
                print(child.before, child.after)
                child.close(force=True)
                return False

        except Exception as e:
            print(u"ftp连接失败")
            print(e)



check_ftp_connect("192.168.5.200")