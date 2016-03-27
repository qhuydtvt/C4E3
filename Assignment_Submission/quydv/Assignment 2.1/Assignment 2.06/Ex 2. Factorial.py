def factorial_calculate(x):
    factorial = 1
    for i in range(1, x+1):
        factorial *= i
    return factorial

num = int(input("Enter a number: "))
print(factorial_calculate(num))

