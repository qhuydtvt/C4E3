l = list(range(1,11))
s = 0
for i in l:
    a = 1/i
    s = s + a
print(s)

n = int(input("Enter n for the sequence from 1 to n:"))
k = list(range(1,n+1))
s1 = 0
for j in k:
    b = 1/j
    s1 = s1 + b
print(s1)

m = int(input("Enter n for the sequence from 1 to n:"))
g = list(range(1,m+1))
s2 = 0
for e in g:
    h = list(range(1,e+1))
    print(h)
    p = 1
    for f in h:
        p = p*f
    print(p)
    r = 1/p
    s2 = s2 + r
print(s2)
