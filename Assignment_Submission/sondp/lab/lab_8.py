from turtle import *
while True:
 n=input("Tam giac or hinh vuong or ngu giac: ")
 i=0
 if n=="tam giac":
    while i<3:
     right(120)
     forward(60)
     i=i+1
 elif n=="hinh vuong":
    while i<4:
     right(90)
     forward(60)
     i=i+1
 elif n=="ngu giac":
    while i<5:
        forward(100)
        left(72)
        i=i+1
