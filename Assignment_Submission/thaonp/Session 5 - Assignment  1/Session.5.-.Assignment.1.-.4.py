#4.1 ??? Em khong hieu de bai
#4.2
S2=0
i2=1
while i2<=10:
    S2=S2+1/i2
    i2=i2+1
print('S= ',S2)
#4.3
n=int(input('Enter n= '))
S3=0
i3=1
while i3<=n:
    S3=S3+1/i3
    i3=i3+1
print('S= ',S3)

#4.4
m=int(input('Enter n= '))
S4=1
P=1
i3=1
while i3<=m:
    P=P/i3
    S4=S4+P
    i3=i3+1
print('S= ',S4)
