import requests
import re

class BaiViet:
    def __init__(self, t, l, a, tg):
        self.tieude = t
        self.link=l
        self.anh = a
        self.thoigian =tg


cafebiz = requests.get("http://cafebiz.vn/")

from bs4 import BeautifulSoup

trangweb = BeautifulSoup(cafebiz.content,"html.parser")


list_home= trangweb.find("div",class_="list_home")
li_list= list_home.find_all("li")

baiviet=[]
for li in li_list:
    tieude= li.find("h3").get_text()
    link="http://cafebiz.vn"+ li.find("h3").a['href']
    anh= li.img['src']
    thoigian= li.find("span",class_="time").get_text()
    baiviet.append(BaiViet(tieude,link,anh,thoigian))

for i in range(0,10):
   print(str.format("{0}.{1}",i+1,baiviet[i].tieude))
print("-----------------------------")

tin= int(input("Bạn đọc tin số mấy: "))
print("-----------------------------")

bai = requests.get(baiviet[tin-1].link)
bai_web = BeautifulSoup(bai.content,"html.parser")


print("Tiều đề:",bai_web.find("h1",class_="title").get_text())
print("Tóm tắt")
print(bai_web.find("h2",class_="sapo").get_text())
print("-----------------------------")
print("Nội dung")
print(bai_web.find("div",class_="detail-content").get_text())

#khai bao them thuoc tinh
#post.content=conent