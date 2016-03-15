def vehinh(m,n):    
    for i in range(0,n):
        print("* ",end='')
    print("")
    for i in range(2,m):
        print("*",end='')
        for i in range(2,n*2-1):
            print(" ",end='')
        print("*")
    for i in range(0,n):
        print("* ",end='')
m=int(input("nhap m:"))
n=int(input("nhap n:"))
vehinh(m,n)
