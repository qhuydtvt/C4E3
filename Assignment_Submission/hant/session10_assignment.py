from flask import Flask,render_template

app = Flask(__name__)

class movie:
    def __init__(self,n,img):
        self.name = n
        self.image = img

Movies = [
    movie('Into The Wild',
                'https://i.ytimg.com/vi/pofkWsxzUOI/maxresdefault.jpg'),
    movie('The social network',
                'http://cdn.collider.com/wp-content/uploads/The-Social-Network-movie-poster-David-Fincher.jpg'),
    movie('Inception',
                'http://static2.businessinsider.com/image/5537c43b6da8118d4484b11b-842-421/inception-top-spinning-rotation-2.png'),
    movie('Howls Moving Castle',
                'http://images.posterjunction.com/Howl-s-Moving-Castle-movie-poster-1020273575.jpg'),
    movie('Tekkonkinkreet',
                'https://letsfallasleep.files.wordpress.com/2008/10/tekkonkinkreetpole.jpg'),
    movie('Coraline',
                'http://www.stephenjoneseditor.com/covers/coraline-hc.jpg')

]

@app.route('/')
def hi():
    return('ha')


@app.route('/movie/<movie_idx>')
def movie(movie_idx):
    for i in range(0,len(Movies)):
        if int(movie_idx) == i:
            return render_template('movie.html',
                                    Title=Movies[i].name,
                                    img = Movies[i].image)


if __name__ == '__main__':
    app.run()