while True:
    n = int(input("Enter a number: "))
    i=1
    while True:
        if n==1:
            print("This is a prime number")
            break
        elif n==2:
            print("This is a prime number")
            break
        elif n<0:
            print("This is not a prime number")
            break
        else:
            i=i+1
            if i==n:
                print("This is a prime number")
                break
            elif n/i%2==0 or n/i%2==1:
                print("This is not a prime number")
                break
