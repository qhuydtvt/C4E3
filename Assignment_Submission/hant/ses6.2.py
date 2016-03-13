n=int(input("enter a number:"))
m=range(1,n+1)
while True:
    if n==0:
        print("the factorial of a number is: 1")
        break
    elif n<0:
        print("there is no factorial of a nonegative number")
        break
    tich=1
    for a in m:
        tich=tich*a
    print("the fatorial of the number is:",tich)
    break
