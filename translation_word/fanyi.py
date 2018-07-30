#!/usr/bin/env python
#coding=utf-8
#描述：两个词典：有道和百度，默认使用有道(相互切换使用youdao和baidu)，q或quit退出
#注意：百度词典，每月只提供200万字符的免费额度，超出需要按照字符数收费！
import json
import requests
import random, md5
import sys

class Dict_Trans():
    u""""两个词典：有道和百度"""
    def __init__(self, word):
        # word 为需要翻译的词或者句子，utf-8编码
        self.word = word

    def youdao(self):
        u"""有道词典，返回翻译后的结果"""
        try:
            # 有道词典 api
            url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null'
            data = {
                'i':self.word,
                'from':'AUTO',
                'to':'Auto',
                'doctype':'json',
                'version':'2.1',
                'keyfrom':'fanyi.web',
                'action':'FY_BY_CLICKBUTTION',
                'typoResult':'false'
                    }
            response = requests.post(url, data=data, timeout=5)
            if response.status_code == 200:
                r = json.loads(response.text)
                translate_result = r['translateResult'][0][0]['tgt']
                print(u"翻译的词/句为：{}".format(translate_result))
                return translate_result
            else:
                print(u"出错了，请再试一次")
                return None
        except requests.exceptions.ConnectionError:
            print(u"连接翻译服务器异常：requests.exceptions.ConnectionError，请检查网络后重试")
            sys.exit(0)

    def baidu(self):
        u"""百度词典，返回翻译后的结果"""
        try:
            # 百度词典 api
            url="http://api.fanyi.baidu.com/api/trans/vip/translate"
            #appid和key需要通过注册获得
            appid = '20180725000188849' #你的appid
            secretKey = 'NtFbgrE_SfK1ICr6hmPY' #你的密钥
            #salt为随机数，int
            salt = str(random.randint(32768, 65536))
            #签名sign为appid+q+salt+key的md5值
            sign = appid+self.word+str(salt)+secretKey
            m1 = md5.new()
            m1.update(sign)
            sign = m1.hexdigest()
            data = {
                'q':self.word,
                'appid':appid,
                'from':'auto',
                'to':'auto',
                'salt':salt,
                'sign': sign
                    }
            response = requests.post(url, data=data, timeout=5)
            if response.status_code == 200:
                r = json.loads(response.text)
                result = r['trans_result'][0]['dst']
                print(u"翻译的词/句为：{}".format(result))
                return result
            else:
                print(u"出错了，请再试一次")
                return None
        except requests.exceptions.ConnectionError:
            print(u"连接翻译服务器异常：requests.exceptions.ConnectionError，请检查网络后重试")
            sys.exit(0)

def translation():
    u"""输入需要翻译的词或句子，调用Dict_Trans类进行翻译"""
    while True:
        #word = input(u"请输入需要翻译的词或句子:")
        word = raw_input("请输入需要翻译的词或句子:")
        #输入q或quit，直接退出总循环
        if (word == "q") or (word == "quit"):
            print("退出翻译小工具！")
            break
        #输入为空，重复总循环
        elif word == "":
            continue
        #输入baidu，进入百度词典循环中
        elif word == "baidu":
            print(u"进入百度词典中...")
            while True:
                #word1 = input(u"请输入需要翻译的词或句子:")
                word1 = raw_input("请输入需要翻译的词或句子:")
                #输入q或quit，直接退出总循环
                if (word1 == "q") or (word1 == "quit"):
                    print("退出翻译小工具！")
                    return
                #输入youdao，跳出百度词典循环
                elif word1 == "youdao":
                    print(u"回到有道词典中...")
                    break
                #输入为空，重复百度循环
                elif word1 == "":
                    continue
                #正常输入字符，则使用百度词典翻译
                trans_baidu = Dict_Trans(word1)
                trans_baidu.baidu()
            #加一个continue，让输入baidu后，跳出百度词典循环后，跳回重复总循环，防止跳出百度词典后往下执行
            continue
        #正常输入字符，则使用有道词典翻译
        trans_youdao = Dict_Trans(word)
        trans_youdao.youdao()





translation()