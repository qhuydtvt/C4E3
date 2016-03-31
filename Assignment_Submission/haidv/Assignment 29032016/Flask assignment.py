from flask import Flask,render_template

app = Flask(__name__)

class movie:
    def __init__(self,title,img):
        self.title=title
        self.img=img
movie0=[movie("panda3","https://resizing.flixster.com/4f74T5YJSw9ikpRsIUxUtcR1X9A=/180x267/v1.bTsxMTQ4ODIzNztqOzE3MDE0OzIwNDg7MjAyNTszMDAw"),
        movie("Deadpool","http://s3.foxfilm.com/foxmovies/production/films/103/images/feature/deadpool-film-header-now-playing-front-main-stage.jpg"),
        movie("Come back to me","http://videodrome-podcast.com/wp-content/uploads/2015/01/oculus-come-back-to-me-300x214.png")]
print(movie0[1].title)
@app.route('/')
def hello_world():
    return 'Hello World!'
@app.route('/C2')
def C2():
    return 'Hello C4E3!'
@app.route('/Hai')
def HAI():
    return render_template('homemovie.html')
@app.route('/<index>')
def xemphimmy(index):
    i=int(index)
    if i<=len(movie0):
        return render_template("phimmy.html",Title=movie0[i].title,image=movie0[i].img)
    else:
        return "The film not found"

    # return "Title" + movie0.title+' '+'imag'+movie0.img
    # return render_template('heroes.html')


if __name__ == '__main__':
    app.run()
