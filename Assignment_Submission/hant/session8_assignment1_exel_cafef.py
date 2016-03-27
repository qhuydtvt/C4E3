
from bs4 import BeautifulSoup
import xlwt

class DataRow:
    def __init__(self, t, n):
        self.title = t
        self.numbers = n
    def print(self):
        print(self.title)
        print(self.numbers)

file = open("scafef.html", "rb")

web_content = file.read()

soup = BeautifulSoup(web_content.decode("utf-8"), "html.parser")

table_content = soup.find("table", id="tableContent")
table_body = table_content.find("tbody")

trs = table_body.find_all("tr", recursive=False)

data_rows = []

for tr in trs:
    tds = tr.find_all("td", recursive=False)

    title = str(tds[0].contents[0]).strip()
    numbers = [tds[i].contents[0] for i in range(1, len(tds) - 1) if len(tds[i].contents) > 0]

    data_row = DataRow(title, numbers)
    data_rows.append(data_row)

for data_row in data_rows:
    data_row.print()


wb = xlwt.Workbook()

ws = wb.add_sheet('scafef')

for i in range(0,len(data_rows)):
    ws.write(i,0,data_rows[i].title)
    for j in range(len(data_rows[i].numbers)):
        ws.write(i,j+1,data_rows[i].numbers[j])

wb.save('scafef_ass8.xls')