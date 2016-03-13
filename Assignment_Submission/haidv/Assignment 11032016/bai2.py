def factorial(n):
    if n<0:
        factorial = 'Does not exist'
    if n==0:
        factorial = 1
    if n>0:
        factorial = 1
        for i in range (1,n+1):
            factorial=factorial*i
    return factorial
print(factorial(0))
        
