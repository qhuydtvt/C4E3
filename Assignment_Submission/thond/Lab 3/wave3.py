from pymongo import MongoClient
URI = "mongodb://c4e3:CodeTheChange@ds015879.mlab.com:15879/c4e3_movie_db"
client = MongoClient(URI)
db = client.get_default_database()
ud = db["bang_luong_Tho"]

def updo(a,b):
    ud.update_one(a,{'$set':b})
    
updo({'name':'hiep'}, {'team':'techkidz'})
updo({'name':'Huy', 'lop':'c4e3'},{'team':'techkids'})

def delo(a):
    ud.delete_one(a)

delo({'name':'hiep'})

for doc in ud.find():
    print(doc)


    
