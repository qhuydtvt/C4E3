import turtle
from turtle import *

i = 0
while i < 16:
    ask = input('wanna turn right or left or forward?')
    if ask == 'right':
        right(60)
        forward(100)
    elif ask == 'left':
        left(60)
        forward(100)
    else:
        forward(100)
    i = i + 1

