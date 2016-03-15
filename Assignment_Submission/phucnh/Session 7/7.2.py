#2. Write a Python function to simulate a simple calculator 


def maytinh(a,b,phep):
    if phep=="+":
        return a+b
    if phep=="-":
        return a-b
    if phep=="*":
        return a*b
    if phep=="/":
        return a/b


a=int(input("nhap so a= "))
b=int(input("nhap so b= "))
pheptinh=input("chon phep tinh + - * / ")
print(str.format(" {0} {2} {1} ket qua la {3}",a,b,pheptinh,maytinh(a,b,pheptinh)))

