def factorial(x):
    i=1
    a=1
    while i<x+1:
        a=a*i
        i=i+1
    return a

n=int(input("enter the number:"))
a = factorial(n)
print("the factorial of a number is:",a)
