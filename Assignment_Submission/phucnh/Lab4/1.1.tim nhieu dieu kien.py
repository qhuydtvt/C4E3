import requests

tinhte = requests.get("https://tinhte.vn/")

from bs4 import BeautifulSoup
import re
trangweb_tinhte= BeautifulSoup(tinhte.content,"html.parser")

#find
menu_bar= trangweb_tinhte.find("ul",class_="publicTabs navLeft")

def take_only_text(href):
    return href and not re.compile("#").search(href)

result = menu_bar.find_all("a",attrs={"href":take_only_text,"class":"navLink"})
for x in result:
    print(x.string)