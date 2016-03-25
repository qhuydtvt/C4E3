from bs4 import BeautifulSoup

class DataRow:
    def __init__(self, t, n):
        self.title = t
        self.numbers = n
    def print(self):
        print("Title", self.title)
        print("Numbers", self.numbers)

file = open("scafef.html", "rb")

web_content = file.read()

soup = BeautifulSoup(web_content.decode("utf-8"), "html.parser")

table_content = soup.find("table", id="tableContent")
table_body = table_content.find("tbody")

trs = table_body.find_all("tr", recursive=False)

data_rows = []

for tr in trs:
    tds = tr.find_all("td", recursive=False)

    #
    #======================================================
    #tr : # tds[0]      | tds[1] |tds[2] | tds[3] |tds[4]
    #======================================================
    #tr: # 1. Doanh thu | tds[1] |tds[2] | tds[3] |tds[4]
    #======================================================

    title = str(tds[0].contents[0]).strip()
    numbers = [tds[i].contents[0]               # What to get
               for i in range(1, len(tds) - 1)  # Loop
               if len(tds[i].contents) > 0]     # Filter

    data_row = DataRow(title, numbers)
    data_rows.append(data_row)

for data_row in data_rows:
    data_row.print()
    print("-----------------------------")