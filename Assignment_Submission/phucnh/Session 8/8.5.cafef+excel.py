from bs4 import BeautifulSoup
import urllib.request

class DataRow:
    def __init__(self, t, n):
        self.title = t
        self.numbers = n
    def print(self):
        print("Title", self.title)
        print("Numbers", self.numbers)

url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2015/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"

webpage = urllib.request.urlopen(url)

html = webpage.read()

html_string = html.decode("utf-8")

soup= BeautifulSoup(html_string,"html.parser")

table=soup.find("table",id="tableContent")

data_rows = []

tr_list= table.find_all("tr", recursive=False)
for tr in tr_list:
    tds = tr.find_all("td", recursive=False)

    title = str(tds[0].contents[0]).strip()
    numbers = [tds[i].contents[0]               # What to get
               for i in range(1, len(tds) - 1)  # Loop
               if (len(tds[i].contents) > 0)]     # Filter

    data_row = DataRow(title, numbers)
    data_rows.append(data_row)


import xlwt

wb = xlwt.Workbook() #Create workbook object
ws = wb.add_sheet('cafef.xls')

for i in range(0,len(data_rows)):
    #data_row.print()
    #print(data_rows[i].title)
    ws.write(i, 0,data_rows[i].title)
    number=data_rows[i].numbers
    for j in range(0,len(number)):
        if (number!=[]):
            ws.write(i,j+1,number[j])
    #print("-----------------------------")

#for i in range(0,len(data_rows)):

    # ws.write(i, 0,data_rows[i].title)
    # for j in range(0,len(data_rows[i].numbers)):
    #     ws.write(i,j+1,data_rows[i].numbers[j+1])

wb.save('example.xls')