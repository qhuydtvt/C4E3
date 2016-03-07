while True:
    a = int(input("enter a number "))
    if a%2 == 0:
        print ("this is an even number.")
        b = (a**.5)
        if b%2 == 0:
            print ("this is a square number")
            break
        else:
            print ("this is not square number.")
    else:
        print ("this is an odd number.")
        break
