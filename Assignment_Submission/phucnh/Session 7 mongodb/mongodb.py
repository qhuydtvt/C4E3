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
        #print(movie)
        print(i,movie['trans_name'],"(",movie['year'],")")
        print(movie['org_name'],"-" , movie['quality'])
        print();

def them_phim():
        org_name=input("Ten tieng Anh cua phim: ")
        trans_name=input("Ten tieng Viet cua phim: ")
        quality=input("Chat luong phim? HD/Cam: ")
        year=int(input("Nam san xuat: "))
        movies.insert_one({
            "org_name" : org_name,
            "trans_name": trans_name,
            "quality": quality,
            "year": year})
def xoa_phim():
    phim_xoa=int(input("Ban muon xoa phim stt so may: "))
    i=0
    for movie in movies.find():
        i=i+1        
        if phim_xoa==i:
           movies.delete_one({"_id":movie['_id']}) 



def sua_phim():
    phim_sua=int(input("Ban muon sua phim stt so may: "))
    i=0
    for movie in movies.find():
        i=i+1        
        if phim_sua==i:
            muc_sua=input("Ban muon sua phan nao: Ten TV/Ten TA/CL/Nam: ")
            muc_sua=muc_sua.lower()
            if muc_sua=="ten tv":
                trans_name=input("Ten tieng Viet moi cua phim: ")
                movies.update_one({
                    "_id":movie['_id']},
                    {'$set':{"trans_name": trans_name}})
            elif muc_sua=="ten ta":
                org_name=input("Ten tieng Anh moi cua phim: ")
                movies.update_one({
                    "_id":movie['_id']},
                    {'$set':{"trans_name": trans_name}})    
            elif muc_sua=="cl":
                quality=input("Chat luong moi cua phim: ")
                movies.update_one({
                    "_id":movie['_id']},
                    {'$set':{"quality": quality}})
            elif muc_sua=="nam":
                year=int(input("Nam sx moi cua phim: "))
                movies.update_one({
                    '_id':movie['_id']},
                    {'$set':{'year': year}})           
           
       
duyet_phim()
thao_tac=input("Ban muon them phim, sua phim hay xoa phim? Them/Sua/Xoa: ");
thao_tac=thao_tac.lower()
if thao_tac=="them":
    them_phim()
elif thao_tac=="xoa":
    xoa_phim()
elif thao_tac=="sua":
    sua_phim()

duyet_phim()
