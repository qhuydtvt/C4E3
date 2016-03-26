from bs4 import BeautifulSoup
import xlwt
import urllib.request

url1 = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2015/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"
wp = urllib.request.urlopen(url1)
html = wp.read()
html_string= html.decode("utf-8")

class DataRow:
    def __init__(self, t, n):
        self.title = t
        self.numbers = n
    def tprint(self):
        print(self.title)
    def nprint(self):
        print(self.numbers)

soup = BeautifulSoup(html_string, "html.parser")

table_content = soup.find("table", id="tableContent")
# table_body = table_content.find("tbody")

trs = table_content.find_all("tr", recursive = False)
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
#     data_row.tprint()
#     data_row.nprint()
#     print("-----------------------------")

wb = xlwt.Workbook()
ws = wb.add_sheet("scafef")
i = 0
while i in range(len(data_rows)):
    ws.write(i, 0, data_rows[i].title)
    for j in range(len(data_rows[i].numbers)):
         ws.write(i,j+1,data_rows[i].numbers[j])
    i += 1
wb.save("scafef.xls")

