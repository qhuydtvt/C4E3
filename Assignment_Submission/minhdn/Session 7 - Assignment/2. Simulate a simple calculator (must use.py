def math(x, y, calculator):
    if calculator == '+':
        return x + y
    elif calculator == '-':
        return x - y
    elif calculator == '*':
        return x * y
    elif calculator == '/':
        return x / y
    else:
        return 'Error'

x = int(input('Enter x: '))
calculator = input('Enter calculator: ')
y = int(input('Enter y: '))

print(str.format('{0} {1} {2} = {3}', x, calculator, y, math(x, y, calculator)))
        
