from turtle import *

a = str(input("Ban muon ve hinh gi? "))
if a == "tam giac":
    while True:
        forward(100)
        left(120)
        if abs(pos()) < 1:
            break
    
elif a == "vuong":
    while True:
        forward(100)
        left(90)
        if abs(pos()) < 1:
            break
    
elif a == "ngu giac":
    while True:
        forward(100)
        left(60)
        if abs(pos()) < 1:
            break
    
