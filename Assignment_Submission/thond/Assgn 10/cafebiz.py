import requests
from bs4 import BeautifulSoup
import re

cafebiz = requests.get("http://cafebiz.vn/")

web_cafebiz = BeautifulSoup(cafebiz.content, "html.parser")
list_home = web_cafebiz.find("div", attrs = {'class':'list_home'})
details = list_home.find_all("li")
idx = 1
for a in details:
    print(idx)
    image = print(a.find("img"))
    title = print(a.h3.a.string)
    time = print(a.find("span", attrs = {'class':'time'}).contents[0])
    print()
    idx += 1
print('----------------------------------------------------------------------------')
