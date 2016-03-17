from turtle import *
m=4
while m<10:
    i=0
    while i<m:
        if i%2==0:
            pencolor('red')
            fd(100)
            left(360/m)
        else:
            pencolor('blue')
            fd(100)
            left(360/m)
        i=i+1
    m=m+1

