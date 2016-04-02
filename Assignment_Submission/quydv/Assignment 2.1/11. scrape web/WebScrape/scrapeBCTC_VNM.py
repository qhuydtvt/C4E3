from bs4 import BeautifulSoup
import urllib.request
import xlwt
wb = xlwt.Workbook()
ws = wb.add_sheet("BCTC VNM")

url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2015/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"

web_page = urllib.request.urlopen(url)
html = web_page.read()
html_string = html.decode("utf-8")

soup = BeautifulSoup(html_string, "html.parser")

table = soup.find(id="tableContent")

class Data_rows:
    def __init__(self, title, numbers):
        self.title = title
        self.numbers = numbers

    def print(self):
        print("Title:", self.title)
        print("Numbers:", self.numbers)

data_rows = []

trs = table.find_all("tr")
for tr in trs:
    tds = tr.find_all("td", "b_r_c")
    if len(tds) > 0:
        title = tds[0].contents[0].strip()
        # print(title)
        numbers = [tds[idx].contents[0]
               for idx in range(1, len(tds) - 1)
               if len(tds[idx]) > 0]
        data_row = Data_rows(title, numbers)
        data_rows.append(data_row)


ws = wb.get_sheet(0)

for i in range(len(data_rows)):
    ws.write(i, 0, data_rows[i].title)
    for k in range(len(data_rows[i].numbers)):
        ws.write(i, k + 1, data_rows[i].numbers[k])

wb.save("scafef.xls")

