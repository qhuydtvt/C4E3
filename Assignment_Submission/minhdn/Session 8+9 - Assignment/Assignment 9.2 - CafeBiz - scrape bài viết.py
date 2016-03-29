__author__ = 'MS MINH'

from bs4 import BeautifulSoup
file = open("cafebiz tuyen cay viet.html", "rb")
web = file.read()
web_content = web.decode("utf-8")
soup = BeautifulSoup(web_content, "html.parser")

cont = soup.find("div", class_= "content")
title = cont.find("h1").string
print(title)

h2 = cont.find("h2").string
print(h2)

image = cont.find("img")
print(image)

detail_content = cont.find("div", class_="detail-content").get_text()
print(detail_content)

# ps = detail_content.find_all("p")
#
# for p in ps:
#     try:
#         if p.string == None:
#             strong = p.find("strong").string
#             span = p.find("span").string
#             print(strong, span)
#         else:
#             print(p.string)
#     except AttributeError:
#         continue




