#!/usr/bin/env python
#coding=utf-8
#描述：使用柱形图或饼图进行画图

from pyecharts import Pie, Page, Style, Bar
import subprocess

class Picture_type():
    u"""使用哪种类型进行画图"""
    def __init__(self,title,subtitle,type_name,name_list,rate_list):
        self.title = title
        self.subtitle = subtitle
        self.type_name = type_name
        self.name_list = name_list
        self.rate_list = rate_list

    def bar_charts(self):
        u"""柱形图"""
        bar = Bar(title=self.title,subtitle=self.subtitle)
        bar.add(self.type_name, self.name_list,self.rate_list)
        bar.render(path=r'/home/test/图片/bar_charts.gif')

    def pie_charts(self):
        u"""饼图"""
        pie = Pie(title=self.title,subtitle=self.subtitle)
        pie.add(self.type_name,self.name_list, self.rate_list,is_label_show=True)
        pie.render(path=r'/home/test/图片/pie_charts.gif')




def huatu():
    while True:
        pic_type = raw_input("请输入需要绘制的图片类型:(柱形图或饼图？)")
        if ("柱形" in pic_type) or ("zhuxing" in pic_type) :
            title = raw_input("请输入图片标题:")
            subtitle = raw_input("请输入图片副标题:")
            type_name = raw_input("请输入商品类型:")
            names = raw_input("请输入商品名称（以空格隔开）:")
            names_list = names.split()
            rate = raw_input("请输入各自商品的数量（以空格隔开）:")
            rate_list = rate.split()
            m = Picture_type(title,subtitle,type_name,names_list,rate_list)
            m.bar_charts()
            subprocess.call("xdg-open /home/test/图片/bar_charts.gif", shell=True)
            break
        elif ("饼图" in pic_type) or ("bingtu" in pic_type):
            title = raw_input("请输入图片标题:")
            subtitle = raw_input("请输入图片副标题:")
            type_name = raw_input("请输入商品类型:")
            names = raw_input("请输入商品名称（以空格隔开）:")
            names_list = names.split()
            rate = raw_input("请输入各自商品的数量（以空格隔开）:")
            rate_list = rate.split()
            m = Picture_type(title,subtitle,type_name,names_list,rate_list)
            m.pie_charts()
            subprocess.call("xdg-open /home/test/图片/pie_charts.gif", shell=True)
            break
        #输入q或quit，直接退出循环
        elif (pic_type == "q") or (pic_type == "quit"):
            print("退出画图小工具！")
            break
        #输入为空，重复总循环
        elif pic_type == "":
            continue
        else:
            print("类型输入错误，请重新输入！")
            continue




huatu()

