from turtle import *

n = 4

while n < 10:
    i = 0
    while i < n:
        if i%2 == 0: 
            pencolor('red')
            forward(50)
            left(360/n)
            
        else:
            pencolor('blue')
            forward(50)
            left(360/n)

        i = i + 1
        
    n = n + 1


