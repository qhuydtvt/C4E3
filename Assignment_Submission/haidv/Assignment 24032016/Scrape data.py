import requests
from bs4 import BeautifulSoup
url_to_scrape="http://vnexpress.net/"
r=requests.get(url_to_scrape)
soup = BeautifulSoup(r.text,"html.parser")
a=soup.find_all("div",id="box_news_top")
for b in a:
    i=b.find_all("div","box_sub_hot_news")
    for k in i:
        z=k.find_all("a","txt_link")
        for m in z:
            if len(m.text)>0:
                t=m.text.strip()
                print(t)