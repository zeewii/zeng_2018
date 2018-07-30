#coding=utf-8
#描述：本模块为通过使用pexpect模块登录telnet输入命令，并取出输入结果
#作者：曾祥卫


import datetime
import pexpect


#输入：user-登录名,ip-登录ip,password-登录密码,command-输入命令
#输出：输入命令返回的结果
def telnet_command(user,ip,password,command):
    try:
        #远程主机可能的命令提示符'$#>'（标识着上一条命令已执行完毕）
        finish = "[$#>]"
        # 为telnet命令生成一个spawn类的子程序对象
        child = pexpect.spawn('telnet %s'%ip)
        #列出期望出现的字符串，"login","Unknown host",EOF,超时
        i = child.expect(["(?i)login", "(?i)Unknown host", pexpect.EOF, pexpect.TIMEOUT])

        #匹配到了EOF或TIMEOUT，表示EOF或超时或"(?i)Unknown host"，程序打印提示信息并退出
        if i !=0:
            print u"telnet登录失败，由于登录时超时或EOF或主机名无效"
            child.close(force=True)

        #如果匹配login字符成功，输入用户名
        else:
            child.sendline(user)
            #列出期望出现的字符串，'password',EOF,超时
            i = child.expect(["(?i)password", pexpect.EOF, pexpect.TIMEOUT])
            #如果匹配password字符成功,输入密码
            if i != 0:
                print u"telnet登录失败，由于输入密码时超时或EOF"
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
            #print result

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
    except pexpect.ExceptionPexpect, e:
        print 'telnet连接失败',str(e)






if __name__ == '__main__':
    user = 'zeng'
    ip = '192.168.11.94'
    password = 'zeng'
    command ='ifconfig'
    result = telnet_command(user,ip,password,command)
    print result