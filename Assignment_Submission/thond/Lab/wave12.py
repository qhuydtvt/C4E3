while True:
    a = input("enter your username: ")
    if len(a) == 0:
        print("You must enter your username.")
    if len(a)!= 0:
        if a != "bighero6":
            print("username is invalid.")
        while a == "bighero6":
            b = input("enter your password: ")
            if len(b) == 0:
                print("You must enter your password.")
            else: 
                if b != "codethechange":
                    print("password is invalid.")
                if b == "codethechange":
                    print("welcome to techkids 2016")
                    break
        break
            
