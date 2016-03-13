n=input("input a list of number:")
m=n.split()
m = map(int,m)
k = [i for i in m if i%2==0]
print("the even number:",end='')
for i in k: print(i," ",end='')
