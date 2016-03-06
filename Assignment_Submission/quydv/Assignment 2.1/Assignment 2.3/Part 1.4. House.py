from turtle import *
import turtle

turtle.speed(5)
fd(200)
left(90)
fd(200)
left(45)

#ve mai nha
color('red')
begin_fill()
fd(200 * 2 ** (1/2) / 2)
left(90)
fd(200 * 2 ** (1/2) / 2)
left(135)
fd(200)
end_fill()

color('black')
left(180)
fd(200)
left(90)
fd(200)
left(90)
fd(30)

#ve cua
color('blue')
begin_fill()
i1 = 0
while i1 < 2:
    fd(60)
    left(90)
    fd(100)
    left(90)
    i1 = i1 + 1
end_fill()

penup()
left(90)
fd(120)
right(90)
fd(100)
pendown()

#ve cua so
color('yellow')
begin_fill()
i2 = 0
while i2 < 2:
    fd(50)
    left(90)
    fd(50)
    left(90)
    i2 = i2 + 1
end_fill()
