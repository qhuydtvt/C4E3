from flask import Flask,render_template
from mongoengine import*

connect('c4e3',host='mongodb://admin:admin@ds015919.mlab.com:15919/c4e3')

app = Flask(__name__)

class Movie(Document):

    title = StringField()
    img = StringField()

movie_list = Movie.objects

@app.route('/')
def welcome():
    return "ha"

@app.route('/movies')
def movies():
    return render_template('heroes.html',movies=movie_list)



if __name__ == '__main__':
    app.run()