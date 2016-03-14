x = input("Enter a list of number(use space as buffer inbetween numbers): ")
def evenl(n):
    a = x.split(" ")
    l = [int(i) for i in a]
    k = []
    for b in l:
        if (b%2)==0:
            k.append(b)
    e = print("The even number: ", end=" ")
    for c in k:
        d = print(c, end =" ")
    return 
evenl(x)
