def get_divisor(x):
    list_of_divisor = []
    for i in range(1,x+1):
        if x % i == 0:
            list_of_divisor.append(i)
    return list_of_divisor

num = int(input("Enter a number: "))
print(str.format("All of the divisors of {0} are: {1}",num, get_divisor(num)))
