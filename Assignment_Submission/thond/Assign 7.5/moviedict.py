from pymongo import MongoClient
from bson.objectid import ObjectId
mov_name = input("What other movie do you want to add to the list? (in English) ")
if len(mov_name) != 0:
    org_name = mov_name
    print("Please provide details of the movie")
    trans_name = input("what is the translation of the movie name?" )
    quality = input("Quality of the movie (HD or Cam): ")
    year = input("What is the release year of the movie?" )
    URI = "mongodb://c4e3:CodeTheChange@ds015879.mlab.com:15879/c4e3_movie_db"
    client = MongoClient(URI)
    db = client.get_default_database()
    movies = db["movies"]
    movies.insert_one(
        {"org_name": org_name,
         "trans_name": trans_name,
         "quality": quality,
         "year": year
         }
    )
    for movie in movies.find():
        print(movie)
