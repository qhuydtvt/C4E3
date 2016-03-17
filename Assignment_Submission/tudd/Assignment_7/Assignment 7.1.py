def uoc_cua_1_so(x):
    uoc_cua_so = []
    for i in range(1,x+1):
        if x % i == 0:
            uoc_cua_so.append(i)
    return uoc_cua_so

n = int(input("nhap so: "))
print(str.format("Uoc cua {0} la: {1}",n, uoc_cua_1_so(n)))
