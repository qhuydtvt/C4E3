name = 'Tho'
a = 24
person = {
    "name":name,
    "age":a
    }
person2={}
person2['name']=name
person2['age']=a
print(person)
print(person2)
n = input("Ten bo phim: ")
m = input("Chat luong: ")
l = input("Nam: ")
movie={}
movie['name'] = n
movie['quality'] = m
movie['year'] = l
print(movie)
a = input("Ten bo phim muon sua: ")
if movie['name']==a:
    b = input("Thong tin muon sua: ")
    if b in movie:
        movie[b]=input("sau khi sua la: ")
        print(movie)
          
