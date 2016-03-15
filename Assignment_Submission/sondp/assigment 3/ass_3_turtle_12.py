##1.turtle 2
from turtle import *
i=10
color("green","white")
while i<100:
circle(i+10)
 i=i+10
##2.turtle 1
from turtle import *
i=0
while i<4:
    color("black","white")
    left(90)
    forward(150)
    i=i+1
backward(90)
begin_fill()

color("blue","blue")
left(90)
forward(85)
left(90)
forward(40)
left(90)
forward(85)
end_fill()
right(90)
forward(20)
right(90)
forward(150)
right(45)
begin_fill()
color("white","red")
a=150/(2**0.5)
forward(a)
right(90)
forward(a)
end_fill()
left(45)
begin_fill()
color("black","white")
backward(20)
left(90)
penup()
backward(20)
pendown()
end_fill()
begin_fill()
color("yellow")
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
end_fill()



