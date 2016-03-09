from turtle import*
color("white", "red")
begin_fill()
i=0
while i<3:
    fd(100)
    lt(120)
   
    i=i+1
end_fill()
color("black","white")
begin_fill()
rt(90)
i=0
while i<4:
    fd(100)
    lt(90)
    i=i+1
end_fill()
penup()
fd(100)
lt(90)
fd(20)
lt(90)
pendown()
color("white","blue")
begin_fill()
fd(60)
rt(90)
fd(30)
rt(90)
fd(60)
end_fill()
penup()
lt(90)
fd(10)
lt(90)
fd(60)
pendown()
color("white","yellow")
begin_fill()
i=0
while i<4:
    fd(20)
    rt(90)
    i=i+1
end_fill()
