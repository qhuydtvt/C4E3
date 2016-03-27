from bs4 import BeautifulSoup

file = open("vnexpress.html","rb")

web= file.read()
web_string= web.decode("utf-8")


soup= BeautifulSoup(web_string,"html.parser")

box_sub_hot_news= soup.find("div","box_sub_hot_news")
ul= box_sub_hot_news.find("ul")

li_list= ul.find_all("a","txt_link")

print("Hot New trên Vnexpress lúc 11 giờ ngày 23/03/2016")
i=0
for li in li_list:
    i=i+1
    print(str.format("{0}. {1}",i,li["title"]))




#print(li_list)


