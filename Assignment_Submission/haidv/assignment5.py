i=1
a=0
b=1
while i<=100:
    c=a+b
    a=b
    b=c
    print(str.format('So cap tho thang {0} la {1}',i,c))
    i=i+1
