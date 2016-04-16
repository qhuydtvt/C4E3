__author__ = 'MS MINH'

from flask import Flask, render_template
from mongoengine import *

connect("c4e3", host = "mongodb://admin:admin@ds015919.mlab.com:15919/c4e3")
app = Flask(__name__)

class Movie(Document):
    title = StringField()
    img = StringField()
    # id = IntField()

movies = Movie.objects

for movie in movies:
    print(movie.title, ":", movie.img)

    # print(type(movie.title, ":", movie.img))
    # print(str.format("({0}) {1}: {2}"), movie.id, movie.title, movie.img)
