from turtle import *
i=0
speed (0)
while i < 4:
    fd(200)
    left(90)
    i = i+1
goto(30,0)
color ("blue")
begin_fill()
i=0
while i < 2:
    fd (50)
    left(90)
    fd (100)
    left(90)
    i = i +1
end_fill()
penup()
goto (200,200)
color('red')
begin_fill()
left(135)
fd((100*2**.5))
left(90)
fd((100*2**.5))
left(135)
fd(200)
end_fill()
penup()
goto(125,125)
color('yellow')
begin_fill()
i = 0
while i <4:
    fd(50)
    left(90)
    i = i +1
end_fill()
