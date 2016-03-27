from turtle import *
import turtle

shape = input('What shape?')
if shape == "triangle":
    forward(100)
    left(120)
    forward(100)
    left(120)
    forward(100)
elif shape == "square":
    i = 0
    while i < 4:
        forward(100)
        left(90)
        i = i + 1
else:
    i = 0
    while i < 5:
        forward(100)
        left(72)
        i = i + 1
