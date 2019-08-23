#coding=utf-8
#描述：本模块为通过使用telnetlib模块登录telnet输入命令，并取出输入结果
#作者：曾祥卫


import datetime, time

import telnetlib


#输入：user-登录名,ip-登录ip,password-登录密码,command-输入命令
#输出：输入命令返回的结果
def telnet_command_pc(user,ip,password,commands):
    try:
        #远程主机的命令提示符（标识着上一条命令已执行完毕）
        #finish = b"[$#>]"
        finish = b":~$ "
        #finish = b"*Switch#"
        # 连接Telnet服务器
        child = telnetlib.Telnet(ip, timeout=30)
        #telnet日志级别，默认为0
        child.set_debuglevel(5)

        #出现登录提示，输入用户名
        child.read_until(b'login: ')
        # child.read_until(b'Username: ')
        child.write(user.encode("ascii")+b"\n")
        #出现密码提示，输入密码
        child.read_until(b"Password: ")
        child.write(password.encode("ascii")+b"\n")
        time.sleep(5)
        # print(child.read_eager(), child.read_all(), child.read_very_eager(), child.read_lazy(),child.read_very_lazy(),child.read_some(), sep="\n")

        #for command in commands:
            #child.write(command+'\n')

        #登录完毕后，执行command命令
        child.read_until(finish)
        child.write(commands.encode("ascii")+b"\n")
        #命令执行完毕取出命令输出结果
        child.read_until(finish)
        # print(child.read_eager(), child.read_all(), child.read_very_eager(), child.read_lazy(),child.read_very_lazy(),child.read_some(), sep="\n")
        result = child.read_all().decode("ascii")
        #print(result, child.read_all(), child.read_very_eager(), child.read_lazy(),child.read_very_lazy(),child.read_some(), sep="\n")

        # #将执行命令的时间和结果以追加的形式保存到telnet_log.txt文件中备份文件
        # f = open('telnet_log.txt','a')
        # str1 = str(datetime.datetime.now())+' '
        # f.writelines(str1+result)
        # f.close()

        #终止Telnet连接
        child.close()
        #结果返回给函数（现在没有返回值...）
        return result

    #异常打印原因
    except Exception as e:
        print('telnet连接失败',str(e))


#输入：user-登录名,ip-登录ip,password-登录密码,command-输入命令
#输出：输入命令返回的结果---IES7120-4GS
def telnet_command_switch(user,ip,password,commands):
    try:
        #远程主机的命令提示符（标识着上一条命令已执行完毕）
        #finish = b"[$#>]"
        #finish = b":~$ "
        finish = b"Switch#"
        # 连接Telnet服务器
        child = telnetlib.Telnet(ip, timeout=30)
        #telnet日志级别，默认为0
        child.set_debuglevel(5)
        time.sleep(10)
        #出现登录提示，输入用户名
        child.read_until(b'Username:\x1b[0m')
        # child.read_until(b'Username: ')
        child.write(user.encode("ascii")+b"\n")
        #出现密码提示，输入密码
        child.read_until(b"Password:\x1b[0m")
        #child.read_until(b"Password:")
        child.write(password.encode("ascii")+b"\n")
        time.sleep(5)

        #登录完毕后，执行command命令
        child.read_until(finish)
        child.write(commands.encode("ascii")+b"\n")
        #命令执行完毕取出命令输出结果
        child.read_until(finish)
        result = child.read_all().decode("ascii")

        #终止Telnet连接
        child.close()
        #结果返回给函数（现在没有返回值...）
        return result

    #异常打印原因
    except Exception as e:
        print('telnet连接失败',str(e))

#输入：user-登录名,ip-登录ip,password-登录密码,command-输入命令
#输出：输入命令返回的结果--swos交换机,目前没有返回结果
def telnet_command_switch2(user,ip,password,commands):
    try:
        #远程主机的命令提示符（标识着上一条命令已执行完毕）
        #finish = b"[$#>]"
        #finish = b":~$ "
        finish = b"Switch#"
        # 连接Telnet服务器
        child = telnetlib.Telnet(ip, timeout=30)
        #telnet日志级别，默认为0
        child.set_debuglevel(5)
        time.sleep(10)
        #出现登录提示，输入用户名
        #child.read_until(b'Username:\x1b[0m')
        child.read_until(b'Username: ')
        child.write(user.encode("ascii")+b"\n")
        #出现密码提示，输入密码
        # child.read_until(b"Password:\x1b[0m")
        child.read_until(b"Password:")
        child.write(password.encode("ascii")+b"\r\r\n")
        time.sleep(5)

        #登录完毕后，执行command命令
        child.read_until(finish)
        child.write(commands.encode("ascii")+b"\n")
        time.sleep(5)
        #命令执行完毕取出命令输出结果
        child.read_until(finish)
        result = child.read_eager().decode("ascii")
        print(result)
        #终止Telnet连接
        child.close()
        #结果返回给函数（现在没有返回值...）
        return result

    #异常打印原因
    except Exception as e:
        print('telnet连接失败',str(e))

if __name__ == '__main__':
    # user = 'admin'
    # ip = '192.168.1.252'
    # password = 'admin'
    # commands = 'List'
    # result = telnet_command_switch(user, ip, password, commands)
    # print("result is {}".format(result))
    user = 'admin123'
    ip = '192.168.1.240'
    password = 'admin123'
    commands = 'show arp'
    result = telnet_command_switch2(user, ip, password, commands)
    print("result is {}".format(result))