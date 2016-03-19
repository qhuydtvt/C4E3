x = int(input("Enter a number: "))
def factoriall(n):
    l = list(range(1, n+1))
    p = 1
    for i in l:
        p *= i
    return p
print("The factorial of", x, "is", factoriall(x))
    
