#coding=utf-8
import requests
from bs4 import BeautifulSoup
import traceback
import re
import time, yaml


# 根据获得的网址爬取指定网页信息
def get_html_text(url, code="utf-8"):
    try:
        r = requests.get(url, timeout=30) # 把爬取后的内容赋给r，等待时间对多30秒
        r.encoding = code
        print(r.status_code,r.text)
        return r.text # 返回爬取网页后的文本
    except RuntimeError: # 一般超时错误
        return ""  # 函数结束返回


# 获得股票列表
def get_stock_list(self, stock_url):
    html = get_html_text(stock_url, "GB2312")
    soup = BeautifulSoup(html, 'html.parser')
    a = soup.find_all('a')
    for i in a:
        try:
            href = i.attrs['href']
            self.append(re.findall(r"[s][hz]\d{6}", href)[0])
        except:
            continue
    print(self)

get_html_text("http://quote.eastmoney.com/stocklist.html", "GB2312")

#
# def get_stock_list(ls, stock_url):
#     html = get_html_text(stock_url, "GB2312")
#     soup = BeautifulSoup(html, 'html.parser')
#     a = soup.find_all('a')
#     for i in a:
#         try:
#             if ("(" and ")") in i.string:
#                 ls.append(str(i.string))
#         except:
#             continue
#     print(ls)
#     return ls






# 获得每个个股的股票信息
def get_stock_information(self, stock_url, path):
    count = 0
    for stock in self:
        url = stock_url + stock + '.html'
        html = get_html_text(url)
        try:
            if html == "":
                continue
            information_dictionary = {}
            soup = BeautifulSoup(html, 'html.parser')
            stock_information = soup.find('div', attrs={'class': 'stock-bets'})
            name = stock_information.find_all(attrs={'class': 'bets-name'})[0]
            information_dictionary.update({'股票名称' : name.text.split()[0]})
            key_list = stock_information.find_all('dt')
            value_list = stock_information.find_all('dd')
            for i in range(len(key_list)):
                key = key_list[i].text
                value = value_list[i].text
                information_dictionary[key] = value
            print(str(information_dictionary))
            with open(path, 'a', encoding = 'utf-8') as f:
                f.write(str(information_dictionary) + '\n')
        except:
            count = count + 1
            print("\r当前进度: {:.2f}%".format(count*100/len(self)), end="")
            continue


# 主函数
def main():
    stock_list_url = "http://quote.eastmoney.com/stocklist.html"
    stock_information_url = "http://gupiao.baidu.com/stock/"
    output_file = "/home/test/stock.txt"
    list = []
    get_stock_list(list, stock_list_url)
    get_stock_information(list, stock_information_url, output_file)

#main()
#get_stock_information(['000513', "000514"], "http://gupiao.baidu.com/stock/", "/home/test/stock.txt")



