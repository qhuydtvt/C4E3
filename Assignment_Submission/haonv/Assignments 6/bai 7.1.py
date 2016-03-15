n = int(input(' number : '))
def a (x):
    n_divisors = []
    for i in range(1,x+1):
        if x%i==0:
            n_divisors.append(i)
    return n_divisors
print('divisors : ' , a(n))
         
