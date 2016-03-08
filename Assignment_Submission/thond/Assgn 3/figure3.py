from turtle import *
n = 4
speed (0)
while n < 10:
    i = 0
    while i < n:
        if i%2 == 0:
            color('red')
            fd(100)
            left(360/n)
        else:
            color('blue')
            fd(100)
            left(360/n)
        i = i + 1
    n = n + 1 
