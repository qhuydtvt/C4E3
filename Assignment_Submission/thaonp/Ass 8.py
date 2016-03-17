from pymongo import MongoClient
from bson.objectid import ObjectId

URI ="mongodb://c4e3:CodeTheChange@ds015879.mlab.com:15879/c4e3_movie_db"
client = MongoClient(URI)

db = client.get_default_database()
movies = db["movies"]

def film():
    i=0
    for movie in movies.find():
        i=i+1
        print(i,movie['trans_name'],"(",movie['year'],")")
        print(movie['org_name'],"-" , movie['quality'])
        print();

def insert():
    org_name=input("Org-name: ")
    trans_name=input("Trans-name: ")
    quality=input("Quality? HD/Cam: ")
    year=int(input("Year: "))
    movies.insert_one({
        "org_name" : org_name,
        "trans_name": trans_name,
        "quality": quality,
        "year": year})
def delete():
    phim_xoa=int(input("Which film number's do you want to delete: "))
    i=0
    for movie in movies.find():
        i=i+1        
        if phim_xoa==i:
           movies.delete_one({"_id":movie['_id']}) 

def edit():
    edit_movie=int(input("Which film number's do you want to edit: "))
    i=0
    for movie in movies.find():
        i=i+1        
        if edit_movie==i:
           edit_part=input("Which part do you want to edit: Org-name/Trans-name/Quality/Year: ")
           edit_part=edit_part.lower()
           if edit_part=="trans-name":
                trans_name=input("New trans-name: ")
                movies.update_one({
                    "_id":movie['_id']},
                    {'$set':{"trans_name": trans_name}})
           elif edit_part=="org-name":
                org_name=input("New org-name: ")
                movies.update_one({
                    "_id":movie['_id']},
                    {'$set':{"trans_name": trans_name}})    
           elif edit_part=="quality":
                quality=input('New quality: ')
                movies.update_one({
                    "_id":movie['_id']},
                    {'$set':{"quality": quality}})
           elif edit_part=="year":
                year=int(input("New year: "))
                movies.update_one({
                    '_id':movie['_id']},
                    {'$set':{'year': year}})      
           
film()
operations=input("Do you want to insert or delete or edit : ");
operations=operations.lower()
if operations=="insert":
    insert()
elif operations=="delete":
    delete()
elif operations=="edit":
    edit()
    
film()
