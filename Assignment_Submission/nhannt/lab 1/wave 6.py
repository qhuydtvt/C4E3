while True:
    n = input("enter your username? ")
    if n=="":
        print("ban chua nhap username")
    elif n=="bighero6":
        while True:
             m = input("enter your password? ")
             if m=="":
                 print("ban chua nhap pass")
             elif m=="codethechange":
                 print("welcome to techkid")
                 break
             else:
                 print("password is invalid")
        break
    else:
        print("user is invalid")
    
