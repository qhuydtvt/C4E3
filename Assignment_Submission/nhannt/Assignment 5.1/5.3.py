#1
range1=range(0,7)
for i in range1:
    print(i)
#2
range2=range(1,11)
for i in range2:
    if i%3==1:
        print(i)
#3
range3=range(5,10)
list3= []
list3.extend(range3)
i=0
while i<len(list3):
    print(list3[i]-2*i)
    i=i+1
#4
range4=range(6,11)
list4=[]
list4.extend(range4)
u=0
while u<len(list4):
    print(list4[u]-u*3)
    u=u+1
