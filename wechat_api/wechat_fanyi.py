#!/usr/bin/python
#coding=utf-8
import itchat, requests, time ,subprocess, json, random, sys, md5
reload(sys)
sys.setdefaultencoding('utf-8')

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

def translation(word):
    u"""输入需要翻译的词或句子，调用Dict_Trans类进行翻译"""
    while True:
        #输入q或quit，直接退出总循环
        if (word == "q") or (word == "quit"):
            print(u"退出翻译小工具！")
            break
        #输入为空，重复总循环
        elif word == "":
            continue
        #正常输入字符，则使用有道词典翻译
        trans_youdao = Dict_Trans(word)
        return trans_youdao.youdao()


# itchat.auto_login()
# itchat.send("Hello zeng", toUserName='filehelper')

#1. 实现微信消息的获取
#注册的操作,通过装饰符将print_content注册为处理文本消息的函数
# 文本对应itchat.content.TEXT
# 图片对应itchat.content.PICTURE
# 语音对应itchat.content.RECORDING
# 名片对应itchat.content.CARD
# @itchat.msg_register(itchat.content.TEXT)
# def print_content(msg):
#     print(msg['Text'])
#
# itchat.auto_login(hotReload=True)
# itchat.run()

#2.实现微信消息的发送

# itchat.auto_login(hotReload=True)
# itchat.send(msg=u"测试消息发送",toUserName="filehelper")

# 当然，还有一种更加快捷的回复方法就是在注册函数中直接回复。
# 例如下面的例子将会将文本消息原封不动的返回
# @itchat.msg_register(itchat.content.TEXT)
# def print_content(msg):
#     return msg['Text']
#
# itchat.auto_login(hotReload=True)
# itchat.run()

# 3. 实现最简单的与图灵机器人的交互
# apiUrl = 'http://www.tuling123.com/openapi/api'
# data = {
#     'key'    : '8edce3ce905a4c1dbb965e6b35c3834d', # 如果这个Tuling Key不能用，那就换一个
#     'info'   : 'hello', # 这是我们发出去的消息
#     'userid' : 'wechat-robot', # 这里你想改什么都可以
# }
# # 我们通过如下命令发送一个post请求
# r = requests.post(apiUrl, data=data).json()
#
# # 让我们打印一下返回的值，看一下我们拿到了什么
# print r,r['text']
# 5.实验程序
KEY = '9a7e02089b7843df8063c08d2fa95e3c'
KEY1 = '8edce3ce905a4c1dbb965e6b35c3834d'

def get_response(msg):
    # 这里我们就像在“3. 实现最简单的与图灵机器人的交互”中做的一样
    # 构造了要发送给服务器的数据
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key'    : KEY,
        'info'   : msg,
        'userid' : 'wechat-robot',
    }
    try:
        r = requests.post(apiUrl, data=data).json()
        # 字典的get方法在字典没有'text'值的时候会返回None而不会抛出异常
        return r.get('text')
    # 为了防止服务器没有正常响应导致程序异常退出，这里用try-except捕获了异常
    # 如果服务器没能正常交互（返回非json或无法连接），那么就会进入下面的return
    except:
        # 将会返回一个None
        return

# 这里是我们在“1. 实现微信消息的获取”中已经用到过的同样的注册方法
@itchat.msg_register(itchat.content.TEXT)
def filehelper_reply(msg,sender="filehelper"):
    print(msg['Text'])
    word = msg['Text'].strip()
    result = translation(word)
    itchat.send(msg=result, toUserName=sender)
    now = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
    print(u'%s:翻译%s成功！' %(now, word))



def wechat():
    itchat.auto_login(hotReload=True)
    itchat.run()









wechat()