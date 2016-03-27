

from bs4 import BeautifulSoup

file = open("Vnexpress.htm", "rb") #rb = read binary
web = file.read()
web_string = web.decode("utf-8") #decode Tieng Viet

soup = BeautifulSoup(web_string, "html.parser")

Vnexpress = soup.find("div", tabindex="5002")
for title in Vnexpress.find_all("a"):
    for i in title:
        print(i)
