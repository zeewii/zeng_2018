#coding=utf-8
#描述：本模块为通过使用pexpect模块登录ssh输入命令，并取出输入结果
#作者：曾祥卫


import datetime
import pexpect


#输入：user-登录名,ip-登录ip,password-登录密码,command-输入命令
#输出：输入命令返回的结果
def ssh_command(user,ip,password,command):
    try:
        #第一次登录ssh（即没有public key）时的提示字符串
        ssh_newkey = 'Are you sure you want to continue connecting(yes/no)?'
        # 为ssh命令生成一个spawn类的子程序对象
        child = pexpect.spawn('ssh -l %s %s %s'%(user,ip,command))
        #列出期望出现的字符串，超时，ssh_newkey，或'password:'
        i = child.expect([pexpect.TIMEOUT,ssh_newkey,'password: '])

        #如果出现的字符串为pexpect.TIMEOUT超时
        if i == 0:
            print 'ssh登录超时:'
            #打印出错信息
            print child.before, child.after
            return None

        #如果出现的字符串为ssh_newkey，即第一次登录，没有public key
        if i == 1:
            #输入'yes'
            child.sendline('yes')
            #列出期望出现的字符串，超时或'password:'
            i = child.expect([pexpect.TIMEOUT, 'password: '])
            #如果出现的字符串为pexpect.TIMEOUT超时
            if i == 0:
                print 'ssh登录超时:'
                #打印出错信息
                print child.before, child.after
                return None

        #如果出现的字符串为'password: ', 输入密码
        child.sendline(password)

        #列出输入密码后期望出现的字符串，'password',EOF，超时
        i = child.expect(['password: ',pexpect.EOF,pexpect.TIMEOUT])
        #匹配到字符'password: '，打印密码错误
        if i == 0:
            print '密码输入错误！'
        #匹配到了EOF，打印ssh登录成功，并输入命令后成功退出
        elif i == 1:
            print '恭喜,ssh登录输入命令成功！'
        #匹配到了超时，打印超时
        else:
            print '输入命令后等待超时！'

        #将执行命令的时间和结果以追加的形式保存到ssh_log.txt文件中备份文件
        f = open('ssh_log.txt','a')
        str1 = str(datetime.datetime.now())+' '+command
        f.writelines(str1+child.before)
        f.close()
        #返回命令的输出结果
        result = child.before
        return result

    #异常打印原因并删除public key
    except pexpect.ExceptionPexpect, e:
        print "ssh连接失败，正在重启进程",str(e)
        pexpect.run("rm -rf ~/.ssh")





if __name__ == '__main__':
    user = 'zeng'
    ip = '192.168.88.11'
    password = 'zeng'
    command ='ifconfig'
    result = ssh_command(user,ip,password,command)
    print result