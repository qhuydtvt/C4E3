from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup
from mongoengine import *

class Article:
    def __init__(self, title, author, image, content):
        self.title = title
        self.author = author
        self.image = image
        self.content = content

#Truy cập tinhte.vn bằng BeautifulSoup
get_webpage = requests.get("https://tinhte.vn/")
get_webpage_html = BeautifulSoup(get_webpage.content, "html.parser")

#Scrape tinhte.vn
article_box = get_webpage_html.find("div", attrs={"id": "WidgetPageContents"})
article_list = article_box.find_all("div", attrs={"class": "section sectionMain recentNews"})

list_of_article = []

for article in article_list:
    title = article.div.h2.a.get_text()
    author = article.div.div.div.span.a.get_text()
    img = article.img["src"]
    find_contents = article.find_all("div", attrs={"class": "newsText"})
    for content in find_contents:
        article_content = content.get_text().strip()
    post = Article(title, author, img, article_content)
    list_of_article.append(post)

#connect MongoDB
connect('c4e3_movie_db',host='mongodb://c4e3:CodeTheChange@ds015879.mlab.com:15879/c4e3_movie_db')

class Quy(Document):
    title = StringField()
    author = StringField()
    image = StringField()
    content = StringField()

# for article in list_of_article:
#     article_object = Quy(title = article.title,
#                               author = article.author,
#                               image = article.image,
#                               content = article.content)
#     article_object.save()

mongo_list_of_article = Quy.objects()


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/index')
def index():
    return render_template("index.html",
                           list_of_article = mongo_list_of_article)

if __name__ == '__main__':
    app.run()
