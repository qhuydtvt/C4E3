from turtle import *
color('red','yellow')
begin_fill()
i = 4
while i < 10 :
    a = 0
    while a < i:
        if a==0:
            fd(100)
            left(360/i)
        else:
            fd(100)
            left(360/i)
        a = a + 1
    i = i + 1
end_fill()
    
