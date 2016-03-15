def tong(a,b):
    c=a+b
    return c
def hieu(a,b):
    c=a-b
    return c
def nhan(a,b):
    c=a*b
    return c
def chia(a,b):
    c=a/b
    return c
x=int(input("nhap so thu 1:"))
y=int(input("nhap so thu 2:"))
a=input("nhap phep toan:")
if a=="cong":
    i=tong(x,y)
elif a=="tru":
    i=hieu(x,y)
elif a=="nhan":
    i=nhan(x,y)
elif a=="chia":
    i=chia(x,y)
print("dap an la:",i)
