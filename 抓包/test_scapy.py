#!/usr/bin/python3
#coding=utf-8
import pexpect, os
from scapy.all import *

# #pcap_saved = sniff(offline="demo.pcap")
# pcap_saved = rdpcap("demo.pcap")
# print(type(pcap_saved))
# a = pcap_saved[3][IP].dst
# b = pcap_saved[3][DNS].qd.qname
# print(a,b)
# print(type(a), type(b))
#
# c = str(b, encoding='utf-8')
# print(c,type(c))


# pcap_saved = sniff(offline="dywdz.pcap", filter="port 80",prn=lambda x:x.summary())
# f = pcap_saved[4]["TCP"]
# a = pcap_saved[4][Raw].load
# print(a,type(a))
# b = str(a, encoding='utf-8')
# print(b)
# d = pcap_saved[4]["Ether"].src
# #c = str(d, encoding='utf-8')
#
# print(d,type(d),type(f))

PATH_capture = os.path.join(os.path.dirname(__file__), "data", "capture.pcap")
#抓包
def capture_packet(PCpwd, sniff_param):
    try:
        finish = ">>>"
        #首先删除掉先前保存的capture.pcap文件
        if os.path.exists(PATH_capture):
            os.unlink(PATH_capture)
        #进入scapy的配置命令
        child = pexpect.spawn('sudo scapy')
        child.expect([':',pexpect.TIMEOUT,pexpect.EOF])
        child.sendline(PCpwd)
        time.sleep(2)
        #抓包
        child.expect(finish)
        child.sendline('pcap = sniff({})'.format(sniff_param))
        print(sniff_param)
        #保存
        child.expect([finish,pexpect.TIMEOUT])
        child.sendline('wrpcap("capture.pcap", pcap)')
        print('wrpcap("capture.pcap", pcap)')
        #退出scapy
        child.expect([finish,pexpect.TIMEOUT])
        child.sendline('quit()')
        print('quit()')
        #退出scapy交互模式
        child.close(force=True)
        #判断是否存在capture.pcap文件,并返回其值
        result = os.path.exists(PATH_capture)
        print(result)
        return result
    #捕捉异常并打印异常信息
    except Exception as e:
        raise Exception("capture packet fail! The reason is %s"%e)

#解包
def parsing_packet(offline=PATH_capture,filter=None):
    try:
        #读取本地数据包
        pcap = sniff(offline=offline, filter=filter)
        return pcap
    #捕捉异常并打印异常信息
    except Exception as e:
        raise Exception("parsing packet fail! The reason is %s"%e)

# capture_packet("test",'timeout=60, iface="eth0",filter="udp port 54321", count=1')
#capture_packet('pcap = sniff(iface="eth0",filter="udp port 12345", count=5)')
a = parsing_packet('capture.pcap')
print(type(a))
# a[10].show()
# b = str(a[3]["TCP"].flags)
# print(b,type(b))


#遍历整个包
for i in a:
    #如果有某个包的TCP的flags为PA，即有数据推送时，则打印该数据包的Raw
    if str(i["TCP"].flags) == "PA":
        result = str(i["Raw"].load, encoding="utf-8")
        print(result)
for i in a:
    a.show()
b = str(a[3]["Raw"].load, encoding="utf-8")
print(a[3]["IP"].dst, b, sep="\n")

#dhcp
# a.summary()
# a[2].show()
# b = a[2]["DHCP"].options
# c = dict(b[:5])
# print(b,c["message-type"],type(c))

# a.summary()
# for i in a :
#     if i.haslayer("BOOTP"):
#         i.show()
#         print(dict(i["DHCP"].options[:1])["message-type"])

# a[2].show()
# b = a[2]["IP"].src
# print(b,type(b))
print(a)
a.summary()
a[0].show()
print(a[0].dst, a[0].src, a[0]["IP"].src, a[0]["IP"].dst, a[0].dport)

