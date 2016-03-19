from pymongo import MongoClient
from bson.objectid import ObjectId
URI = "mongodb://c4e3:codethechange@ds015939.mlab.com:15939/c4e3_movie"
client = MongoClient(URI)
db = client.get_default_database()
movies = db["movies"]
movies.insert_one(
    {
        "ori_name" : "Everything is easy when you are crazy",
        "trans_name" : "Moi Thu Se De Dang Khi Ban Dien",
        "quality " : "8k",
        "year" : 2016
    }
    )

for movie in movies.find():
    print(movie)
for movie in movies.find({'ori_name': 'Secret'}):
    print(movie)
for movie in movies.find({'_id': ObjectId('56e9a048e4b048de5aace0cb')}):
    print(movie)    
client.close()





    


