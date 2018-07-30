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
        #输入baidu，进入百度词典循环中
        elif word == "baidu":
            print(u"进入百度词典中...")
            while True:
                #输入q或quit，直接退出总循环
                if (word == "q") or (word == "quit"):
                    print(u"退出翻译小工具！")
                    return
                #输入youdao，跳出百度词典循环
                elif word == "youdao":
                    print(u"回到有道词典中...")
                    break
                #输入为空，重复百度循环
                elif word == "":
                    continue
                #正常输入字符，则使用百度词典翻译
                trans_baidu = Dict_Trans(word)
                return trans_baidu.baidu()
            #加一个continue，让输入baidu后，跳出百度词典循环后，跳回重复总循环，防止跳出百度词典后往下执行
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
def tuling_reply(msg,sender="filehelper"):
    print(msg['Text'])
    if msg['Text'].strip().startswith(u"翻译"):
        word = msg['Text'].strip().lstrip(u"翻译 ")
        result = translation(word)
        itchat.send(msg=result, toUserName=sender)
    elif msg['Text'].strip().startswith(u"命令call"):
        word = msg['Text'].strip().lstrip(u"命令call ")
        result = subprocess.call(word, shell=True)
        print(result)
        if result == 0:
            itchat.send(msg=u"命令call输入成功", toUserName=sender)
        else:
            itchat.send(msg=u"命令call输入失败", toUserName=sender)
    elif msg['Text'].strip().startswith(u"命令get"):
        word = msg['Text'].strip().lstrip(u"命令get ")
        result = subprocess.check_output(word, shell=True)
        print(result)
        itchat.send(msg=result, toUserName=sender)
    # 为了保证在图灵Key出现问题的时候仍旧可以回复，这里设置一个默认回复
    defaultReply = 'I received: ' + msg['Text']
    # 如果图灵Key出现问题，那么reply将会是None
    reply = get_response(msg['Text'])
    # a or b的意思是，如果a有内容，那么返回a，否则返回b
    # 有内容一般就是指非空或者非None，你可以用`if a: print('True')`来测试
    return reply or defaultReply


def wechat(send_msg=u"测试",sender="filehelper"):
    itchat.auto_login(hotReload=True)
    while True:
        wechat_type = raw_input("请输入需要微信回复的类型:(发消息或图灵机器人回复)")
        if wechat_type == "send":
            itchat.send(msg=send_msg,toUserName=sender)
            now = time.strftime('%Y%m%d%H%M',time.localtime(time.time()))
            print(u"%s:发送'%s'成功！"%(now,send_msg))
        elif wechat_type == "tuling":
            itchat.run()
            now = time.strftime('%Y%m%d%H%M',time.localtime(time.time()))
            print(u'%s:图灵机器人回复成功！'%now)
        #输入q或quit，直接退出循环
        elif (wechat_type == "q") or (wechat_type == "quit"):
            print("退出微信小工具！")
            break
        #输入为空，重复总循环
        elif wechat_type == "":
            continue
        else:
            print("类型输入错误，请重新输入！")
            continue





wechat()