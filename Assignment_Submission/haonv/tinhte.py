from bs4 import BeautifulSoup
import requests
tinhte = requests.get("https://tinhte.vn/")
# print(tinhte)
from bs4 import BeautifulSoup
trangweb_tinhte = BeautifulSoup(tinhte.content,"html.parser")


# tìm các biến cục bộ trong big footer
bigfooter = trangweb_tinhte.find("ul",attrs={"class":"bigFooterRow bigFooterRow--mainRow bigFooterRow--has4Columns"})
print(type(bigfooter))
#print(bigfooter)

#  chỉ tới ul
footer_target =bigfooter.li.div.ul
#print(footer_target)

# chỏ tới lớp con của footer_tager
for child in footer_target.children:
    print(child.string.strip())