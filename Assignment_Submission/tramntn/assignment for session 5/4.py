#4.1
S=0
for i in range(1,10):
    S=S+1/i
print(S)

#4.2
n=int(input('nhap so n'))
S=0
for i in range(1,n):
    S=S+1/n
print(S)


#4.3
n=int(input('nhap so n'))
s=0
giaithua=1
i=1
for i in range (1,n):
     giaithua = giaithua * (i+1)
     s = s + 1/giaithua
print(s)
