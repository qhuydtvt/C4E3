from turtle import *
begin_fill()
n=4
while n<10:
    i=0
    while i<n:
        if i%2==0:
            color('red', 'white')
            forward(100)
            left(360/n)
            i=i+1
        else:
            color('blue', 'white')
            forward(100)
            left(360/n)
            i=i+1  
    n=n+1
end_fill()
