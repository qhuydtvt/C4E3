#2.1
sheep = [100, 10, 20, 30, 40,25,67,89]
print("Hello, my name is Nhan and these are my sheep sizes:")
print(sheep)
#2.2
print("Now my biggest sheep has size",max(sheep),"let's shear it")
#2.3
print("After shearing, here is my flock")
sheep.insert(sheep.index(max(sheep)),8)
sheep.remove(max(sheep))
print(sheep)
#2.4
sheep1=[]
for i in sheep:
    i=i+50
    sheep1.append(i)
print("One month has passed, now here is my flock:")
print(sheep1)
#2.5
##a=int(input("how many month?:"))
##def sheepsheep():
##    print("Now my biggest sheep has size",max(sheep),"let's shear it")
##    print("After shearing, here is my flock")
##    sheep.insert(sheep.index(max(sheep)),8)
##    sheep.remove(max(sheep))
##    print(sheep)
##    sheep1=[]
##    for i in sheep:
##        i=i+50
##        sheep1.append(i)
##    print("One month has passed, now here is my flock:")
##    print(sheep1)
##    sheep.clear()
##    for i in sheep:
##        i=sheep
##u=0
##while u<a:
##    sheepsheep()
##    u=u+1

