from turtle import *
import turtle
color('green', 'yellow')
begin_fill()
i=0
while i<10:
    forward(i*3)
    penup()
    forward(10)
    pendown()
    i=i+1
end_fill()
done()
