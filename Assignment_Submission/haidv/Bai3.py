from turtle import*
i=4
while i<10:
    a=0
    while a<i:
        if a%2==0:
            color('red')
            fd(100)
            left(360/i)
        else:
            color('blue')
            fd(100)
            left(360/i)
        a=a+1
    i=i+1

