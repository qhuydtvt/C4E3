#1

#2
tong=0
for i in range(1,11):
    tong= tong+1/i
print(tong)

#3
n= int(input("nhap so n "))
tong=0
for i in range(1,n+1):
     
    tong= tong+1/i
print(tong)

#4

n= int(input("nhap so n "))
tong=0
for i in range(1,n+1):
    nhan=1
    for j in range(1,i+1):
        nhan=nhan*j
    tong= tong+1/nhan 
print(tong)
