from bs4 import BeautifulSoup

file = open("scafef.html", "rb") # r = read, b = binary
web = file.read()
web_string = web.decode("utf-8") #decode Tieng Viet

soup = BeautifulSoup(web_string, "html.parser")

table = soup.find("table", id = "tableContent")
trs = table.find_all("tr")
for tr in trs:
    tds_row = tr.find_all("td", "b_r_c")
    for td in tds_row:
        if len(td) > 0:
            print(td.contents[0])
