from turtle import *
color('green','white')
begin_fill()
i=0
while i<360:
    while True:
        forward(1)
        right(1)
        if abs(pos())<1:
            break
    right(10)
    while True:
        forward(1)
        right(1)
        if abs(pos())<1:
            break
    i=i+1
end_fill()
done()
    
