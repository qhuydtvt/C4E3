while True:
    n=int(input("dien so "))
    if n%2==0:
        print("so chan")
        if n**0.5%2==1 or n**0.5%2==0:
            print("so chinh phuong ")
            break
    else:
        print("so le")
