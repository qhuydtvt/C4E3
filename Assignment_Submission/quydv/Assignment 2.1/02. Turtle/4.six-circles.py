import turtle
from turtle import *
color("blue")
begin_fill()
turtle.speed(0)

circle = 0
while circle < 6:
    turtle.circle(10)
    right(60)
    circle = circle + 1

color("white")
right(90)
forward(200)

color("black")
circle = 0
while circle < 36:
    turtle.circle(30)
    right(10)
    circle = circle + 1
