#!/usr/bin/python
#coding=utf-8

import subprocess, sys
reload(sys)
sys.setdefaultencoding('utf-8')

def main():
    word = raw_input(u"请输入要搜索的内容:")
    result = word.replace(" ", "")
    subprocess.call("xdg-open https://www.baidu.com/s?wd=%s"%result, shell=True)


main()