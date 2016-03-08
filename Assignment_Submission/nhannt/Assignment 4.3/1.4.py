from turtle import *
i=0
while i<1:
    begin_fill()
    color('white', 'red')
    left(60)
    fd(200)
    right(120)
    fd(200)
    right(120)
    fd(200)
    i=i+1
    end_fill()
while i<5:
    begin_fill()
    pencolor('black')
    left(90)
    fd(200)
    i=i+1
    end_fill()
right(180)
fd(120)
right(90)
penup()
fd(20)
pendown()
begin_fill()
while i<9:
    color('white', 'yellow')
    fd(50)
    left(90)
    i=i+1
end_fill()
penup()
fd(180)
right(90)
fd(50)
right(90)
begin_fill()
color('white', 'blue')
fd(80)
left(90)
fd(50)
left(90)
fd(80)
left(90)
fd(50)
end_fill()
done()


