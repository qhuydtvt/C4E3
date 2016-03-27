from firebase import firebase
fb= firebase.FirebaseApplication("https://techkids-c4e.firebaseio.com/",None)


#result=fb.get('/user',None)

#print (result)

##for key in result:
##    
##    chat =(result[key])
##    print (chat['name'],": ",chat['text'])

##for a,b in result.items():
##    #print (a,b)
##    print (b['name'],": ",b['text'])
my_name='Phuc'
my_title='Hello'
my_content="ABC DEF XYX nhe"
url="http://health.infoniac.com/uimg/choose-baby-sex.jpg"
result=fb.post('',{'name':my_name,'title':my_title,'content':my_content,'image':url})
print (result)
