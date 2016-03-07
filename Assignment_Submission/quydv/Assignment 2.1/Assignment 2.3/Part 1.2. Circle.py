from turtle import *
import turtle

color("green")
begin_fill()
turtle.speed(0)
i = 0
x = 10
while i < 10:
    turtle.circle(x)
    x = x + 10
    i = i + 1
