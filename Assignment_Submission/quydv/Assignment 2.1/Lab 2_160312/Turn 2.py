import turtle
from turtle import *
##turtle.speed(3)
##def draw(x):
##    i = 180*(x-2)/x
##    for x in range(x):
##        fd(100)
##        left(180 - i)
##    
##shape = input("Pick a shape: triangle, square, pentagonal: ")
##if shape == "triangle":
##    shape = 3
##elif shape == "square":
##    shape = 4
##elif shape == "pentagonal":
##    shape = 5
##
##draw(int(shape))

##def dash(x):
##    for i in range(x):
##        fd(x*4)
##        penup()
##        fd(5)
##        pendown()
##        x += 2
##num = int(input("Enter a number: "))
##dash(num)

##def draw(x):
##    i = 180*(x-2)/x
##    for x in range (x):
##        fd(100)
##        left(180 - i)
##for i in range(6):
##    left(120)
##    penup()
##    fd(100)
##    pendown()
##    right(60)
##    draw(6)

string = "Quy"
new_list = []
for i in string:
    y = ord(i)
    new_list.append(y)

print(new_list)
letter_list = []
for i in new_list:
    letter = chr(i)
    letter_list.append(letter)

print(''.join(letter_list))
    
