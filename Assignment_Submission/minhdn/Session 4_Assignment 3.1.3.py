from turtle import *
showturtle()

i = 4
while i < 10:
    while True:
        pencolor('red')
        forward(50)
        left(360/i)
        pencolor('blue')
        forward(50)
        left(360/i)
        if abs(pos()) < 1:
            break
        
    i = i + 1


