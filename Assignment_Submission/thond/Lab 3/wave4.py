import pyexcel
import pyexcel.ext.xlsx

##example_dict = {"Column 1": [1,2,3], 'Column 2': [4,5,6], 'Column 3': [7,8,9]}
##sheet = pyexcel.get_sheet(adict = example_dict)
##sheet.save_as('output.xlsx')

from pymongo import MongoClient

URI = "mongodb://c4e3:CodeTheChange@ds015879.mlab.com:15879/c4e3_movie_db"
client = MongoClient(URI)
db = client.get_default_database()
fo = db["bang_luong_Tho"]
##def tim_mot(a):
##    print(fo.find_one(a))
##
##tim_mot({'name':'hiep'})
#

sali_dict = {'name': 
