from turtle import*
i=1
while i<5:
    fd(100)
    right(90)
    i=i+1
color('red','red')
begin_fill()
left(45)
fd(100/(2)**0.5)
right(90)
fd(100/(2)**0.5)
end_fill()
penup()
goto(20,-100)
pendown()
left(135)
color('blue','blue')
begin_fill()
fd(50)
right(90)
fd(30)
right(90)
fd(50)
end_fill()
penup()
goto(70,-40)
pendown()
left(90)
i=0
color('yellow','yellow')
begin_fill()
while i<5:
    fd(20)
    left(90)
    i=i+1
end_fill()
hideturtle()

    
