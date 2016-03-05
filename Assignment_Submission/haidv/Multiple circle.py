import turtle
turtle.color('red','green')
turtle.bgcolor('yellow')
turtle.begin_fill()
for angle in range (0,360,10):
    turtle.seth(angle)
    turtle.circle(100)
turtle.end_fill()
