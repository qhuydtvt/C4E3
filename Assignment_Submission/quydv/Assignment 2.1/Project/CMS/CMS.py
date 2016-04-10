from flask import Flask, render_template
from mongoengine import *

#Upload data to Mongo
# connect("cmslectures","mongodb://<dbuser>:<dbpassword>@ds019990.mlab.com:19990/cmslectures")
#
class Lecture:
    def __init__(self, href, title, brief, document, assignment):
        self.href = href
        self.title = title
        self.brief = brief
        self.document = document
        self.assignment = assignment
#
lecture1 = Lecture("lecture-1",
                   "Lecture 1: Introduction to Python",
                   ["Python is easy to learn.",
                   "Python is good."],
                   [{"name": "slide1.pptx",
                     "link": "http://google.com"},
                    {"name": "document1.pdf",
                     "link": "http://youtube.com"}],
                   [{"name": "Handout 01",
                     "link": ""},
                    {"name": "Assignment 01",
                     "link": "http://bongda.com.vn"}])

lecture2 = Lecture("lecture-2",
                   "Lecture 2: List and Dictionary",
                   ["List is easy to learn.",
                   "Dictionary is good."],
                   [{"name": "slide2.pptx",
                     "link": "http://google.com"},
                    {"name": "document2.pdf",
                     "link": "http://youtube.com"}],
                   [{"name": "Handout 02",
                     "link": ""},
                    {"name": "Assignment 02",
                     "link": "http://bongda.com.vn"}])

# class CMSLecture(Document):
#     href = StringField()
#     title = StringField()
#     brief


lecture_list = [lecture1, lecture2]

app = Flask(__name__)

#Lay anh tai local host:
@app.route('/<path:path>')
def static_file(path):
    return app.send_static_file(path)

@app.route('/')
def home():
    return render_template("Index.html",
                           lecture_list = lecture_list)


@app.route('/<lectureHref>')
def lectureHref(lectureHref):
    for lecture in lecture_list:
        if lecture.href == lectureHref:
            return render_template("lecture.html",
                                   lecture = lecture,
                                   lecture_list = lecture_list)

if __name__ == '__main__':
    app.run()
