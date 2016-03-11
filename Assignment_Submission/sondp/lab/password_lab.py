n=input("Enter your  username: ")
if len(n)==0:
 print("you must enter your username")
 n=input("Enter your username: ")
elif len(n)!=0:
    print("username is invalid")
    m=input("Enter your password: ")
    while len(m)==0:
        m=input("Enter your password: ")
    if len(m)!=0:
        while m!="codethechange":
         print("Nhap password sai roi ")
         m=input("Enter your password: ")
        if m=="codethechange":
         print("welcome to techkids 2016")
        
        
          
