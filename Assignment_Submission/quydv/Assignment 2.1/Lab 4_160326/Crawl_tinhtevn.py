import requests
from bs4 import BeautifulSoup

tinhte = requests.get("https://tinhte.vn/")
# # print(tinhte)
# print(tinhte.content)
#
# file_name = "tinhte.html"
# file_html = open(file_name, "wb")
# file_html.write(tinhte.content)
# file_html.close()

trangweb_tinhte = BeautifulSoup(tinhte.content, "html.parser")
# print(trangweb_tinhte.get_text())

# menu_bar= trangweb_tinhte.find("ul",class_="publicTabs navLeft")
#
#
# nav_links = menu_bar.find_all("a", attrs={"class": "navLink"})
# for nav_link in nav_links:
#     # print(nav_link.get_text())
#     if nav_link.string == None:
#         continue
#     print(nav_link.string)
#
# print(type(menu_bar))
# print(type(nav_links))

big_footer = trangweb_tinhte.find("li", class_="bigFooterCol bigFooterCol--col1")
# footer_box = big_footer.find("ul", class_="footerMenu")
# print(footer_box.get_text())

# big_footer = big_footer.ul
# print(big_footer.get_text())

# for child in big_footer.ul.children:
#     # child.get_text()
#     # child.get("href")
#     print(child.string.strip())


