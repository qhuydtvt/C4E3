from bs4 import BeautifulSoup
import requests
import re

class Posts:
    def __init__(self, t, l, tg):
        self.title = t
        self.link=l
        self.time =tg

cafebiz = requests.get("http://cafebiz.vn/")

webpage = BeautifulSoup(cafebiz._content,"html.parser")

list_home= webpage.find("div",class_="list_home")
li_list= list_home.find_all("li")

post=[]
for li in li_list:
    title= li.find("h3").get_text()
    link="http://cafebiz.vn"+li.find("h3").find("a").get('href')
    time= li.find("span",class_="time").get_text()
    post.append(Posts(title,link,time))

for i in range(28):
   print(str.format("{0}.{1}    {2}     {3}",i+1,post[i].title,post[i].time,post[i].link))

print("-----------------------------")

post_number= int(input("Bạn đọc tin số mấy: "))

print("-----------------------------")

bai = requests.get(post[post_number-1].link)
web = BeautifulSoup(bai.content,"html.parser")

print("Tiều đề:",web.find("h1",class_="title").get_text())
print("Tóm tắt",web.find("h2",class_="sapo").get_text())
print("-----------------------------")
print("Nội dung",web.find("div",class_="detail-content").get_text())