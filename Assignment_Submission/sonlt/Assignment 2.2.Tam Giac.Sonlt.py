from turtle import *
color('green','yellow')
begin_fill()
while True:
    forward(100)
    left(120)
    if abs(pos())<1:
        break
end_fill()
done()
