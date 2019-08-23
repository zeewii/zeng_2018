#coding=utf-8


import requests, os
from bs4 import BeautifulSoup


r = requests.get("http://www.qq.com")
# # print(r.text)
# print(r.status_code)
# print(r.content.decode('gbk'))
#r = requests.get("https://www.baidu.com", verify=False)
#print(r.status_code)
# r.encoding = 'utf-8'
# tmp = r.text
#print(tmp)

tmp = r.content.decode('gbk')
soup = BeautifulSoup(tmp, "html.parser")
areas = soup.find_all("img")
#print(areas)
i = 0
for area in areas:

    if "jpg" in area['src']:
        img_url = area['src'].strip("//")
        img_url1 = "http://"+img_url
        print(img_url1)

        with open("qq%s"%i+'.jpg', 'wb') as f:
            f.write(requests.get(img_url1).content)
    i += 1


# a = requests.get("http://img1.gtimg.com/ninja/2/2018/12/ninja154396025874444.jpg")
# with open("11.jpg", "wb") as f:
#     f.write(a.content)
