from bs4 import BeautifulSoup

file= open("scafef.html","rb")
web=file.read()
web_string=web.decode("utf-8")

soup= BeautifulSoup(web_string,"html.parser")




table=soup.find("table",id="tableContent")

tr_list=table.find_all("tr")
for tr in tr_list:
    td_list=tr.find_all("td")
    hang=""
    for td in td_list:
        if td.text!="":
            hang=hang+td.text.strip()+" | "
    print(hang)
