#4.1
myrange=range(1,11)
n=0
for i in myrange:
    n=n+i
print("tong cac phan tu trong list la:",n)
#4.2
m=0
for i in myrange:
    m=m+1/i
print("tong S la:",m)
#4.3
l= int(input("nhap n:"))
myrange3=range(1,l+1)
e=0
for i in myrange3:
    e=e+1/i
print("tong S theo n la:",e)
#4.4 
k= int(input("nhap n:"))
myrange4=(range(1,k+1))
p=0
u=1
for i in myrange4:
    p=p+1/u
    u=u*(i+1)
print("tong S bai 4 theo n la:",p)
