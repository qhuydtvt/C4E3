from flask import Flask, render_template

app = Flask(__name__)

class Movie:
    def __init__(self, title, img):
        self.title = title
        self.img = img

movies = [
    Movie("Batman", "http://www.studiocity-macau.com/uploads/images/SC/Entertainment/Batman/batman_share.jpg"),
    Movie("Superman", "https://assets3.thrillist.com/v1/image/1244108/size/tl-horizontal_main/batman-superman-and-your-other-childhood-heroes-now-morbidly-obese"),
    Movie("Captain America: Civil War", "http://i.imgur.com/Pl9rAQy.jpg"),
    Movie("Godfather 1", "http://stat.homeshop18.com/homeshop18/images/productImages/351/marlon-brando-is-the-godfather-movie-poster-medium-pp31464-large_fe79f501c74afd38d13ab3ecff26f63a.jpg"),
    Movie("Godfather 2", "http://img.goldposter.com/2015/04/The-Godfather-Part-II_poster_goldposter_com_21.jpg"),
    Movie("V for Vendetta", "http://www.masculinity-movies.com/wp-content/uploads/2012/02/v-for-vendetta-2005.jpg")
]

@app.route("/movie/<movie_number>")
def superhero(movie_number):
    idx = int(movie_number)
    if idx in range(len(movies)):
        return render_template("movie.html",
                               title = movies[idx].title,
                               img = movies[idx].img)
    return "Not found"

if __name__ == '__main__':
    app.run()