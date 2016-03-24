from pymongo import MongoClient
from bson.objectid import ObjectId

URI = "mongodb://c4e3:CodeTheChange@ds015879.mlab.com:15879/c4e3_movie_db"
client = MongoClient(URI)

db = client.get_default_database()
movies = db["movies"]

##movies.insert_one(
##    {
##        "org_name": "Dawn of Justice",
##        "trans_name": "Cong ly thuc giac",
##        "quality": "1080",
##        "year": 2016
##    }
##)

##movies.delete_one({"org_name": "Into the wild"})
##movies.delete_one({'_id': ObjectId('56e9e3707d1a570a5cf9faee')})
movies.update_one(
    {"trans_name": "Moi tinh bat tan"},
        {
            "$set": {
                "quality": "10K"
            }
        }
)
for movie in movies.find():
    print(movie)

client.close()
