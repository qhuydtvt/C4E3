while True:
    n = int(input("Enter a even number: "))
    if (n%2) == 0:
        print("This is a even number")
        a = n**(0.5)
        if (a%2) == 0:
            print("n la so chinh phuong")
        else:
            print("n khong phai so chinh phuong")
        break
    else:
        print("This is a odd number")
        
       
       
