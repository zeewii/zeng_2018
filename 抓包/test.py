#!/usr/bin/python2.7
#coding=utf-8

import pcap
import dpkt

#目标ip地址，用于过滤
dst_lists = [
    '192.168.5.250',
    '103.235.46.39',
    '103.235.46.38'
]

#创建一个抓包对象pc
pc=pcap.pcap("eth0")
#设置监听过滤器，可以是'tcp' 'udp' 'port 80' 'tcp port 80'等过滤用的
pc.setfilter('tcp port 80')
# p_time为收到时间，p_data为收到数据(估计pc为元素为元组的列表，即[(p_time1,p_data1),(p_time2,p_data2),...])
for p_time, p_data in pc:
    #使用模块dpkt中ethernet.Ethernet来解包
    p=dpkt.ethernet.Ethernet(p_data)
    #print ("%s %x",p_time,p)
    #如果p.data数据类型为网络层数据包
    if p.data.__class__.__name__ == 'IP':
        #ip层数据包
        ip_data = p.data
        src_ip = '%d.%d.%d.%d' % tuple(map(ord, list(ip_data.src)))
        dst_ip = '%d.%d.%d.%d' % tuple(map(ord, list(ip_data.dst)))
        #print(src_ip,dst_ip)
        #网络层数据包里面的传输层为tcp协议
        if p.data.data.__class__.__name__ == 'TCP':
            #传输层数据包
            tcp_data = p.data.data
            #目的端口为80
            if tcp_data.dport == 80:
                #应用层数据
                appl_data = tcp_data.data
                #如果应用层的数据存在
                if appl_data:
                    #print(src_ip,dst_ip)
                    #print tcp_data.data
                    #如果目的ip在过滤的ip列表中，打印应用层数据
                    if dst_ip in dst_lists:
                        tmp = appl_data.strip()
                        if tmp.startswith("POST") or tmp.startswith("GET"):
                            req_data = tmp + "\n"
                            print req_data
            #源端口为80
            if tcp_data.sport == 80:
                #应用层数据
                appl_data = tcp_data.data
                #如果应用层的数据存在
                if appl_data:
                    #如果目的ip在过滤的ip列表中，打印应用层数据
                    if src_ip in dst_lists:
                        tmp = appl_data.strip().split("\r\n\r\n")[0]
                        if tmp.startswith("HTTP"):
                            req_data = tmp + "\n\n"
                            print req_data



