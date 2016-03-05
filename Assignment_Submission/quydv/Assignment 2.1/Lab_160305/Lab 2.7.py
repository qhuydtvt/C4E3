while True:
    username = input("Enter user name:")
    if username == "":
        print("You must enter your username")
        
    elif username == "bighero6":
        while True:
            password = input("Enter password:")
            if password == "codethechange":
                print("Welcome to techkids 2016")
                break
            elif password == "":
                print("You must enter a password")
            else:
                print("Please reenter your password!")
    else:
        print("please reenter your username")
    break
