#!/usr/bin/python3
#coding=utf-8
import requests, yaml
from bs4 import BeautifulSoup
import traceback
import re
import time, urllib3


#headers = {'User-Agent': "Mozilla/5.0 (X11; Linux i686; rv:38.0) Gecko/20100101 Firefox/38.0"}
# 根据获得的网址爬取指定网页信息
def get_html_text(url, code="utf-8"):
    try:
        r = requests.get(url, timeout=30) # 把爬取后的内容赋给r
        r.encoding = code
        #print(r.status_code,r.text)
        return r.text # 返回爬取网页后的文本
    except RuntimeError: # 一般超时错误
        return ""  # 函数结束返回

#输入url获取股票的价格
def from_url_get_price(url):
    html = get_html_text(url)
    soup = BeautifulSoup(html, 'html.parser')
    div = soup.find('div', attrs={'class': 'stock-bets'})
    try:
        #如果是涨的话
        name = div.find_all(attrs={'class': 'price s-up '})[0]
        price = name.text.split()
        #print(price[0], price[1], price[2])
        return price[0], price[1], price[2]
    except:
        #如果是跌的话
        name = div.find_all(attrs={'class': 'price s-down '})[0]
        price = name.text.split()
        #print(price[0], price[1], price[2])
        return price[0], price[1], price[2]

#从配置文件yaml中获取股票信息
def get_stock_yaml():
    with open(u"/home/test/tools/stock.yaml", "r") as yaml_file:
        yaml_obj = yaml.load(yaml_file.read())
        stock_list = yaml_obj["stock"]
        return stock_list

#获取股票名称对应的代码
def get_stock_num(name):
    stock_list = get_stock_yaml()
    return str(stock_list[name])


#由股票名称生成对应的url
def get_stock_url(name_back):
    name = name_back.strip()
    #获取股票代码
    if (name == u"上证指数") or (name == "szzs") or (name == "sz"):
        stcok_num_str = "sh000001"
    elif (name == u"深证成指") or (name =="szcz") or (name =="sc"):
        stcok_num_str = "sz399001"
    elif (name == u"创业板指") or (name == "cybz") or (name == "cy"):
        stcok_num_str = "sz399006"
    elif (name == u"丽珠集团") or (name == "lzjt") or (name == "lz"):
        stcok_num_str = "sz000513"
    elif (name == u"格力电器") or (name == "gldq") or (name == "gl"):
        stcok_num_str = "sz000651"
    elif (name == u"华侨城A") or (name == "hqca") or (name == "hqc"):
        stcok_num_str = "sz000069"
    elif (name == u"华泰证券") or (name == "htzq") or (name == "ht"):
        stcok_num_str = "sh601688"
    elif (name == u"东珠生态") or (name == "dzst") or (name == "dz"):
        stcok_num_str = "sh603359"
    elif (name == u"贵研铂业") or (name == "gyby") or (name == "by"):
        stcok_num_str = "sh600459"
    else:
        stock_num = get_stock_num(name)
        if stock_num.startswith("6"):
            stcok_num_str = "sh" + stock_num
        else:
            stcok_num_str = "sz" + stock_num
    url = 'http://gupiao.baidu.com/stock/{}.html'.format(stcok_num_str)
    return url

#输入名称，获取股票的价格
def from_name_get_price(name):
    try:
        #由股票名称生成对应的url
        url = get_stock_url(name)

        #输入url获取股票的价格
        price = from_url_get_price(url)
        return price
    except:
        print(u"请输入正确的名称！")


def main():
    while True:
        name_input = input(u"请输入名称：")
        name = name_input.strip()
        #输入q或quit，直接退出总循环
        if (name == "q") or (name == "quit"):
            print("退出查询工具！")
            break
        #输入为空，重复总循环
        elif name == "":
            continue
        elif name == "dp":
            price1 = from_name_get_price(u"上证指数")
            price2 = from_name_get_price(u"深证成指")
            price3 = from_name_get_price(u"创业板指")
            print("sz:{};sc:{};cy:{}".format(price1, price2, price3))
            continue
        elif name =="gz":
            price1 = from_name_get_price(u"贵研铂业")
            price2 = from_name_get_price(u"泸州老窖")
            price3 = from_name_get_price(u"华泰证券")
            price4 = from_name_get_price(u"丽珠集团")
            print("gyby:{};lj:{};ht:{};lz:{}".format(price1, price2, price3, price4))
            continue

        price = from_name_get_price(name)
        print(price)

main()