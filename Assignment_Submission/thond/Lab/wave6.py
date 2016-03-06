while True:
    a = input("Left or right or forward?")
    from turtle import *
    if a == "right":
        right(60)
        fd(100)
    elif a == "left":
        left (60)
        fd(100)
    elif a == "foward":
        fd(100)

