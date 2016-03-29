from bs4 import  BeautifulSoup
import requests
import re

cafebiz = requests.get('http://cafebiz.vn/')

file_name ='CafeBiz.html'
file_html = open(file_name,'wb')
file_html.write(cafebiz.content)
file_html.close()

cafebiz = BeautifulSoup(cafebiz.content,'html.parser')

listhome = cafebiz.find('div',class_="list_home")
list = listhome.find_all('li')

for li in list:

    taga = li.find_all('a',recursive=False)
    for a in taga:
        print(a['title'])
        print(a['href'])
        imgs = a.find_all('img')
        for img in imgs:
            print(img['src'])

    tagp = li.find_all('p')
    for p in tagp:

        spans = p.find_all('span')
        for span in spans:
            print(span.text)
            print('---------------------------')


n = input("Bạn đọc tin?:")

tin = listhome.find_all(href = re.compile(n))
for i in tin:
    a=i.get("href")
b = ("http://cafebiz.vn")+a
tintiep = requests.get(b)
trang_tintiep = BeautifulSoup(tintiep.content, "html.parser")

title_tieude = trang_tintiep.find("div", id ="mainDetail")
print("tiêu đề :",title_tieude.h1.string)
print("tóm tắt:", title_tieude.h2.string)
noidung = title_tieude.find("div",{"class":"detail-content"})
print("nội dung:", noidung.get_text().strip())