while True:
    n = int(input("Enter a number: "))
    i=1
    m=1
    while True:
        if n<5:
            print("This is not a perfect number")
            break
        else:
            i=i+1
            if i==n and m==n:
                print("This is a perfect number")
                break
            elif i==n and m!=n:
                print("This is not a perfect number")
                break
            elif n/i%2==0 or n/i%2==1:
                m=m+i
