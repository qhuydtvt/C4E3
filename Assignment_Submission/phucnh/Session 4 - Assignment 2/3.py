from turtle import *
import turtle
color('green', 'yellow')
begin_fill()
while True:
    turtle.circle(100)
    if abs(pos()) < 1:
        break
end_fill()
done()
