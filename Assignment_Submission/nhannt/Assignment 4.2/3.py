from turtle import *
color('green', 'yellow')
begin_fill()
while True:
    forward(1)
    left(1)
    if abs(pos()) < 1:
        break
end_fill()
done()
