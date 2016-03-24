from bs4 import BeautifulSoup

file = open("VnExpress.html","rb")

web= file.read()
web_string= web.decode("utf-8")

soup = BeautifulSoup(web_string,"html.parser")

hot_news= soup.find("div","box_sub_hot_news")
ul= hot_news.find("ul")

news= ul.find_all("a","txt_link")

print("Hot New trên VnExpress lúc 21 giờ ngày 23/03/2016")
i=1
for n in news:
    print(str.format("{0}. {1}",i,n["title"]))
    i=i+1