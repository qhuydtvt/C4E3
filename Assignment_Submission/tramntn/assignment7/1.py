def divisor(x):
    list1 = []
    for i in range(1,x+1):
        if n%i == 0:
            list1.append(i)
    return list1

n = int(input('Enter a number: '))
print('Divisors: ', divisor(n))
