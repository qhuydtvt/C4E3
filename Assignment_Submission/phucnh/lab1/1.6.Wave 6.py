from turtle import *
import turtle
color('green', 'yellow')
begin_fill()
i=0
while True:
    re_ben=input("Ban re phai hay trai?")
    if re_ben=="right":
        right(60)
        forward(100)
    elif re_ben=="left":
        left(60)
        forward(100)
end_fill()
done()
