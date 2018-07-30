#coding=utf-8
#描述：本模块为通过使用telnetlib模块登录telnet输入命令，并取出输入结果
#作者：曾祥卫


import datetime

import telnetlib


#输入：user-登录名,ip-登录ip,password-登录密码,command-输入命令
#输出：输入命令返回的结果
def telnet_command(user,ip,password,commands):
    try:
        #远程主机的命令提示符（标识着上一条命令已执行完毕）
        finish = ':~$'
        # 连接Telnet服务器
        child = telnetlib.Telnet(ip)
        #telnet日志级别，默认为0
        child.set_debuglevel(1)

        #出现登录提示，输入用户名
        child.read_until('login:')
        child.write(user+'\n')
        #出现密码提示，输入密码
        child.read_until('Password:')
        child.write(password+'\n')

        #for command in commands:
            #child.write(command+'\n')

        #登录完毕后，执行command命令
        child.read_until(finish)
        child.write(commands+'\n')
        #命令执行完毕取出命令输出结果
        child.read_until(finish)
        result = child.read_eager()

        #将执行命令的时间和结果以追加的形式保存到telnet_log.txt文件中备份文件
        f = open('telnet_log.txt','a')
        str1 = str(datetime.datetime.now())+' '
        f.writelines(str1+result)
        f.close()

        #终止Telnet连接
        child.close()
        #结果返回给函数（现在没有返回值...）
        return result

    #异常打印原因
    except Exception,e:
        print 'telnet连接失败',str(e)



if __name__ == '__main__':
    user = 'zeng'
    ip = '192.168.88.11'
    password = 'zeng'
    commands = 'ls /'
    result = telnet_command(user,ip,password,commands)
    print result