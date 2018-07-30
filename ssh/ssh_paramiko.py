#coding=utf-8
#描述：本模块为通过使用pexpect模块登录ssh输入命令，并取出输入结果
#作者：曾祥卫

import paramiko


def ssh_command(ip,username,passwd,cmd):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip,22,username,passwd,timeout=5)
        for m in cmd:
            stdin, stdout, stderr = ssh.exec_command(m)
            #stdin.write('y')   #简单交互，输入 ‘Y’
            out = stdout.readlines()
            #屏幕输出
            for o in out:
                print o,

        ssh.close()
    except :
        print '%s\tError\n'%(ip)


if __name__ == '__main__':
    cmd = ['cat /home/zeng/ftp/wifidog']#你要执行的命令列表
    username = "zeng"
    passwd = "zeng"    #密码
    ip = '192.168.11.192'
    ssh_command(ip,username,passwd,cmd)