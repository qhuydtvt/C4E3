a,x=input("nhap toa do diem 1:").split(",")
b,y=input("nhap toa do diem 2:").split(",")
a,b,x,y = [int(a),int(b),int(x),int(y)]
d= ((a-b)**2+(x-y)**2)**0.5
print("khoang cach giua 2 diem la:",d)
