from flask import Flask, render_template

app = Flask(__name__)

class Movie:
    def __init__(self, title, img):
        self.title = title
        self.img = img

movies = [
    Movie("Batman", "http://www.studiocity-macau.com/uploads/images/SC/Entertainment/Batman/batman_share.jpg"),
    Movie("Superman", "https://assets3.thrillist.com/v1/image/1244108/size/tl-horizontal_main/batman-superman-and-your-other-childhood-heroes-now-morbidly-obese"),
    Movie("Running man", "https://www.dramafever.com/st/img/nowplay/3970_gongyoo_RunningMan_Nowplay_Small.jpg"),
    Movie("Dad", "https://moonml03.files.wordpress.com/2013/05/9.jpg"),

]
@app.route('/')
def hello_world():
   return 'Hello World!'
@app.route("/movie/<movie_number>")
def superhero(movie_number):
    idx = int(movie_number)
    if idx in range(len(movies)):
        return render_template("hero.html",
                               title = movies[idx].title,
                               img = movies[idx].img)
    return "Not found"

if __name__ == '__main__':
    app.run()