from turtle import *
n = 4
speed (0)
while True:
    if n < 10:
        color('red')
        fd(100)
        left(360/n)
        color ('blue')
        fd(100)
        left(360/n)
        if abs(pos())<1:
            n = n+1
        else:
            continue            
    else:
        break
