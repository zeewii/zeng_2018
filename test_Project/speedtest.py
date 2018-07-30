#coding=utf-8
#描述：本模块实现通过speedtest-cli命令进行测试
#作者：曾祥卫

import subprocess

def speedtest():
    try:
        #输入speedtest-cli进行测试，结果取出
        results = subprocess.check_output('speedtest-cli',shell=True)
        #结果分开成列表
        result = results.split('\n')

        #取出下载和上传的结果并转换为浮点数
        download = float(result[6].strip('Download: ').strip(' Mbit/s'))
        upload = float(result[8].strip('Upload: ').strip(' Mbit/s'))
        print '下载速度为：',download,'Mbit/s'
        print '上传速度为：',upload,'Mbit/s'
    except Exception,e:
        print str(e)



if __name__ == '__main__':
    speedtest()
