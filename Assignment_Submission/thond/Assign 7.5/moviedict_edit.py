from pymongo import MongoClient
from bson.objectid import ObjectId
n = input("What movie do you want to edit? (in English) ")
URI = "mongodb://c4e3:CodeTheChange@ds015879.mlab.com:15879/c4e3_movie_db"
client = MongoClient(URI)
db = client.get_default_database()
movies = db["movies"]
for movie in movies.find({"org_name": n}):
    print(movie)
    m = input("What detail do you want to edit?(Origninal name, translated name, quality, or release year) ")
    e = input("What do you want to change it to? ")
    if m == "translated name":
        movie['trans_name'] = e
    elif m == "orginial name":
        movie['org_name'] = e
    elif m == 'quality':
        movie['quality']= e
    elif m == 'year':
        movie['year'] = e
    print(movie)


