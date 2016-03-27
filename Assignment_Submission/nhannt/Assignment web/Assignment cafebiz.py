__author__ = 'Administrator'

from bs4 import BeautifulSoup
import requests
import re

cafebiz = requests.get("http://cafebiz.vn/")

trangweb_cafebiz = BeautifulSoup(cafebiz.content, "html.parser")
home = trangweb_cafebiz.find("div", {"class":"list_home"})

print(home.get_text())
n = input("Bạn đọc tin nào?:")

doctin = home.find_all(href = re.compile(n))
for i in doctin:
    a=i.get("href")
b = ("http://cafebiz.vn")+a
tintiep = requests.get(b)
trang_tintiep = BeautifulSoup(tintiep.content, "html.parser")

title_tieude = trang_tintiep.find("div", id ="mainDetail")
print("Tiêu đề tin bạn chọn là:",title_tieude.h1.string)
print("Tóm tắt:", title_tieude.h2.string)
noidung = title_tieude.find("div",{"class":"detail-content"})
print("Nội dung:", noidung.get_text().strip())

