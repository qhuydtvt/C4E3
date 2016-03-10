while True:
    a = int(input("Enter a number?"))
    if a <= 1:
        print (a, "is not a prime number.")
    elif a == 2:
        print (a, "is a prime number.")
    else:
        i = 2
        while i < a:
            if a%i == 0:
                print (a, "is not a prime number.")
                break
            else:
                print (a, "is a prime number.")
                break
            i = i + 1   
