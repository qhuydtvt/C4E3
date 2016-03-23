from pymongo import MongoClient
#from bson.objectid import ObjectId


# Connect to Mlab
URI ="mongodb://c4e3:CodeTheChange@ds015879.mlab.com:15879/c4e3_movie_db"
client = MongoClient(URI)

# Get the default database
db = client.get_default_database()

def them_document(collection,document):
    new_collection=db[collection]
    result= new_collection.insert_one(document)
    print(result)


def excel(duongdan):
    import xlrd

    book = xlrd.open_workbook(duongdan)
    sheet = book.sheet_by_index(0) #or by the index it has in excel's sheet collection
 
    data = [] #make a data store
    for i in range(sheet.nrows): 
       if i>0: #bo qua dong dau tien 
            data.append(sheet.row_values(i)) #drop all the values in the rows into data
    return data


#ds_luong= excel("D:\CODE\C4E3\github\Assignment_Submission\phucnh\Session 8\mail.xlsx")

ds_luong= excel("D:\CODE\C4E3\github\Assignment_Submission\phucnh\lab3\mail.xlsx")


#for luong in ds_luong:    
#def dm_them(name, team, lop , sbd, luong):
#  return {'name':name, 'team':team,'lop':lop,'sbd':sbd,'luong':luong,'tong':(sbd*luong)}

def chen_luong(luong):
  return {'name':luong[0], 'team':luong[1],'lop':luong[2],'sbd':luong[3],'luong':luong[4],'tong':(luong[3]*luong[4])}
  

def them_luong():  
    for luong in ds_luong:    
        them_document("bang_luong_phuc",chen_luong(luong))

#them_document("bang_luong_phuc",dm_them('Hiep','C4E','C4E3',10,100))
#them_document("bang_luong_phuc",dm_them('Huy','C4E','C4E1',10,200))
#them_document("bang_luong_phuc",dm_them('Huy','C4E','C4E2',10,200))
#them_document("bang_luong_phuc",dm_them('Huy','C4E','C4E3',8,200))

dbluong = db["bang_luong_phuc"]
def duyet_luong():
    i=0
    for luong in dbluong.find():
        i=i+1
        #print(luong)
        print(i,"Ten: ",luong['name'],"-","Team: ",luong['team'],"-","Lop: ",luong['lop'],"-","So buoi day: ",luong['sbd'],"-",
              "Luong: ",luong['luong'],"-","Tong: ",luong['tong'])
        
def reset_luong():
    for luong in dbluong.find():        
           dbluong.delete_one({"_id":luong['_id']}) 
def tim_luong(ten):
    return dbluong.find_one({'name':ten})


def sua_luong():
    phim_sua=int(input("Ban muon sua so buoi day cua so thu tu may: "))
    i=0
    for luong in dbluong.find():
        i=i+1        
        if phim_sua==i:
            muc_sua=int(input("Ban muon sua thanh may buoi day: "))
            dbluong.update_one({
                "_id":luong['_id']},
                {'$set':{"sbd": muc_sua}})

def xoa_luong():
    phim_sua=int(input("Ban muon xoa luong o so thu tu may: "))
    i=0
    for luong in dbluong.find():
        i=i+1        
        if phim_sua==i:
           dbluong.delete_one({"_id":luong['_id']}) 
                
def luu_luong():
    import pyexcel
    import pyexcel.ext.xlsx

    luu_file=[]
    for luong in dbluong.find():
        luu_file.append([luong['name'],
                        luong['team'],
                        luong['lop'],
                        luong['sbd'],
                        luong['luong'],
                        luong['tong']])

    #luu_file=[['Phuc','C4E','C4E3',21,100,2100]]
    pyexcel.save_as(array=luu_file, dest_file_name="example.xlsx")


#reset_luong()
#them_luong()
duyet_luong()
print()
thao_tac=input("Ban muon sua, xoa luong hay luu file? Sua/Xoa/Luu: ");
thao_tac=thao_tac.lower()
if thao_tac=="xoa":
    xoa_luong()
elif thao_tac=="sua":
    sua_luong()
elif thao_tac=="luu":
    luu_luong()    
duyet_luong()


        
