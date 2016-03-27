from bs4 import BeautifulSoup

file = open ("scafef.html", "rb") #r = read b = binary
web = file.read ()
web_string = web.decode("utf-8") #decode TV

soup = BeautifulSoup(web_string, "html.parser")

taco = soup.find("table", id = "tableContent")
tab = taco.find("tbody")
tr = tab.find_all("tr")
for i in tr:
    for td in i.find_all("td", "b_r_c"):
        t = td.get_text().strip()
        if len(t) != 0:
            print(t, end = "| ")
    print()
