def draw(x,y,l,a):
    import turtle
    
    n = turtle
    n.penup()
    n.goto(x,y)
    n.pendown()
    i = 0
    while i < a:
        n.fd(l)
        n.left(360/a)
        i += 1
    
draw(0,0,50,3)
draw(101,0,50,4)
draw(201,0,50,5)
