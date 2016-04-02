from flask import Flask, render_template
from mongoengine import *

connect("c4e3",host = "mongodb://admin:admin@ds015919.mlab.com:15919/c4e3")
app = Flask(__name__)


class Movie(Document):
    title = StringField()
    img = StringField()


class Movie_def:
    def __init__(self, title, img):
        self.title = title
        self.img = img


movie_list_new = Movie.objects
movies = []
for movie in movie_list_new:
    nm = Movie_def(movie.title,movie.img)
    movies.append(nm)

@app.route('/heroes/mongo')
def heroes_mongo():
    return render_template('movie3.html',
                           movie_list = movie_list_new)
    return "Movie not found"

if __name__ == '__main__':
    app.run()
