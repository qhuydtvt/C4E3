from bs4 import  BeautifulSoup
import requests
import re

cafebizs = requests.get('http://cafebiz.vn/')

file_name ='CafeBiz.html'
file_html = open(file_name,'wb')
file_html.write(cafebizs.content)
file_html.close()

cafebiz = BeautifulSoup(cafebizs.content,'html.parser')

listhome = cafebiz.find('div',class_="list_home")
lis = listhome.find_all('li')

for li in lis:

    ass = li.find_all('a',recursive=False)
    for a in ass:
        print(a['title'])
        print(a['href'])
        imgs = a.find_all('img')
        for img in imgs:
            print(img['src'])

    ps = li.find_all('p')
    for p in ps:

        spans = p.find_all('span')
        for span in spans:
            print(span.text)
            print()
            print('---------------------------------------------------------------------------------------------------------------------------')
            print()
n=input('what to find')
l = listhome.ul.li
#
# #
# # def take_only_text(title):
# #     return title and re.compile(n).search(title)
#
# thu = l.find_all('a',take_only_text)
# for a in thu:
#     print(a)
trang = listhome.find_all(href= re.compile(n))
for i in trang:
    a=i.get('href')

b=('http://cafebiz.vn/')+a
tintiep = requests.get(b)
trang_tin= BeautifulSoup(tintiep.content,'html.parser')
timtrang = trang_tin.find('div',class_='detail-content')
# ps = i.find_all('p')
# # for p in ps:
# #     print(p.get_text())
print(timtrang.get_text().strip())