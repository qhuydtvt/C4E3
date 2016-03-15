from turtle import *

def tamgiac():
    for i in range(3):
        forward(250)
        left(120)
        
def tugiac():
    for i in range(4):
        forward(250)
        left(90)

def ngugiac():
    for i in range(5):
        forward(250)
        left(72)

hinh=input("ban muon ve hinh gi ")
if hinh=="tam giac":
    tamgiac()
elif hinh=="tu giac":
    tugiac()
elif hinh=="ngu giac":
    ngugiac()
    
