from turtle import *

while True:
    n = str(input("Go left or right? "))
    if n == "1":
        right(60)
        forward(100)
    elif n == "0":
        left(60)
        forward(100)

