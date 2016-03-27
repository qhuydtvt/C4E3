__author__ = 'MS MINH'

from bs4 import BeautifulSoup
file = open("VnExpress.html", "rb")
web = file.read()
web_string = web.decode("utf-8")
soup = BeautifulSoup(web_string, "html.parser")

box = soup.find("div", "box_sub_hot_news")
# ul = box.find("ul")
lis = box.find_all("li")
news = []
for li in lis:
    txt = li.find("a", "txt_link")
    news.append(txt["title"])

i = 1
for new in news:
    print(str.format("{0} - {1}", i, new))
    i += 1







