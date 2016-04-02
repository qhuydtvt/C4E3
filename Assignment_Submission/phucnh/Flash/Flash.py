from flask import Flask,render_template
from mongoengine import *

connect("c4e3",host="mongodb://admin:admin@ds015919.mlab.com:15919/c4e3")
class Movie(Document):
    title=StringField()
    img=StringField()

# movie = Movie(title="PHuc",img="http://cdn8.openculture.com/wp-content/uploads/2011/10/Superman-fleischer.jpg")
#
# movie.save()

movie_list= Movie.objects
for movie in movie_list:
    print(movie.title," :", movie.img)
app = Flask(__name__)

# class Movie:
#     def __init__(self,title,img,link):
#         self.title= title
#         self.img= img
#         self.link=link
# movie_list=[
#  Movie("Batman","http://images.newseveryday.com/data/images/full/6782/batman-vs-superman.jpeg","http://google.com"),
#  Movie("Superman","http://cdn8.openculture.com/wp-content/uploads/2011/10/Superman-fleischer.jpg","http://war.com"),
#  Movie("Panda 3","https://i.ytimg.com/vi/kR6iiYvVEYc/maxresdefault.jpg","http://war.com"),
#  Movie("Hitman","http://anh.24h.com.vn/upload/2-2014/images/2014-04-07/1396863671-hitman-2.jpg","http://war.com")]
#  #dien 5 movie


# http://cdn8.openculture.com/wp-content/uploads/2011/10/Superman-fleischer.jpg

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/sayhi')
def say_hi():
    return 'Hello C4E3- Happy coding'

@app.route('/phuc')
def say_phuc():
    return 'Hello phuc'

@app.route("/sayhi/<name>")
def say_hi_to(name):
    return "Hi "+name

@app.route("/hero/<hero_name>")
def batman(hero_name):
    if str(hero_name)== "superman":
        return render_template("hero.html",title="superman",img="http://cdn8.openculture.com/wp-content/uploads/2011/10/Superman-fleischer.jpg")
    if str(hero_name)=="batman":
        return render_template("hero.html",title="batman",img="http://images.newseveryday.com/data/images/full/6782/batman-vs-superman.jpeg")
    return "Not found"
    # return render_template("hero.html")

@app.route("/movie/<movie_idx>")
def movie(movie_idx):
    idx=int(movie_idx)
    if movie_idx in range(len(movie_list)):
        return render_template("hero.html",title=movie_list[idx].title,img=movie_list[idx].img)
    return "<h1>Movie not found</h1>"

@app.route("/movie2/<movie_idx>")
def get_movie(movie_idx):
    index=int(movie_idx)
    if index in range(len(movie_list)):
        return render_template("hero_2.html", movie=movie_list[index])
    return "<h1>Movie not found</h1>"

@app.route("/movies/")
def get_movies():
    return render_template("heroes.html", movies=movie_list)




if __name__ == '__main__':
    app.run()
