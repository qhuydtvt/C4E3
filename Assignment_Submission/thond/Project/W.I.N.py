from flask import Flask, render_template
from mongoengine import connect
from restaurants import *

connect('test',host = "mongodb://c4e3:c4e3@ds023530.mlab.com:23530/restaurant-c4e3")

app = Flask(__name__)
class Restaurant8(Document):
    post_id = StringField()
    message = StringField()
    created_time = StringField()
    likes = StringField()
    shares = StringField()
    comments = StringField()
    score = StringField()

rs = Restaurant8.objects


@app.route('/test')
def test():
    return render_template("output.html",
                           restaurant_list = rs)
    return "Not found"

#Front - end
#for example: res_list = [ {name:"QuatLam"....}, {name:"Pham Van Dong"....}  ]
# {% for restaurant in res_list %}
# <h1>{{ restaurant.name }} </h1>
# {% endfor %}



if __name__ == '__main__':
    app.run()
