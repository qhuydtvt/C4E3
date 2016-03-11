def multiply(p):
    multiply=1
    for x in p:
        multiply=multiply*x
    return multiply
h=input('please enter your list?')
p=[int(x) for x in h.split()]
print(multiply(p))
        
