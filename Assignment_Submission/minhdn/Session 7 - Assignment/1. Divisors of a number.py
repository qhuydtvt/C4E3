#Cach 1:
n = int(input('Enter a number: '))

def get_divisor():
    list0 = []
    for i in range(1,n+1):
        if n%i == 0:
            list0.append(i)
    
get_divisor()
print('Divisors of the number: ', list0)


#Cach 2:
def get_divisor(x):
    list0 = []
    for i in range(1,x+1):
        if n%i == 0:
            list0.append(i)
    return list0

n = int(input('Enter a number: '))
print('Divisors of the number: ', get_divisor(n))
