t0 = 0
n0 = 1
print(str.format("Month {0}: {1} pair(s) of rabbits",t0,n0))
t = 1
n1 = 1
print(str.format("Month {0}: {1} pair(s) of rabbits",t,n1))
while t < 4:
    t = t + 1
    n = n0 + n1
    print(str.format("Month {0}: {1} pair(s) of rabbits",t,n))
    n0 = n1
    n1 = n
    
