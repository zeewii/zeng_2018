#!/usr/bin/python3
#coding=utf-8
import requests
from bs4 import BeautifulSoup
import traceback
import yaml
import time, urllib3


import tushare as ts
class stock:
    def dapan(self):
    #大盘指数行情列表
        df = ts.get_index()
        print(df)


    def gegu(self, stock):
    #个股历史数据
        current_time = time.strftime('%Y-%m-%d',time.localtime(time.time()))
        df = ts.get_hist_data(stock, start=current_time, end=current_time)
        print(df)



def main():
    Stock = stock()
    while True:
        name_input = input(u"请输入股票名称：")
        name = name_input.strip()
        #输入q或quit，直接退出总循环
        if (name == "q") or (name == "quit"):
            print("退出股票查询工具！")
            break
        #输入为空，重复总循环
        elif name == "":
            continue
        elif (name == u"大盘") or (name =="dapan"):
            Stock.dapan()
            continue

        with open(u"/home/test/tools/stock.yaml", "r") as yaml_file:
            yaml_obj = yaml.load(yaml_file.read())
            stock_list = yaml_obj["stock"]
            for name1 in stock_list:
                if name == name1:
                    Stock.gegu(stock_list[name1])
                    continue
        print(u"名称输入错误，请输入完整的名称！")
        continue

main()








