__author__ = 'MS MINH'

###Scrape list_home
from bs4 import BeautifulSoup
file = open("cafebiz.html", "rb")
web = file.read()
web_content = web.decode("utf-8")
soup = BeautifulSoup(web_content, "html.parser")

list_home = soup.find("div", class_="list_home")
ul = list_home.find("ul")
lis = ul.find_all("li")

class DataRow:
    def __init__(self, t, d, l, img):
        self.title = t
        self.date = d
        self.link = l
        self.image = img
    def print(self):
        print("Title:", self.title)
        print("Date:", self.date)
        print("Link:", self.link)
        print("Image:", self.image)

data_rows = []

for li in lis:
    a = li.find("a")
    title = a["title"]
    link = a["href"]
    # print(title)
    # print(link)

    # h3 = li.find("h3")
    # cont0 = h3.find("a")
    # title = cont0.string
    # print(title)

    p = li.find("p", class_="cate")
    cont1 = p.find("span")
    date = cont1.string
    # print(date)

    image = li.find("img")
    # print(image)

    data_row = DataRow(title, date, link, image)
    data_rows.append(data_row)

for data_row in data_rows:
    data_row.print()
    print("----------------------------")


### Xuất ra Excel
import xlwt
wb = xlwt.Workbook()
ws = wb.add_sheet("Trang 1")

for i in range(len(data_rows)):
        ws.write(i, 0, data_rows[i].title)
        ws.write(i, 1, data_rows[i].date)
        ws.write(i, 2, data_rows[i].link)
        ws.write(i, 3, str(data_rows[i].image))

wb.save("cafebiz.xls")












