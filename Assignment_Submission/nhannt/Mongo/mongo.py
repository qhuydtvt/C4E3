from pymongo import MongoClient
from bson.objectid import ObjectId

URI = "mongodb://c4e3:CodeTheChange@ds015879.mlab.com:15879/c4e3_movie_db"
client = MongoClient(URI)


db = client.get_default_database()
new_collection = db["bang_luong_nhan_dz"]
def create_mot(Name, Team, Class, So_buoi_day, luong_buoi):
    tong_luong = So_buoi_day * luong_buoi
    Nhan = new_collection.insert_one(
        {'Name': Name,
         'team': Team,
         'Lop': Class,
         'So buoi day': So_buoi_day,
         'Luong/buoi': luong_buoi,
         'Tong luong': tong_luong
         }
        )
##i=0
##while i<7:
##    Ten = input("nhap ten:")
##    Team = input("nhap team:")
##    Lop = input("nhap lop:")
##    So_buoi = int(input("so buoi day:"))
##    luong_buoi = int(input("luong tren buoi:"))
##    create_mot(Ten,Team,Lop,So_buoi,luong_buoi)
##    i=i+1



##def Search_ten(ten):
##    tim_document = new_collection.find({"Name":ten})
##    for i in tim_document:
##        print(i)
##
##Timten = input("tim ten:")
##Search_ten(Timten)

##result = new_collection.update_one(
##    {"team": "C4E"},
##    {"$set":{"Luong/buoi": 400}}
##    )

result = new_collection.delete_one({"team":"C4E"})
    
tim_document = new_collection.find()
for i in tim_document:
        print(i)





