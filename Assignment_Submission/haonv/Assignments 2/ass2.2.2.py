from turtle import *
color('blue', 'yellow')
begin_fill()
while True:
    forward(200)
    right(120)
    if abs(pos()) < 1:
        break
end_fill()
done()