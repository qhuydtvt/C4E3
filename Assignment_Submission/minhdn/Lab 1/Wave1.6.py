from turtle import *

while True:
    n = str(input("Go left or right? "))
    if n == "right":
        right(60)
        forward(100)
    elif n == "left":
        left(60)
        forward(100)

