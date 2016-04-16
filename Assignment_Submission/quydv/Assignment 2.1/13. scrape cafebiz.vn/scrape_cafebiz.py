import requests
from bs4 import BeautifulSoup
import xlwt

#Tạo class để ưu thông tin xuất ra được từ web vào các object
class Post:
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

posts = []

#Truy cập vào cafebiz và đọc bằng BeautifulSoup
cafebiz = requests.get("http://cafebiz.vn/")
cafebiz_html = BeautifulSoup(cafebiz.content, "html.parser")

#Lấy dữ liệu bằng crawling kết hợp walking
cafebiz_list_home = cafebiz_html.find("div", attrs={"class": "list_home"})
titles = cafebiz_list_home.find_all("li")
for t in titles:
    title = t.h3.a.string.strip()
    date = t.p.span.string
    if t.a.img == None:
        continue
    img_link = t.a.img["src"]
    href = "http://cafebiz.vn" + t.a["href"]
    post = Post(title, date, href, img_link)
    posts.append(post)

#In dữ liệu ra console
# for post in posts:
    # print("#" + str(posts.index(post) + 1))
    # post.print()
    # print("------------")

# #Ghi dữ liệu vào excel
# wb = xlwt.Workbook()
# ws = wb.add_sheet("List home Cafebiz")
#
# for post in posts:
#     ws.write(posts.index(post) + 1, 0, str(posts.index(post)) + ". " + post.title)
#     ws.write(posts.index(post) + 1, 1, post.date)
#     ws.write(posts.index(post) + 1, 2, post.href)
#     ws.write(posts.index(post) + 1, 3, post.image_link)
#
# wb.save("Cafebiz.xls")

#Lấy dữ liệu của bài báo theo số thứ tự
def get_content(title_number):
    cafebiz_recruit = requests.get(posts[title_number - 1].href)
    cafebiz_recruit_html = BeautifulSoup(cafebiz_recruit.content, "html.parser")
    cafebiz_recruit_content = cafebiz_recruit_html.find("div", attrs={"class": "detail-content"})
    print("Nội dung bài báo", "\"" + posts[title_number - 1].title + "\"" + ":\n")
    print(cafebiz_recruit_content.get_text().strip())

# get_content(1)

#Lấy post ra bằng keyword
def get_content_by_keyword(keyword):
    for post in posts:
        if str(keyword) in post.title:
            post.print()
            post_get = requests.get(post.href)
            post_get_html = BeautifulSoup(post_get.content, "html.parser")
            post_content = post_get_html.find("div", attrs={"class": "detail-content"})
            # print("\nNội dung bài báo", "\"" + post.title + "\"" + ":\n")
            print("\n" + post_content.get_text().strip())
            print("---------------")

get_content_by_keyword("Google")

