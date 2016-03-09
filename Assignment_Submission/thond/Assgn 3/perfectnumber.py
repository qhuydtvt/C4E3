while True:
    a = int(input("Enter a number: "))
    if a <= 0:
        print(a, "is not a perfect number.")
    else:
        i = 1
        s = 0
        while i < a:
            if a%i == 0:
                s = s + i
                i = i+1
            else:
                i = i + 1
        #print(s)
        if s == a:
            print(a,"is a perfect number.")
        else:
            print(a, "is not a perfect number.")

       
            
                
            
