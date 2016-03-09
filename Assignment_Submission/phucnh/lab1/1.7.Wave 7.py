from turtle import *
import turtle
color('green', 'yellow')
begin_fill()
i=0

hinh=input("Ban thich hinh gi? Tam giac, vuong, luc giac?")
while True:
    if hinh=="tam giac":
        forward(90)
        left(120)
                       
    elif hinh=="vuong":
        forward(90)
        left(90)
                        
    elif hinh=="ngu giac":
        forward(90)
        left(72)
                        
    if abs(pos()) < 1:
        break     
end_fill()
done()
