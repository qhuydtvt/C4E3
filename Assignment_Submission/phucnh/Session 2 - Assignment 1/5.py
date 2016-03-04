i=0
tholon=1
thobe=0
while i<4:
    tong=tholon+thobe
    tholon=thobe+tholon
    thobe=tholon
    print(('Monnt {0}: {1} pair(s) of rabbits').format(i,tong))
    print (tholon,thobe)
    i=i+1
