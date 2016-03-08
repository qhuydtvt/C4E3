while True:
    n = int(input("enter a number:"))
    x = 0
    i = 1
    while i<n:
        if(n%i==0):
            x = x+i
        i= i+1
    if n>1 and (x==n):
        print(n,'is a PERFECT NUMBER')
    else:
        print(n,'is NOT a PERFECT NUMBER')
