# s = 1/1 + 1/2! + 1/3! + ... + 1/n!

n = int(input('Enter a number: '))
s = 0
gt = 1
for i in range(1,n+1):
    gt *= i
    s += 1/gt
print('s =', s)


