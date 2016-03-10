def giaithua(n):
    i=1
    giaithua=1
    while i<n+1:
        giaithua=giaithua*i
        i=i+1
    return giaithua
while True:
    a=int(input('Nhat so can tim tong: '))
    i=1
    s=0
    while i<a+1:
        s=s+1/(giaithua(i))
        i=i+1
    print('Tong cac so can tim la', s)



                   
