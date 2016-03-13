def calculator(a,b,calculation):
    if calculation=="+":
        return a+b
    if calculation=="-":
        return a-b
    if calculation=="*":
        return a*b
    if calculation=="/":
        return a/b
a=int(input("Enter a= "))
b=int(input("Enter b= "))
calculation=input("Choose a calculation + - * / ")
print(str.format(" {0} {2} {1} is {3}",a,b,calculation,calculator(a,b,calculation)))
