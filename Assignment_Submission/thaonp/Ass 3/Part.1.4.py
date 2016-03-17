import math
from turtle import*  
i=0
color('white','red')
begin_fill()
l = ( 100**2 + 100**2)**0.5
alfa = math.atan2(100, 100) 
alfa = math.degrees(alfa)
alfa = 180.0 - alfa 
forward(200)
left(alfa)
forward(l)
left(2*(180-alfa))
forward(l)
end_fill()
pencolor('black')
lt(135)
while i<=3:
    forward(200)
    right(90)
    i=i+1
penup()
fd(180)
right(90)
fd(75)
right(90)
color('white', 'yellow')
begin_fill()
j=0
while j<=3:
    forward(50)
    right(90)
    j=j+1
end_fill()
fd(150)
lt(90)
color('white','blue')
penup()
fd(20)
pendown()
begin_fill()
fd(105)
lt(90)
fd(50)
lt(90)
fd(105)
lt(90)
end_fill()

