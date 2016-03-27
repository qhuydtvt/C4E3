from bs4 import BeautifulSoup

file= open("scafef.html","rb")
web=file.read()
web_string=web.decode("utf-8")

soup= BeautifulSoup(web_string,"html.parser")

table=soup.find(id="tableContent")

tr_list=table.find_all("tr")
for tr in tr_list:
    td_list=tr.find_all("td")
    i=""
    for td in td_list:
        if td.text != "":
            i=i+td.text + "   "
    print(i)