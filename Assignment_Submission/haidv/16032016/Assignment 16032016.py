from pymongo import MongoClient
from  bson.objectid import ObjectId
URI ="mongodb://c4e3:CodeTheChange@ds015879.mlab.com:15879/c4e3_movie_db"
client = MongoClient(URI)
db=client.get_default_database()
movies=db["movies"]
def film():
    for movie in movies.find():
        print(movie['org_name']);
film()
def add_film(a,b,c,d):
    movies.insert_one({"org_name":a,"trans_name":b,"quality":c,"year":d})


def tim_film(name,field): 
    i=1
    BD =[]
    for movie in movies.find():
        
        
        if field ==1:
             if movie['org_name'].find(name)!=-1:
                 print(i,movie['trans_name'],"(",movie['year'],")")
                 print(movie['org_name'],"-" , movie['quality'])
                 print()
                 BD.append(movie['_id'])
                 i=i+1               
                 
                 
        if field ==2:
             if movie['trans_name'].find(name)!=-1:
                print(i,movie['trans_name'],"(",movie['year'],")")
                print(movie['org_name'],"-" , movie['quality'])
                print()
                BD.append(movie['_id'])
                i=i+1
                            
        
        if field ==3:
             if movie['quality'].find(name)!=-1:
                print(i,movie['trans_name'],"(",movie['year'],")")
                print(movie['org_name'],"-" , movie['quality'])
                print()
                BD.append(movie['_id'])
                i=i+1
    if i==1:
        print('Khong tim duoc gia tri nao')
    return(BD)
def suathongtin():
    k=int(input('Tim ten, ten dich, chat luong, 1, 2, 3 '))
    name=input('tim phim can xoa theo ten, ten dich, chat luong ')
    h=tim_film(name,k)
    n=int(input('Which film number do you want to modify:'))
    for movie in movies.find({'_id': h[n-1]}):
        muc_sua=input("Ban muon sua phan nao: Ten TV/Ten TA/CL/Nam: ")
        muc_sua=muc_sua.lower()
        if muc_sua=="ten tv":
            trans_name=input("Ten tieng Viet moi cua phim: ")
            movies.update_one({"_id":h[n-1]},{'$set':{"trans_name": trans_name}})
        elif muc_sua=="ten ta":
            org_name=input("Ten tieng Anh moi cua phim: ")
            movies.update_one({"_id":h[n-1]},{'$set':{"trans_name": trans_name}})    
        elif muc_sua=="cl":
            quality=input("Chat luong moi cua phim: ")
            movies.update_one({"_id":h[n-1]},{'$set':{"quality": quality}})
        elif muc_sua=="nam":
            year=int(input("Nam sx moi cua phim: "))
            movies.update_one({'_id':h[n-1]},
                      {'$set':{'year': year}})           

           
             

 
def xoaphim():               
    k=int(input('Tim ten, ten dich, chat luong, 1, 2, 3 '))
    name=input('tim phim can xoa theo ten, ten dich, chat luong ')

    
    h=tim_film(name,k)
    
    n=int(input('Which film number do you want to delete:'))

    for movie in movies.find({'_id': h[n-1]}):
            movies.remove(movie)
suathongtin()

g=int(input('The number of films'))
for i in range(0,g):
    a=input('The name of the film ')
    b=input('The translated name of the film ' )
    c=input('The quality of the film ')
    d=int(input('The production year '))
add_film(a,b,c,d)
xoaphim()
