def divisors(n):
    divi=[x for x in range (-n-1,n+1,1)if x!=0 and n%x==0]
    return divi
print(divisors(60))
