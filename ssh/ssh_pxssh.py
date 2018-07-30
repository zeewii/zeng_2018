#coding=utf-8
#描述：本模块为通过使用pxssh模块登录ssh输入命令，并取出输入结果
#作者：曾祥卫


import datetime,time

import pxssh,subprocess


#输入：user-登录名,ip-登录ip,password-登录密码,command-输入命令
#输出：输入命令返回的结果
def ssh_command(user,ip,password,command):
    try:
        #为ssh命令生成一个pxssh类的对象
        child = pxssh.pxssh()
        #利用 pxssh 类的 login 方法进行 ssh 登录，\
        # 原始 prompt 为'$' , '#',这里加入'>'
        child.login(ip,user,password,original_prompt='[#$>]')
        #发送命令
        child.sendline(command)
        #匹配 prompt,即匹配最后出现的字符串有'#$>'
        child.prompt()
        result = child.before

        #将执行命令的时间和结果以追加的形式保存到ssh_log.txt文件中备份文件
        f = open('ssh_log.txt','a')
        str1 = str(datetime.datetime.now())+' '
        f.writelines(str1+result)
        f.close()

        # 退出 ssh session
        child.logout()
        # 将 prompt 前所有内容返回给函数,即命令的执行结果
        return result

    #异常打印原因并删除public key
    except pxssh.ExceptionPxssh,e:
        print "ssh连接失败，正在重启进程",str(e)
        subprocess.call("rm -rf ~/.ssh",shell=True)

#通过tcpdump抓各个接口的包
#输入：user-登录名,ip-登录ip,password-登录密码,command-tcpdump的命令
#输出：无
def tcpdump_command(user,ip,password,command):
    try:
        #为ssh命令生成一个pxssh类的对象
        child = pxssh.pxssh()
        #利用 pxssh 类的 login 方法进行 ssh 登录，\
        # 原始 prompt 为'$' , '#',这里加入'>'
        child.login(ip,user,password,original_prompt='[#$>]')
        #发送命令
        child.sendline(command)
        #抓取时间120s
        time.sleep(120)
        #输入Ctrl+c停止tcpdump
        child.sendcontrol('c')
        #匹配 prompt,即匹配最后出现的字符串有'#$>'
        child.prompt()
        #result = child.before

        # 退出 ssh session
        child.logout()
        # 将 prompt 前所有内容返回给函数,即命令的执行结果
        #return result

    #异常打印原因并删除public key
    except pxssh.ExceptionPxssh,e:
        print "ssh连接失败，正在重启进程",str(e)
        subprocess.call("rm -rf ~/.ssh",shell=True)



if __name__ == '__main__':
    user = 'root'
    ip = '192.168.11.1'
    password = 'BHU@100msh$%^'
    command ='tcpdump -i eth1 -s0 -w /tmp/wanlog'
    tcpdump_command(user,ip,password,command)