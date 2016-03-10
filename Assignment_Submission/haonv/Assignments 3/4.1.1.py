from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    left(30)
    fd(100)
    right(60)
    fd(100)
    right(120)
    fd(100)
    right(60)
    fd(100)
    left(30)
    fd(100)
    right(60)
    if abs(pos()) < 1:
        break
end_fill()


