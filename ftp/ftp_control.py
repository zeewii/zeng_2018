#coding=utf-8
#描述：本模块为ftp控制层函数
#作者：曾祥卫

import pexpect

#描述：登录ftp后下载文件
def get(host,loginname,loginpassword,filename):
    #使用spawn构造一个函数，生成一个spawn类的对象
    child = pexpect.spawn('ftp %s'%host)
    #期望具有提示输入用户名的字符出现
    index = child.expect(["(?i)Name", "(?i)Unknown host", pexpect.EOF, pexpect.TIMEOUT])
    #匹配到了"(?i)Name"，表明接下来要输入用户名
    if index == 0 :
        #输入用户名
        child.sendline(loginname)
        #期望具体有提示输入密码的字符出现
        index = child.expect(["(?i)Password", pexpect.EOF, pexpect.TIMEOUT])
        #没有匹配到"(?i)Password"的字符，表示EOF或超时，打印超时并退出
        if index != 0:
            print u"ftp要求输入密码时出现EOF或超时"
            #强制退出
            child.close(force=True)
        #匹配到了"(?i)Password"，表明接下来要输入用户名，那么输入用户名
        child.sendline(loginpassword)
        #期望登录成功并出现'ftp>'的字符出现
        index = child.expect( ['ftp>', 'Login incorrect', 'Service not available',pexpect.EOF, pexpect.TIMEOUT])
        #匹配到了'ftp>'，则表示登录ftp成功
        if index == 0:
            print u'恭喜！ftp登录成功'
            # 发送 'bin'+ 换行符给子程序，表示接下来使用二进制模式来传输文件.
            child.sendline("bin")
            print u'正在下载文件...'
            #输入下载文件的命令
            child.sendline('get %s'%filename)

            #期望下载成功后，出现 'Transfer complete.*ftp>'的字符
            #直接用正则表达式 '.*' 提示符 'ftp>' 以上的字符全省去.
            index = child.expect( ['Transfer complete.*ftp>', pexpect.EOF, pexpect.TIMEOUT] )
            #没有匹配到'*ftp>'的字符，表示EOF或超时，打印超时并退出
            if index != 0:
                print u"下载文件时出现EOF或超时"
                #强制退出
                child.close(force=True)
            #匹配到了 '*ftp>'，表明下载文件成功，打印成功信息.
            print u'成功下载文件%s'%filename
            #输入 'bye'，结束 ftp session.
            child.sendline("bye")
            print u'传输文件完成，程序退出！'
        #匹配到了'Login incorrect'，则表示登录ftp失败，用户名或密码错误
        elif index == 1:
            print u"登录ftp失败，用户名或密码错误!程序退出"
            child.close(force=True)
        #匹配到其他值（'Service not available',pexpect.EOF, pexpect.TIMEOUT），则表示登录ftp失败.
        else:
            print u"登录ftp失败，服务器不可用或ftp命令退出或超时!程序退出"
            child.close(force=True)
    #匹配到了"(?i)Unknown host"，则表示主机未知
    elif index == 1 :
        print u"没有找到ftp主机!程序退出"
        child.close(force=True)
    #匹配到了 pexpect.EOF 或 pexpect.TIMEOUT，表示超时或者 EOF，程序打印提示信息并退出
    else:
        print u"连接ftp时出现EOF或超时"
        child.close(force=True)


#描述：登录ftp后ftp上传文件
def put(host,loginname,loginpassword,filename):
    #使用spawn构造一个函数，生成一个spawn类的对象
    child = pexpect.spawn('ftp %s'%host)
    #期望具有提示输入用户名的字符出现
    index = child.expect(["(?i)Name", "(?i)Unknown host", pexpect.EOF, pexpect.TIMEOUT])
    #匹配到了"(?i)Name"，表明接下来要输入用户名
    if index == 0 :
        #输入用户名
        child.sendline(loginname)
        #期望具体有提示输入密码的字符出现
        index = child.expect(["(?i)Password", pexpect.EOF, pexpect.TIMEOUT])
        #没有匹配到"(?i)Password"的字符，表示EOF或超时，打印超时并退出
        if index != 0:
            print u"ftp要求输入密码时出现EOF或超时"
            #强制退出
            child.close(force=True)
        #匹配到了"(?i)Password"，表明接下来要输入用户名，那么输入用户名
        child.sendline(loginpassword)
        #期望登录成功并出现'ftp>'的字符出现
        index = child.expect( ['ftp>', 'Login incorrect', 'Service not available',pexpect.EOF, pexpect.TIMEOUT])
        #匹配到了'ftp>'，则表示登录ftp成功
        if index == 0:
            print u'恭喜！ftp登录成功'
            # 发送 'bin'+ 换行符给子程序，表示接下来使用二进制模式来传输文件.
            #child.sendline("bin")
            print u'正在上传文件...'
            #输入上传文件的命令
            child.sendline('put %s'%filename)
            #期望下载成功后，出现 'Transfer complete.*ftp>'的字符
            index = child.expect( ['Transfer complete.*ftp>', pexpect.EOF, pexpect.TIMEOUT] )
            #没有匹配到'*ftp>'的字符，表示EOF或超时，打印超时并退出
            if index != 0:
                print u"上传文件时出现EOF或超时"
                #强制退出
                child.close(force=True)
            #匹配到了 '*ftp>'，表明上传文件成功，打印成功信息.
            print u'成功上传文件%s'%filename
            #输入 'bye'，结束 ftp session.
            child.sendline("bye")
            print u'传输文件完成，程序退出！'
        #匹配到了'Login incorrect'，则表示登录ftp失败，用户名或密码错误
        elif index == 1:
            print u"登录ftp失败，用户名或密码错误!程序退出"
            child.close(force=True)
        #匹配到其他值（'Service not available',pexpect.EOF, pexpect.TIMEOUT），则表示登录ftp失败.
        else:
            print u"登录ftp失败，服务器不可用或ftp命令退出或超时!程序退出"
            child.close(force=True)
    #匹配到了"(?i)Unknown host"，则表示主机未知
    elif index == 1 :
        print u"没有找到ftp主机!程序退出"
        child.close(force=True)
    #匹配到了 pexpect.EOF 或 pexpect.TIMEOUT，表示超时或者 EOF，程序打印提示信息并退出
    else:
        print u"连接ftp时出现EOF或超时"
        child.close(force=True)


'''if __name__ == '__main__':
    host = '192.168.11.104' #ftp的服务器地址
    loginname = 'zeng'      #ftp的登录用户名
    loginpassword = 'zeng'  #ftp的登录密码
    getfilename= 'UltraISO.rar' #下载文件名
    putfilename = 'UltraISO.rar' #上传文件名
    #ftp(host,loginname,loginpassword,getfilename,putfilename)
    get(host,loginname,loginpassword,getfilename)
    put(host,loginname,loginpassword,putfilename)'''




__author__ = 'zeng'
