from pymongo import MongoClient
from bson.objectid import ObjectId

URI = "mongodb://c4e3:codethechange@ds015859.mlab.com:15859/minh_movie_db"
n = MongoClient(URI)
"""
print(n)
#MongoClient(host=['ds015859.mlab.com:15859'], document_class=dict, tz_aware=False, connect=True)
"""

db = n.get_default_database()
movies = db["movies"]
"""
print(db)
#Database(MongoClient(host=['ds015859.mlab.com:15859'], document_class=dict, tz_aware=False, connect=True), 'minh_movie_db') 
print(movies)
#Collection(Database(MongoClient(host=['ds015859.mlab.com:15859'], document_class=dict, tz_aware=False, connect=True), 'minh_movie_db'), 'movies')
"""

def find_movie():
    print("I will find you and I will kill you")
    a = input("_id: ")
    for i in movies.find({ "_id" : ObjectId(a)}):
        print(i)

def delete_movie():
    print("I hate it, too. Deletetime!")
    a = input("org_name: ")
    for i in movies.find_one_and_delete({
            "org_name": a}):
        print(str.format("{0} has been deleted", a))

def add_movie():
    print("Let's add a new movie!")
    colle = {
            "org_name": input("org_name: "),
            "trans_name": input("trans_name: "),
            "quality": input("quality: "),
            "year": int(input("year: "))
            }
    movies.insert_one(colle)
    print("Yay us!")

def edit_movie():
    print("My bad. Fix me!")
    a = input("org_Oldname: ")
    b = input("org_Newname: ")
    for i in movies.find_one_and_update({
            "org_name": a}, {"$set":{
            "org_name": b}}):
        print(str.format("{0} has been updated", a))

#find_movie()
#delete_movie()
#add_movie()
#edit_movie()
    
