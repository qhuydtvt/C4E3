from bs4 import BeautifulSoup

file = open("scafe.html", "rb") #rb = read binary
web = file.read()
web_string = web.decode("utf-8") #decode Tieng Viet

soup = BeautifulSoup(web_string, "html.parser")

scafe = soup.find("table", id ="tableContent")
tr_list = scafe.find_all("tr")
print(tr_list)
for i in tr_list:
   d=i.find_all("td")
   print(d.contents)
   print("--------------------")


