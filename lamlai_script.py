from bs4 import BeautifulSoup
import bs4
import xlwt
import urllib.request
url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2015/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam"
webpage = urllib.request.urlopen(url)

wb = xlwt.Workbook()
ws = wb.add_sheet("scafef")
#web = open("scafef.html", "rb")
file = webpage.read()
web_string = file.decode("utf-8")
soup = BeautifulSoup(web_string, "html.parser")
class Datarow:
    def __init__(self,tittle,number):
        self.Tittle= tittle
        self.number=number
    def inu(self):
        print("Tittle:",self.Tittle)
        print("Number:",self.number)
table_content = soup.find("table", id="tableContent")
tbody_con = table_content.find("tbody")
trs = tbody_con.find_all("tr",recursive = False)
datarows=[]
for tr in trs:
    tds = tr.find_all("td",recursive =False)
    Tittle = tds[0].contents[0].strip()
    number = [ tds[i].contents[0]
                for i in range(1,len(tds)-1)
                if len(tds[i].contents) > 0
             ]
    datarow = Datarow(Tittle,number)
    datarows.append(datarow)
for datarow in datarows:
    datarow.inu()
    print("-----------------")

a=0
j=0
while a<len(datarows):
    ws.write(a,0,datarows[a].Tittle)
    while j < len(number):
        ws.write(a,j+1,datarow[a].number[j])
        a=a+1
        j=j+1
        continue
wb.save("mama.xls")