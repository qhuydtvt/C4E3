from pymongo import MongoClient
#from bson.objectid import ObjectId

URI = "mongodb://c4e3:CodeTheChange@ds015879.mlab.com:15879/c4e3_movie_db"
client = MongoClient(URI)
db = client.get_default_database()
sali = db["bang_luong_Tho"]
##result = sali.insert_one(
##    {'name':'hiep',
##     'team':'c4e',
##     'lop':'c4e3',
##     'so buoi day':10,
##     'luong/buoi':100,
##     'tong buoi day':1000
##     }
##    )
##print(result)


def new_sali(n,t,l,s,lb):
    new = sali.insert_one(
        {'name':n,
         'team':t,
         'lop': l,
         'so buoi day':s,
         'luong/buoi':lb,
         'tong so buoi': ts
         }
        )
    print (new)
while True:
        n = input("Name: ")
        t = input("Team: ")
        l = input("Lop: ")
        s = int(input("So buoi day: "))
        lb = int(input("Luong/buoi: "))
        ts = s * lb
        new_sali(n,t,l,s,lb)
     

