import requests
from bs4 import BeautifulSoup
import xlwt

#Tạo class để ưu thông tin xuất ra được từ web vào các object
class DataRow:
    def __init__(self, title, date, href , image_link):
        self.title = title
        self.date = date
        self.href = href
        self.image_link = image_link

    def print(self):
        print("Title:", self.title)
        print("Date:", self.date)
        print("Link to content:", self.href)
        print("Link to image:", self.image_link)

data_rows = []

#Truy cập vào cafebiz và đọc bằng BeautifulSoup
cafebiz = requests.get("http://cafebiz.vn/")
cafebiz.html = BeautifulSoup(cafebiz.content, "html.parser")

#Lấy dữ liệu bằng crawling kết hợp walking
cafebiz.list_home = cafebiz.html.find("div", attrs={"class": "list_home"})
titles = cafebiz.list_home.find_all("li")
for t in titles:
    title = t.h3.a.string.strip()
    date = t.p.span.string
    if t.a.img == None:
        continue
    img_link = t.a.img["src"]
    href = "http://cafebiz.vn" + t.a["href"]
    data_row = DataRow(title, date, href, img_link)
    data_rows.append(data_row)

#In dữ liệu ra console
for data_row in data_rows:
    print("#" + str(data_rows.index(data_row) + 1))
    data_row.print()
    print("------------")

#Ghi dữ liệu vào excel
wb = xlwt.Workbook()
ws = wb.add_sheet("List home Cafebiz")

for data_row in data_rows:
    ws.write(data_rows.index(data_row) + 1, 0, str(data_rows.index(data_row)) + ". " + data_row.title)
    ws.write(data_rows.index(data_row) + 1, 1, data_row.date)
    ws.write(data_rows.index(data_row) + 1, 2, data_row.href)
    ws.write(data_rows.index(data_row) + 1, 3, data_row.image_link)

wb.save("Cafebiz.xls")

#Lấy dữ liệu của bài báo theo số thứ tự
def get_content(title_number):
    cafebiz_recruit = requests.get(data_rows[title_number - 1].href)
    cafebiz_recruit_html = BeautifulSoup(cafebiz_recruit.content, "html.parser")
    cafebiz_recruit_content = cafebiz_recruit_html.find("div", attrs={"class": "detail-content"})
    print("Nội dung bài báo", "\"" + data_rows[title_number - 1].title + "\"" + ":\n")
    print(cafebiz_recruit_content.get_text().strip())

get_content(1)