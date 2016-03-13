def divisors(x):
    divisorslst=[]
    for i in range(1,x): 
        if x%i==0:
            divisorslst.append(i)
    return divisorslst
n=int(input("Enter a numbuer: "))
print('Divisors of that numbuer: ',divisors(n))
