def tinh(x,y,phep):
    if phep=="+":
        return x+y
    if phep=="-":
        return x-y
    if phep=="*":
        return x*y
    if phep=="/":
        return x/y


x=int(input("nhap so x= "))
y=int(input("nhap so y= "))
phep=input("chon phep tinh + - * / ")
print(str.format(" {0} {1} {2} = {3}",x,phep,y,tinh(x,y,phep)))
