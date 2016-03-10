from turtle import *

while True:
    forward(100)
    right(90)
    if abs(pos()) < 1:
        break

color('red')
begin_fill()
forward(100)
left(135)
forward(50*(2**0.5))
left(90)
forward(50*(2**0.5))
end_fill()
done

penup()
left(45)
forward(100)
left(90)
forward(15)

pendown()
left(90)
color('blue')
begin_fill()
i = 0
while i < 2:
    forward(50)
    right(90)
    forward(25)
    right(90)
    i = i + 1
end_fill()
done

penup()
forward(80)
right(90)
forward(45)

pendown()
color('yellow')
begin_fill()
i = 0
while i < 4:
    forward(25)
    right(90)
    i = i + 1
end_fill()
done





    


