import requests

tinhte = requests.get("https://tinhte.vn/")
#print(tinhe)
# print(tinhte.content)
#
# file_name ="tinhte.html"
# file_html = open(file_name,"wb")
# file_html.write(tinhte.content)
# file_html.close()

from bs4 import BeautifulSoup
import re
trangweb_tinhte= BeautifulSoup(tinhte.content,"html.parser")
#print(trangweb_tinhte.get_text())

menu_bar= trangweb_tinhte.find("ul",class_="publicTabs navLeft")
#print(menu_bar)

# nav_link= menu_bar.find_all("a",attrs="navLink")
# datas=nav_link
# for data in datas:
#     #print(data)
#     if data.string!=None:
#         continue
#     print(data.string)
#     #print(data.get_text())
#
# #print(datas)

footer_bar=trangweb_tinhte.find("li",attrs={"class":"bigFooterCol bigFooterCol--col1"})
# datas=footer_bar.find_all("li")
# for data in datas:
#     print(data.get_text())
# footer_target=footer_bar.div.ul
# print(footer_target)

#result= footer_bar.find(content=re.compile("quangcao"))
#print(result)

def menu_without_ad(href):
    return href and not re.compile("quangcao").search(href)

# result= footer_bar.find_all(href= menu_without_ad)
# for ketqua in result:
#     print(ketqua)

#tim noi dung dung co cafe
result= footer_bar.find_all(string= re.compile("Cafe"))
for ketqua in result:
    print(ketqua)


