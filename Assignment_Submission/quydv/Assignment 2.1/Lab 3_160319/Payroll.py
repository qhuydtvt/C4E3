
from pymongo import MongoClient
from bson.objectid import ObjectId

URI = "mongodb://c4e3:CodeTheChange@ds015879.mlab.com:15879/c4e3_movie_db" #dia chi de ket noi
client = MongoClient(URI)
db = client.get_default_database()

quy_collection = db["payroll_quydv"] #add collection

##def insert_collection(user, team):
##    result = quy_collection.insert_one(
##            {"name": user,
##             "team": team
##                }
##        )
##    print(result)

def nhap_bang_luong(collection):
        ho_ten = input("Ho ten:")
        team = input("Team:")
        lop = input("Lop:")
        so_buoi_day = int(input("So buoi day:"))
        luong_1_buoi = int(input("Luong/buoi:"))
        tong_luong_day = luong_1_buoi * so_buoi_day
        result = collection.insert_one(
            {"ho_ten": ho_ten,
             "team": team,
             "lop": lop,
             "so_buoi_day": so_buoi_day,
             "luong_1_buoi": luong_1_buoi,
             "tong_luong_day": tong_luong_day,
                }
            )
        return result

##for i in range(7):
##    nhap_bang_luong(quy_collection)

##quy_collection.delete_one(
##    {"name": "quydv"
##     }
##    )

def print_collection(collection):
    for i in quy_collection.find():
        print(
            "Ho ten:", i["ho_ten"],
            "Team:", i["team"],
            "Lop:", i["lop"],
            "So buoi day:", i["so_buoi_day"],
            "Luong 1 buoi:", i["luong_1_buoi"],
            "Tong luong day:", i["tong_luong_day"]
            )



def them_tong_luong(ho_ten):
    a = quy_collection.find_one({"ho_ten": ho_ten})
    tong_luong = a["luong_1_buoi"] * a["so_buoi_day"]
    quy_collection.update_many( #update document trong mongodb
        {"ho_ten": ho_ten},
        {"$set": {
            "tong_luong_day": tong_luong}
            }
        )

# them_tong_luong("Nguyen Quang Huy") #them tong luong vao document
# for document in quy_collection.find():
#     if "tong_luong_day" not in document:
#         them_tong_luong(document["ho_ten"])

#ham tim theo ten:
def find(collection, key, data):
    result = collection.find({key: data})
    for i in result:
        print(
            "Ho ten:", i["ho_ten"],
            "Team:", i["team"],
            "Lop:", i["lop"],
            "So buoi day:", i["so_buoi_day"],
            "Luong 1 buoi:", i["luong_1_buoi"],
            "Tong luong day:", i["tong_luong_day"],
            )
    print("\n")

find(quy_collection, "lop", "C4E3")

print_collection(quy_collection)


