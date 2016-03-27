__author__ = 'MS MINH'

from bs4 import BeautifulSoup
file = open("scafef.html", "rb")

web = file.read()
web_content = web.decode("utf-8")
soup = BeautifulSoup(web_content, "html.parser")

table_content = soup.find("table", id = "tableContent")
table_body = table_content.find("tbody")
trs = table_body.find_all("tr", recursive = False)

class DataRow:
    def __init__(self, t, n):
        self.title = t
        self.numbers = n
    def print(self):
        print("Title:", self.title)
        print("Numbers:", self.numbers)
data_rows = []

for tr in trs:
    tds = tr.find_all("td", recursive = False)

    title = (tds[0].contents[0]).strip()
    numbers = [tds[i].contents[0]
               for i in range(1, len(tds) - 1)
               if len(tds[i].contents) > 0]

    data_row = DataRow(title, numbers)
    data_rows.append(data_row)

for data_row in data_rows:
    data_row.print()
    print("-----------------------------")

import xlwt

wb = xlwt.Workbook()

ws = wb.add_sheet("scafef")

for i in range(len(data_rows)):
    ws.write(i, 0, data_rows[i].title)
    for j in range(len(data_rows[i].numbers)):
        ws.write(i, j + 1, data_rows[i].numbers[j])

wb.save("scafef.xls")
