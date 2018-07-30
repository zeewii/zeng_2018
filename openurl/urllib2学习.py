#coding=utf-8

import urllib2,urllib3,urllib
'''
#urllib
response = urllib.urlopen('http://www.hupu.com')
#响应头部
print response.info()
#状态码
print response.getcode()
#请求的url
print response.geturl()
#响应的实体内容
print response.read()
#或者响应的实体内容2
for line in response:
    print line
'''
'''
#urllib2应用1
response = urllib2.urlopen('http://www.hupu.com')
#响应头部
print response.info()
#状态码
print response.getcode()
#请求的url
print response.geturl()
#响应的实体内容
print response.read()
#或者响应的实体内容2
for line in response:
    print line
'''



#urllib 和urllib2都是接受URL请求的相关模块，但是urllib2可以接受一个Request类的实例来设置URL请求的headers，urllib仅可以接受URL。
#这意味着，urllib不可以伪装你的User Agent字符串等。
#urllib提供urlencode方法用来GET查询字符串的产生，而urllib2没有。这是为何urllib常和urllib2一起使用的原因。
#目前的大部分http请求都是通过urllib2来访问的
'''
#urllib2应用2
#urllib2.Request()的功能是构造一个请求信息，返回的request就是一个构造好的请求,是Request类的实例
request = urllib2.Request('http://www.hupu.com')
#urllib2.urlopen()的功能是发送刚刚构造好的请求request，并返回一个文件类的对象response，包括了所有的返回信息。
response = urllib2.urlopen(request)
print response.read()
'''
#有时你会碰到，程序也对，但是服务器拒绝你的访问。这是为什么呢?问题出在请求中的头信息(header)。
# 有的服务端有洁癖，不喜欢程序来触摸它。这个时候你需要将你的程序伪装成浏览器来发出请求。请求的方式就包含在header中。
#常见的情形：
url = "http://mail.sina.com.cn/"
# 将user_agent写入头信息
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
#values是POST的数据
values = {'name' : 'zeewii','password':'zeng@07150830'}
#请求的http头部
headers = { 'User-Agent' : user_agent }
#使用urllib的urlencode方法产生需要POST的数据
data = urllib.urlencode(values)
#使用urllib2的Request类来定义一个实例，Request类包含有url，产生的POST数据，http的headers头部
req = urllib2.Request(url, data, headers)
#发送请求，返回请求的响应的信息
response = urllib2.urlopen(req)
the_page = response.read()
print the_page