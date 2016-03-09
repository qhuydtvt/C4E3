while True:
    number = int(input("Enter a number: "))
    i=1
    if number < 6:
        print(number, "is not a perfect number")
    else:
        S = 0
        while i<number:       
            if number % i == 0:
                S=S+i
            i=i+1
        if S == number:       
            print(number, "is a perfect number")
        else:       
            print(number, "is not a perfect number")  

