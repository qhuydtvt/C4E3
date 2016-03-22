from firebase import firebase
fb = firebase.FirebaseApplication('https://techkids-c4e.firebaseio.com/user/',None)
#result = fb.get('/user',None)
#print(result)
##for key,value in result.items():
##        print(value['name'], ":", value['text'])
##        
#for i in result:
    #print(result[i]['name'],":",result[i]['text'])

result = fb.post('/',{'name':"Tho",'title':'flash', 'content': 'oh yeah', 'image':'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcSRUig6S0deF1iBncmnEOSuP98ia05uQ6PdVfNm7te_tSldGhej'})
print(result)
