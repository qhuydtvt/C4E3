#4. Write a Python function get out all of divisors of a number

def layUoc(x):
    list_uoc=[]
    for i in range(1,x):
        
        if x%i==0:
            list_uoc.append(i)
    return list_uoc

nhapso=int(input("divisors of a numbuer: "))
print(layUoc(nhapso))
