from turtle import *
begin_fill()
u=4
while u<10:
    i=0
    while i<u:
        if i%2==0:
            color('red', 'white')
            fd(100)
            left(360/u)
            i=i+1
        else:
            color('blue', 'white')
            fd(100)
            left(360/u)
            i=i+1  
    u=u+1
end_fill()
done()
