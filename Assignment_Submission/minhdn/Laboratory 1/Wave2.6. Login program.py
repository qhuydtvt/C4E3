while True:
    while True:
        n = str(input("Enter your username: "))
        if len(n) == 0:
            print("You must enter your username")
        else:
            break
   
    if n != "bighero6":
        print("Username is invaild")
           
    else:
        break
    
while True:
    p = str(input("Enter your password: "))
    if p == "codethechange":
        print("Welcome to TechKids!")
        break
    else:
        print("Password is invaild")
