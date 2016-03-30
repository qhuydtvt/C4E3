from flask import Flask,render_template

app = Flask(__name__)

class Movie:
    def __init__(self,title,img):
        self.title= title
        self.img= img

movie_list=[
 Movie("Jessica Jones","http://www.chicagonow.com/matthew-milams-films-and-music/files/2015/11/Marvels-Jessica-Jones.jpg"),
 Movie("Deadpool","http://s3.foxfilm.com/foxmovies/production/films/103/images/feature/deadpool-film-header-now-playing-front-main-stage.jpg"),
 Movie("The Legend of Korra","http://cdn01.wallconvert.com/_media/wallpapers_1920x1080/1/2/korra-avatar-the-legend-of-korra-14458.png"),
 Movie("Revolutionary Girl Utena","http://i9.photobucket.com/albums/a94/leeness/utena-DVD-1-preview.png"),
 Movie("Person of Interest","http://images5.fanpop.com/image/photos/31600000/Person-of-Interest-person-of-interest-31667427-1680-1050.png"),]

@app.route('/')
def hello_world():
    return 'Hello C4E3!'

@app.route("/movie/<movie_idx>")
def movie(movie_idx):
    i=int(movie_idx)
    return render_template("hero.html",title=movie_list[i].title,img=movie_list[i].img)

if __name__ == '__main__':
    app.run()