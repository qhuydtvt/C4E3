while True:
    number = int(input(" Enter a Number: "))
    Sum = 0
    i=1
    while i<number:
        if(number % i == 0):
            Sum = Sum + i
            
        i=i+1
    if number>1 and (Sum == number):
        print( number, " is a Perfect Number")
    else:
        print(number, " is NOT a Perfect Number")
