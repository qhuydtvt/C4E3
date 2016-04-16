from mongoengine import *

class Restaurant8(Document):
    post_id = StringField()
    message = StringField()
    created_time = StringField()
    likes = StringField()
    shares = StringField()
    comments = StringField()
    score = StringField()