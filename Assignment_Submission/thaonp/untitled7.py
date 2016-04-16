from flask import Flask, render_template
from flask import request
from se import *

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def template():
        if request.method == 'POST':
            url = request.form['dinhmenh']
            post_url = build_post_url()
            post_list = extract_posts_within_30_days(post_url)
            for post in post_list:
                get_likes_shares_comments(post)

            sorted_post_list = sorted(post_list, key=get_post_score, reverse=True)

            connect('test', host="mongodb://c4e3:c4e3@ds023530.mlab.com:23530/restaurant-c4e3")

            class Restaurant5(Document):
                post_id = StringField()
                message = StringField()
                created_time = StringField()
                likes = StringField()
                shares = StringField()
                comments = StringField()
                score = StringField()

            # đẩy lên mongo
            for post in sorted_post_list[:6]:
                post_dict = post.__dict__
                post_dict_mongo = Restaurant5(post_id=str(post_dict['id']),
                                              message=post_dict['message'],
                                              created_time=str(post_dict['created_time']),
                                              likes=str(post_dict['likes']),
                                              shares=str(post_dict['shares']),
                                              comments=str(post_dict['comments']),
                                              score=str(post_dict['score'])
                                              )
                post_dict_mongo.save()
        return render_template('input.html')

if __name__ == '__main__':
    app.run()
