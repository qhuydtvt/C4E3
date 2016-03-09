from turtle import*
showturtle()
i=4
while i<10:
    while True:
        pencolor("red")
        fd(100)
        lt(360/i)
        pencolor("blue")
        fd(100)
        lt(360/i)
        if abs(pos()) < 1:
            break
    i=i+1
