from bs4 import BeautifulSoup
import bs4
import requests
cafebiz = requests.get("http://cafebiz.vn/")
trangweb_cafebiz = BeautifulSoup(cafebiz.content, "html.parser")
###print(trangweb_cafebiz.get_text())
divv = trangweb_cafebiz.find("div", class_="list_home")
# print(divv)
link = divv.find('li',rercusive=False)
#print(link)
tim_image = link.find('img')
print(tim_image.get('src'))
tim_a = link.find('a')
print(tim_a.get('href'))
tim_h3 = link.find('h3')
print(tim_h3.get_text())
tim_p = link.find('p')
print(tim_p.get_text())
########## trang tuyen noi dung
