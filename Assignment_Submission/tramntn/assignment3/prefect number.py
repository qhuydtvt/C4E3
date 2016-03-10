while True:
    n= int(input("Enter a number: "))
    i=1
    if n< 5:
        print(n, "is not a perfect number")
    else:
        S = 0
        while i<n:       
            if n % i == 0:
                S=S+i
            i=i+1
        if S == n:       
            print(n, "is a perfect number")
        else:       
            print(n, "is not a perfect number")  
