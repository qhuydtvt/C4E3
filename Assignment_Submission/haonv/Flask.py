from flask import Flask,render_template

app = Flask(__name__)

class Movie:
    def __init__(self,title,img):
        self.title= title
        self.img= img

movie_list=[
Movie(' Nam anh em sieu nhan ' ,' http://cungchoigame.biz/wp-content/uploads/2012/12/choi-game-sieu-nhan-manh-thu.jpeg '),
Movie('Pacific rim' , 'http://cdn2.denofgeek.us/sites/denofgeekus/files/pacific_rim_2.jpg '),
Movie('Begin agian ' , 'https://heliberry.files.wordpress.com/2015/09/begin-again.png '),
Movie('Pokemon ' , 'https://sickr.files.wordpress.com/2014/08/ash_and_pikachu_pokemon.png'),
Movie('Dota 2 ' , 'https://i.ytimg.com/vi/upwMN56_vDk/maxresdefault.jpg')
]


@app.route('/')
def C4e():
    return 'Xa_Lach_Boy'

@app.route("/movie/<movie_idx>")
def movie(movie_idx):
    i=int(movie_idx)
    return render_template("hero.html",title=movie_list[i].title,img=movie_list[i].img)

if __name__ == '__main__':
    app.run()