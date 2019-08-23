#coding=utf-8
#输出十六进制的原始数据
import pcap
import binascii

a=pcap.pcap()
a.setfilter('port 80')
try:
    for i,j in a:
        #输出十六进制的原始数据
        t=binascii.hexlify(j)
        print t
except:
    print 'stop'
    n=raw_input()
