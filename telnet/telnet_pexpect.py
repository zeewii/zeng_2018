#coding=utf-8
#描述：本模块为通过使用pexpect模块登录telnet输入命令，并取出输入结果
#作者：曾祥卫


import datetime
import pexpect


#输入：user-登录名,ip-登录ip,password-登录密码,command-输入命令
#输出：输入命令返回的结果
def telnet_command_pc(ip, user, password, command):
    try:
        #远程主机可能的命令提示符'$#>'（标识着上一条命令已执行完毕）
        finish = "[$#>]"
        # 为telnet命令生成一个spawn类的子程序对象
        child = pexpect.spawn('telnet %s'%ip)
        #列出期望出现的字符串，"login","Unknown host",EOF,超时
        i = child.expect(["(?i)login: ", "(?i)Unknown host", pexpect.EOF, pexpect.TIMEOUT])

        #匹配到了EOF或TIMEOUT，表示EOF或超时或"(?i)Unknown host"，程序打印提示信息并退出
        if i !=0:
            print(u"telnet登录失败，由于登录时超时或EOF或主机名无效")
            child.close(force=True)

        #如果匹配login字符成功，输入用户名
        else:
            child.sendline(user)
            #列出期望出现的字符串，'password',EOF,超时
            i = child.expect(["(?i)Password: ", pexpect.EOF, pexpect.TIMEOUT])
            #如果匹配password字符成功,输入密码
            if i != 0:
                print(u"telnet登录失败，由于输入密码时超时或EOF")
                #强制退出
                child.close(force=True)
            child.sendline(password)
            #期待远程主机的命令提示符出现
            child.expect(finish)
            #如果匹配提示符成功，输入执行命令
            child.sendline(command)
            #期待远程主机的命令提示符出现
            child.expect(finish)
            # 将命令结果输出
            result = child.before
            print(result)

            # #将执行命令的时间和结果以追加的形式保存到telnet_log.txt文件中备份文件
            # f = open('telnet_log.txt','a')
            # str1 = str(datetime.datetime.now())+' '
            # f.writelines(str1+result)
            # f.close()

            # 将 telnet 子程序的执行权交给用户
            #child.interact()
            #退出telent子程序
            child.close(force=True)

            #返回命令的输出结果
            return result

    #异常打印原因
    except pexpect.ExceptionPexpect as e:
        print('telnet连接失败',str(e))

import time
#输入：user-登录名,ip-登录ip,password-登录密码,command-输入命令
#输出：输入命令返回的结果--7120交换机
def telnet_command_switch(ip, user, password, command):
    try:
        #远程主机可能的命令提示符'$#>'（标识着上一条命令已执行完毕）
        finish = b"[$#>]"
        # 为telnet命令生成一个spawn类的子程序对象
        child = pexpect.spawn('telnet %s'%ip)
        time.sleep(5)
        #列出期望出现的字符串，"login","Unknown host",EOF,超时
        i = child.expect([b"(?i)Username:", b"(?i)Unknown host", pexpect.EOF, pexpect.TIMEOUT])
        print("1 is %s"%i, child.before)
        #匹配到了EOF或TIMEOUT，表示EOF或超时或"(?i)Unknown host"，程序打印提示信息并退出
        if i != 0:
            print(u"telnet登录失败，由于登录时超时或EOF或主机名无效")
            child.close(force=True)

        #如果匹配login字符成功，输入用户名
        else:
            child.sendline(user.encode("ascii"))
            #列出期望出现的字符串，'password',EOF,超时
            i = child.expect([b"(?i)Password:", pexpect.EOF, pexpect.TIMEOUT])
            print("2 is %s"%i)
            #如果匹配password字符成功,输入密码
            if i != 0:
                print(u"telnet登录失败，由于输入密码时超时或EOF")
                #强制退出
                child.close(force=True)
            child.sendline(password.encode("ascii"))
            #期待远程主机的命令提示符出现
            child.expect(finish)
            #如果匹配提示符成功，输入执行命令
            child.sendline(command.encode("ascii"))
            #期待远程主机的命令提示符出现
            child.expect(finish)
            # 将命令结果输出
            result = child.before.decode("ascii")
            print(result)

            # #将执行命令的时间和结果以追加的形式保存到telnet_log.txt文件中备份文件
            # f = open('telnet_log.txt','a')
            # str1 = str(datetime.datetime.now())+' '
            # f.writelines(str1+result)
            # f.close()

            # 将 telnet 子程序的执行权交给用户
            #child.interact()
            #退出telent子程序
            child.close(force=True)

            #返回命令的输出结果
            return result

    #异常打印原因
    except pexpect.ExceptionPexpect as e:
        print('telnet连接失败',str(e))

#输入：user-登录名,ip-登录ip,password-登录密码,command-输入命令
#输出：输入命令返回的结果--swos交换机
def telnet_command_switch2(ip, user, password, command):
    try:
        #远程主机可能的命令提示符'$#>'（标识着上一条命令已执行完毕）
        #finish = b"[$#>]"
        finish = b"#"
        # 为telnet命令生成一个spawn类的子程序对象
        child = pexpect.spawn('telnet %s'%ip)
        time.sleep(5)
        #列出期望出现的字符串，"login","Unknown host",EOF,超时
        i = child.expect([b"(?i)Username:", b"(?i)Unknown host", pexpect.EOF, pexpect.TIMEOUT])
        #匹配到了EOF或TIMEOUT，表示EOF或超时或"(?i)Unknown host"，程序打印提示信息并退出
        if i != 0:
            print(u"telnet登录失败，由于登录时超时或EOF或主机名无效")
            child.close(force=True)

        #如果匹配login字符成功，输入用户名
        else:
            child.sendline(user.encode("ascii"))
            #列出期望出现的字符串，'password',EOF,超时
            i = child.expect([b"(?i)Password:", pexpect.EOF, pexpect.TIMEOUT])
            #如果匹配password字符成功,输入密码
            if i != 0:
                print(u"telnet登录失败，由于输入密码时超时或EOF")
                #强制退出
                child.close(force=True)
            child.send(password.encode("ascii")+b"\r\r\n")
            #期待远程主机的命令提示符出现
            child.expect(finish)
            #如果匹配提示符成功，输入执行命令
            child.sendline(command.encode("ascii"))
            #期待远程主机的命令提示符出现
            child.expect(finish)
            # 将命令结果输出
            result = child.before.decode("ascii")
            print(result)

            #将执行命令的时间和结果以追加的形式保存到telnet_log.txt文件中备份文件
            f = open('telnet_log.txt','a')
            str1 = str(datetime.datetime.now())+' '
            f.writelines(str1+result)
            f.close()

            # 将 telnet 子程序的执行权交给用户
            #child.interact()
            #退出telent子程序
            child.close(force=True)

            #返回命令的输出结果
            return result

    #异常打印原因
    except pexpect.ExceptionPexpect as e:
        print('telnet连接失败',str(e))

if __name__ == '__main__':
    user = 'admin123'
    ip = '192.168.1.240'
    password = 'admin123'
    command ='show arp'
    result = telnet_command_switch2(ip,user,password,command)
    print("result is %s"%result)