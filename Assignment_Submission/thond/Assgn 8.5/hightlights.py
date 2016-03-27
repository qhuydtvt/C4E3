from bs4 import BeautifulSoup
##import webbrowser
##import time
##import datetime

##now = time.ctime()
##print(now)
file = open("vnex.html","rb")
web = file.read()
web_string = web.decode("utf-8")

soup = BeautifulSoup(web_string, "html.parser")

hl = soup.find_all("div", id = "box_news_top")
for i in hl:
    for n in i.find_all("div", {"class":"scroll-pane"}):
        for m in n.find_all("a", "txt_link"):
            print(m.contents[0])

    
    
        


