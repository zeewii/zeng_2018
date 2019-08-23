#!/usr/bin/python3
#coding=utf-8

import pexpect, sys, os
class scp_file():
    def __init__(self, ip, user, password):
        self.ip = ip
        self.user = user
        self.password = password

    def scp_to_remote(self, filename, dir):
        u"""实现通过scp拷贝文件到另一个主机上"""
        try:
            scp_newkey = 'Are you sure you want to continue connecting (yes/no)?'
            # 为scp命令生成一个spawn类的子程序对象
            child = pexpect.spawn('scp %s %s@%s:%s'%(filename, self.user, self.ip, dir))
            #列出期望出现的字符串，超时，'password',scp_newkey
            i = child.expect([pexpect.TIMEOUT,scp_newkey,'password: '])

            #如果匹配到了超时
            if i == 0:
                print(u"scp登录时出现超时:")
                #打印出错信息
                print(child.before, child.after)
                return None

            #如果出现的字符串为ssh_newkey，即第一次登录，没有public key
            if i == 1:
               #输入'yes'
                child.sendline('yes')
                #列出期望出现的字符串，超时或'password:'
                i = child.expect([pexpect.TIMEOUT, 'password: '])
                #如果出现的字符串为pexpect.TIMEOUT超时
                if i == 0:
                    print (u'scp登录时出现超时:')
                    #打印出错信息
                    print (child.before, child.after)
                    return None

            #如果匹配到了密码字符
            child.sendline(self.password)

            #列出输入密码后期望出现的字符串，'password',EOF，超时'
            i = child.expect(["(?i)password",pexpect.EOF,pexpect.TIMEOUT])
            #匹配到pexpect.EOF，
            if i == 0:
                print(u'密码输入错误！')
            elif i == 1:
                #print (u'恭喜,scp上传文件成功！')
                print(child.before)
            else:
                print (u'传输文件超时！')

        except pexpect.ExceptionPexpect as e:
            print (u"scp连接失败",str(e))
            pexpect.run("rm -rf ~/.ssh")

    def scp_to_local(self, filename, dir):
        try:
            scp_newkey = 'Are you sure you want to continue connecting (yes/no)?'
            # 为scp命令生成一个spawn类的子程序对象
            child = pexpect.spawn('scp %s@%s:%s %s'%(self.user, self.ip, filename, dir))
            #列出期望出现的字符串，超时，'password',scp_newkey
            i = child.expect([pexpect.TIMEOUT,scp_newkey,'password: '])

            #如果匹配到了超时
            if i == 0:
                print(u"scp登录时出现超时:")
                #打印出错信息
                print (child.before, child.after)
                return None

            #如果出现的字符串为ssh_newkey，即第一次登录，没有public key
            if i == 1:
               #输入'yes'
                child.sendline('yes')
                #列出期望出现的字符串，超时或'password:'
                i = child.expect([pexpect.TIMEOUT, 'password: '])
                #如果出现的字符串为pexpect.TIMEOUT超时
                if i == 0:
                    print (u'scp登录时出现超时:')
                    #打印出错信息
                    print (child.before, child.after)
                    return None

            #如果匹配到了密码字符
            child.sendline(self.password)

            #列出输入密码后期望出现的字符串，'password',EOF，超时'
            i = child.expect(["(?i)password",pexpect.EOF,pexpect.TIMEOUT])
            #匹配到pexpect.EOF，
            if i == 0:
                print (u'密码输入错误！')
            elif i == 1:
                print(child.before)
                print (u'恭喜,scp下载文件成功，请到下载目录查看文件！')
            else:
                print (u'传输文件超时！')

        except pexpect.ExceptionPexpect as e:
            print (u"scp连接失败",str(e))
            pexpect.run("rm -rf ~/.ssh")

def scp_to_250():
    SCP_File = scp_file("192.168.5.250", "root", "test")
    mode = input(u"是要上传还是下载文件(默认为上传)：")
    if ("down" not in mode) or (u"下载" not in mode):
        print(u"你选择了上传文件到5.250！")
        filename = input(u"请输入本地的文件名:")
        if "/"  not in filename:
            filename = os.path.join(os.getcwd(), filename)
        else:
            filename = filename.replace("~", "/home/test")
        print(filename)
        dir = input(u"文件要放入5.250服务器的路径:")
        SCP_File.scp_to_remote(filename, "/var/www/html/{}".format(dir.strip("/")))
        sys.exit(0)
    else:
        print(u"你选择了从5.250下载文件！")
        filename = input(u"请输入5.250的文件名:")
        dir = u"/home/test/下载"
        SCP_File.scp_to_local("/var/www/html/{}".format(filename.strip("/")), dir)
        sys.exit(0)

scp_to_250()