from turtle import *
color('green', 'yellow')
begin_fill()
while True:
    circle(100)
    if abs(pos()) < 1:
        break
end_fill()
done
