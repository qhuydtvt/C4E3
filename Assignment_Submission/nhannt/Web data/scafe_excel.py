from bs4 import BeautifulSoup


class DataRow:
    def __init__(self, t, n):
        self.title = t
        self.numbers = n
    def print(self):
        print("Title", self.title)
        print("Numbers", self.numbers)

file = open("scafe.html", "rb") #rb = read binary
web = file.read()
web_string = web.decode("utf-8") #decode Tieng Viet

soup = BeautifulSoup(web_string, "html.parser")

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


# for data_row in data_rows:
#     data_row.print()
#     print("-----------------------------")

import xlwt


wb = xlwt.Workbook()

ws = wb.add_sheet("scafef")
i=0
for e in data_rows:
   while i < len(data_rows):
       ws.write(i,0, e.title)
       j = 0
       while j<len(e.numbers):
           ws.write(i,j+1,e.numbers[j])
           j=j+1

       i=i+1
       break


wb.save("scafef.xls")

