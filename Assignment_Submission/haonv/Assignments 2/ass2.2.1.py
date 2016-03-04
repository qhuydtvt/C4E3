# ve hinh vuong
from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    right(90)
    if abs(pos()) < 1:
        break
end_fill()
done()
