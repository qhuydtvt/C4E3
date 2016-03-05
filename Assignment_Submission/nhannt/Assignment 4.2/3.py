from turtle import *
color('green', 'yellow')
begin_fill()
while True:
    forward(100)
    left(90)
    if abs(pos()) < 1:
        break
end_fill()
done()
