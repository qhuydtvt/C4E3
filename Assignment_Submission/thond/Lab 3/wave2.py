from pymongo import MongoClient

URI = "mongodb://c4e3:CodeTheChange@ds015879.mlab.com:15879/c4e3_movie_db"
client = MongoClient(URI)
db = client.get_default_database()
fo = db["bang_luong_Tho"]

def tim_mot(a):
    print(fo.find_one(a))

tim_mot({'name':'hiep'})

print('----------')
def display_all():
    for i in fo.find():
        print(i)
display_all()
