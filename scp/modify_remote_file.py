#coding=utf-8
#描述：本模块实现通过ssh登录remote主机后修改remote主机文件内容
#作者：曾祥卫

from ssh import ssh_pexpect
from public import public
import scp
import subprocess



#输入：filename-remote主机需要修改的文件名，user-登录名,ip-登录ip,
    # password-登录密码,dir-remote主机的文件路径，content-需要修改的内容
#输出：无
def modify_remote_file(user,ip,password,dir,filename,content):
    #登录remote主机下载需要修改的文件
    scp.scp_to_local(ip,user,password,dir+filename,'../data_zeng/')
    #登录remote主机并备份文件
    ssh_pexpect.ssh_command(user,ip,password,'mv %s%s %s%s_backup'\
                            %(dir,filename,dir,filename))
    print '备份remote主机的文件%s%s成功'%(dir,filename)
    #在本地打开下载的文件，清空原内容并写入需要新内容
    public.modify_file('../data_zeng/%s'%filename,content)
    #通过scp再传输给remote主机
    scp.scp_to_remote('../data_zeng/%s'%filename,ip,user,password,dir)
    print '修改remote主机文件%s%s成功'%(dir,filename)
    #删除本地到文件
    subprocess.call('rm -rf ../data_zeng/%s'%filename,shell=True)



if __name__ == "__main__":
    filename = 'wifidog'
    ip = '192.168.11.1'
    user = 'root'
    password = 'BHU@100msh$%^'
    dir = '/etc/version/'
    content = ['3\n']

    modify_remote_file(user,ip,password,dir,filename,content)

