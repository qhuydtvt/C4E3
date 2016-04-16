from flask import Flask, render_template

app = Flask(__name__)

class Movie:
    def __init__(self, title, img, link):
        self.title = title
        self.img = img
        self.link = link

movies = [
    Movie("Batman",
          "http://www.studiocity-macau.com/uploads/images/SC/Entertainment/Batman/batman_share.jpg",
          "https://www.google.com/"),
    Movie("Superman",
          "http://pixel.nymag.com/imgs/daily/vulture/2013/07/24/24-manofsteel-batman.w529.h352.jpg",
          "https://www.youtube.com/"),
    Movie("Deadpool",
          "https://thenypost.files.wordpress.com/2016/02/deadpool_poster2a.jpg?quality=100&strip=all&strip=all",
          "https://www.facebook.com/")
]

# @app.route('/hero/<hero_name>')
# def hero(hero_name):
#     if str(hero_name) == 'superman':
#         return render_template("hero.html", title = 'superman', img = 'http://pixel.nymag.com/imgs/daily/vulture/2013/07/24/24-manofsteel-batman.w529.h352.jpg')
#
#     if str(hero_name) == 'batman':
#         return render_template("hero.html", title = 'batman', img = 'http://www.studiocity-macau.com/uploads/images/SC/Entertainment/Batman/batman_share.jpg')
#     return "Not found"
    # return 'Title: ' + movie0.title + ' ' + 'Img: ' + movie0.img

@app.route('/movie_1/<movie_idx>')
def get_movie_by_idx(movie_idx):
    index = int(movie_idx)
    if index in range(len(movies)):
        return render_template("hero1.html", title = movies[index].title, img = movies[index].img)
    else:
        return "Not found"
    

@app.route('/movie_2/<movie_idx>')
def get_movie_by_idx_2(movie_idx):
    index = int(movie_idx)
    if index in range(len(movies)):
        return render_template("hero2.html", movie=movies[index])
    else:
        return "Not found"

@app.route('/movies')
def get_movies():
    return render_template("heroes.html", movie_list=movies)


if __name__ == '__main__':
    app.run()