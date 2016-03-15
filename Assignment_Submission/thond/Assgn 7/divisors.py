def div():
    n = int(input("Enter a number: "))
    l = []
    for i in range(1,n):
        if (n%i) == 0:
            l.append(i)
    return print("All the divisors of", n, "are", l)
    
div()
