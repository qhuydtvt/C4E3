from pymongo import MongoClient
URI = "mongodb://c4e3snmovie:c4e3sbmovie@ds015869.mlab.com:15869/c4e3_son_movie"
client = MongoClient(URI)
db = client.get_default_database()
movies = db["movies"]

movies.insert_one(
    {
        "org_name" : "Intro the wild",
        "tran_name" : "Lac vao noi hoang da",
        "quality" : "1080",
        "year" : "2016"
    }
)
client.close()
