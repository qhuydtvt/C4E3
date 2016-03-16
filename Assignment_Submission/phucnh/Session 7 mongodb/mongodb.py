from pymongo import MongoClient
from bson.objectid import ObjectId

# Connect to Mlab
URI ="mongodb://c4e3:CodeTheChange@ds015879.mlab.com:15879/c4e3_movie_db"
client = MongoClient(URI)

# Get the default database
db = client.get_default_database()
movies = db["movies"]

def duyet_phim():
    i=0
    for movie in movies.find():
        i=i+1   
        print(i,movie['trans_name'],"(",movie['year'],")")
        print(movie['org_name'],"-" , movie['quality'])
        print();

duyet_phim()

them_phim=input("Ban co muon them phim? Co/Khong:")
if them_phim == "co":
    org_name=input("Ten tieng Anh cua phim: ")
    trans_name=input("Ten tieng Viet cua phim: ")
    quality=input("Chat luong phim? HD/Cam: ")
    year=input("Nam san xuat: ")
    movies.insert_one({
        "org_name" : org_name,
        "trans_name": trans_name,
        "quality": quality,
        "year": year})

duyet_phim()
