def factorial(x):
    result = 1
    for i in range(1,x+1):
        result *= i
    return result
n=int(input('nhap n'))
print('the factorial of a number is:',factorial(n))
