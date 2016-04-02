import requests
from bs4 import BeautifulSoup
import re

tinhte = requests.get("https://tinhte.vn/")
trangweb_tinhte = BeautifulSoup(tinhte.content, "html.parser")

def take_only_text(href):
    return href and not re.compile("#").search(href)

#find
menu_bar= trangweb_tinhte.find("ul",class_="publicTabs navLeft")
result = menu_bar.find_all("a", attrs={"href": take_only_text, "class": "navLink"})
for x in result:
    print(x.string)
