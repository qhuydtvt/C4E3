# 5.2.1
size = [3, 5, 7,10,15,20,90]
print(size)
# 5.2.2
print(str.format('biggest {0}', max(size)))
# 5.2.3
size[size.index(max(size))] = 8
print ('your ship size after shearing the biggest one', size)
# 5.2.4
size1=[]
for a in size:
    a = a + 50
    size1.append(a)
    print('one month has passed,now here is my flock',size1)
#5.2.5
    
