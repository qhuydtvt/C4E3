from flask import Flask, render_template #tai sao phai import * thi moi ra render template
from mongoengine import *

connect("c4e3", host="mongodb://admin:admin@ds015919.mlab.com:15919/c4e3")

class Movie(Document):
    title = StringField()
    img = StringField()

movie_list = Movie.objects

for movie in movie_list:
    print("id: " + str(movie.id))
    print("Title: " + movie.title + "\nLink: " + movie.img)
    print("-------------------")

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/movie_list')
def get_movie_list():
    return render_template("mongo_movie_list.html",
                           movie_list=movie_list)

@app.route('/movie_list/<movie_id>')
def get_movie_by_id(movie_id):
    for movie in movie_list:
        if str(movie.id) == movie_id:
            return render_template("get_movie_by_id.html",
                                   movie = movie)
    return "Id not found"

if __name__ == '__main__':
    app.run()
