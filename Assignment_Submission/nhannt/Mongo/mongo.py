from pymongo import MongoClient
from bson.objectid import ObjectId

URI = "mongodb://c4e3:CodeTheChange@ds015879.mlab.com:15879/c4e3_movie_db"
client = MongoClient(URI)

db = client.get_default_database()
movies = db["movies"]
movies.insert_one(
{
"org_name" : "Nhan so hansome",
"trans_name": "Dai ca Nhan Dep trai",
"quality": "4K",
"year": 1992
}
)
for movie in movies.find():
    print(movie)
