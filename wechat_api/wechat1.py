#!/usr/bin/env python
#coding=utf-8
import itchat, requests

class WeChat():

    def login(self):
        u"""微信登录"""
        itchat.auto_login(hotReload=True)

    def run(self):
        itchat.run()

    @itchat.msg_register(itchat.content.TEXT)
    def print_text(self,msg):
        u"""微信文本消息的获取"""
        print(msg['Text'])

    @itchat.msg_register(itchat.content.PICTURE)
    def print_picture(self,msg):
        u"""微信图片消息的获取"""
        pass

    @itchat.msg_register(itchat.content.RECORDING)
    def print_recording(self,msg):
        u"""微信语音消息的获取"""
        pass

    @itchat.msg_register(itchat.content.CARD)
    def print_card(self,msg):
        u"""微信名片消息的获取"""
        pass

    def send_message(self,msg, sender="filehelper"):
        u"""发送消息"""
        itchat.send(msg=msg,toUserName=sender)

    def auto_reply_same_message(self,msg):
        u"""自动回复相同的消息"""
        return msg['Text']

    def get_tuling_response(self,msg):
        u"""通过图灵机器人根据收到的消息，返回图灵机器人返回的消息"""
        # 构造了要发送给服务器的数据
        apiUrl = 'http://www.tuling123.com/openapi/api'
        KEY = '9a7e02089b7843df8063c08d2fa95e3c'
        data = {
            'key'    : KEY,
            'info'   : msg,
            'userid' : 'wechat-robot',
                }
        try:
            #发送接口请求
            r = requests.post(apiUrl, data=data)
            #json结果转换为python格式
            result = r.json()
            # 字典的get方法在字典没有'text'值的时候会返回None而不会抛出异常
            return result.get('text')
        # 为了防止服务器没有正常响应导致程序异常退出，这里用try-except捕获了异常
        # 如果服务器没能正常交互（返回非json或无法连接），那么就会进入下面的return
        except:
            # 将会返回一个None
            return

    @itchat.msg_register(itchat.content.TEXT)
    def tuling_reply(self,msg):
        u"""整合回复，防止图灵key出错无反应"""
        #首先打印发送的消息
        print(msg['Text'])
        # 如果图灵Key出现问题，那么reply将会是None
        reply = self.get_tuling_response(msg['Text'])
        # 为了保证在图灵Key出现问题的时候仍旧可以回复，这里设置一个默认回复
        defaultReply = 'I received: ' + msg['Text']
        # a or b的意思是，如果a有内容，那么返回a，否则返回b
        # 有内容一般就是指非空或者非None，你可以用`if a: print('True')`来测试
        return reply or defaultReply



tuling = WeChat()
tuling.login()
# tuling.send_message(u"你好！")
tuling.run()

