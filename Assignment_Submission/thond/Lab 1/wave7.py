while True:
    a = input("Triangle or square or pentagon?")
    from turtle import *
    if a == "triangle":
        reset()
        fd (100)
        right(120)
        fd(100)
        right (120)
        fd (100)
    elif a == "square":
        reset()
        fd(100)
        left (90)
        fd(100)
        left (90)
        fd(100)
        left (90)
        fd(100)
        left (90)
    elif a == "pentagon":
        reset()
        fd(100)
        left(60)
        fd(100)
        left(60)
        fd(100)
        left(60)
        fd(100)
        left(60)
        fd(100)
        left(60)
        fd(100)
        left(60)




