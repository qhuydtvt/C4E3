def divisor(x):
    a=[]
    for i in range(1,x+1):
        if x%i==0:
            a.append(i)
            i=i+1
    return a
n=int(input("nhap so can tim uoc:"))
a=divisor(n)
print("cac uoc cua so do la:",a)
