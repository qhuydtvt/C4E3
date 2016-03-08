from turtle import *

i = 0
n = 5
while i < 10:
    
    pendown()
    forward(n)
    n = n + 1
    penup()
    forward(10)
    i = i + 1
