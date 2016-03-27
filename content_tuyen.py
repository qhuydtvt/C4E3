from bs4 import BeautifulSoup
import bs4
import requests
biz_content = requests.get("http://cafebiz.vn/cau-chuyen-kinh-doanh/cafebiz-tuyen-cay-viet-bien-tap-vien-xay-dung-noi-dung-20160309143036239.chn/")
dep_mama = BeautifulSoup(biz_content.content,"html.parser")
divv = dep_mama.find("div",attrs={'id':'mainDetail','class':'content' })
print(divv.get_text())