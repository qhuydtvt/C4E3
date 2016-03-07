import turtle
from turtle import *

i = 0
x = 5
while i < 10:
    forward(x)
    penup()
    forward(x)
    x = x + 1
    pendown()
    forward(x)
    i = i + 1
