n=input("input a list of number:")
m=n.split()
m = map(int,m)
a=1
for x in m:
    a=a*x
print(a)
