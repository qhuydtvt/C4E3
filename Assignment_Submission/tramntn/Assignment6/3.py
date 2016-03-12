list1=input('nhap list')
list1 = [int(x) for x in list1.split()]
for x in list1:
    if (x%2)==0:
        print('even number is:',x)
    
