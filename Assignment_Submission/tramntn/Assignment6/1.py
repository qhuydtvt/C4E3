def listmultifly(numlist):
    result=1
    for i in numlist:
        result *=i
    return result

list1=input(' enter a list of number')
list1 = [int(x) for x in list1.split()]
a=listmultifly(list1)
print(a)

