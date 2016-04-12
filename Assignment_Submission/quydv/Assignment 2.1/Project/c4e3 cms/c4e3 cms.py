from mongoengine import *
from flask import *
from werkzeug.utils import *


#Upload data to Mongo
connect('nim', host='mongodb://hiep:hiepxanh@ds015929.mlab.com:15929/nim')

class lecture(Document):
    href = StringField()
    title = StringField()
    brief = ListField(StringField())
    document = ListField(DictField())
    assignment = ListField(DictField())

lecture_list = lecture.objects

app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def login():
    if request.method == "POST":
        u=request.form['username']
        p=request.form['password']
        if u=="1" and p=="1":
            return render_template("Index.html",
                                   lecture_list = lecture_list)
    return render_template('login.html')

@app.route('/<lectureHref>/')
def lectureHref(lectureHref):
    for lecture in lecture_list:
        if lecture.href == lectureHref:
            return render_template("lecture.html",
                                   lecture = lecture,
                                   lecture_list = lecture_list)

#Lay anh tai local host:
@app.route('/<path:path>/')
def static_file(path):
    return app.send_static_file(path)

@app.route('/index/')
def index():
    return render_template("Index.html",
                           lecture_list = lecture_list)


if __name__ == '__main__':
    app.run()