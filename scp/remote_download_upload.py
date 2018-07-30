#coding=utf-8
#描述：本模块实现通过模块paramiko实现远程下载和上传文件(目前PC之间可以，对路由还有问题)
#作者：曾祥卫

from ssh import ssh_pexpect
from public import public
import scp
import subprocess,paramiko,time


#描述：本函数实现通过paramiko拷贝文件到另一个主机上
#输入：filename-remote主机的文件名，user-登录名,ip-登录ip,
    # password-登录密码,dir-本地主机的路径
#输出：无
def remote_download(ip,user,password,filename,dir):
    t = paramiko.Transport((ip,22))
    t.connect(username = user, password = password)
    sftp = paramiko.SFTPClient.from_transport(t)
    sftp.get(filename, dir)
    t.close()


if __name__ == "__main__":
    filename = '/etc/version/wifidog'
    ip = '192.168.11.1'
    user = 'root'
    password = 'BHU@100msh$%^'
    dir = '/home/zeng/wifdog'
    content = ['3\n']
    remote_download(ip,user,password,filename,dir)