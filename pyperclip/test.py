#!/usr/bin/python3
#coding=utf-8

import pyperclip, sys


PASSWORDS = {'email':'dddd',
             'blog':'vlmlll'}

#sys.argv列表中的第一项总是一个字符串，它包含程序的文件名（这里是test.py），而第二项是第一个命令行参数（是用户输入的的，比如这里输入email）
if len(sys.argv) < 2:
    print("1")
    sys.exit()

account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print("2")
else:
    print("3")


#在该目录下运行python3 test.py eamil，即可复制键（如email）对应的值（如dddd）