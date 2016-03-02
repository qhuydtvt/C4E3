l=1
n=1
i=0
while i<=4: 
    print(str.format("Month {0}: {1} pair(s) of rabbits", i, l))
    luu=l
    l= luu+n
    n=luu
    i=i+1
