from flask import Flask,render_template

app = Flask(__name__)

class Movie:
    def __init__(self,title,img):
        self.title= title
        self.img= img
movie_list=[
 Movie("Batman","http://images.newseveryday.com/data/images/full/6782/batman-vs-superman.jpeg"),
 Movie("Superman","http://cdn8.openculture.com/wp-content/uploads/2011/10/Superman-fleischer.jpg"),
 Movie("Panda 3","https://i.ytimg.com/vi/kR6iiYvVEYc/maxresdefault.jpg"),
 Movie("Hitman","http://anh.24h.com.vn/upload/2-2014/images/2014-04-07/1396863671-hitman-2.jpg"),
 Movie("Em là bà nội của anh","http://baophunuso.com/wp-content/uploads/2015/11/dan-dien-vien-trong-phim-em-la-ba-noi-cua-anh-1024x990.jpg"),]
#dien 5 movie


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
    idx=int(movie_idx)-1
    return render_template("hero.html",title=movie_list[idx].title,img=movie_list[idx].img)
idx=3
print(movie_list[idx].img)

if __name__ == '__main__':
    app.run()
