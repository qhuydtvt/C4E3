from turtle import *
import turtle

i = 0
angle_num = 4
triangle_num = 2
while i < 6:
    angle = 180 * triangle_num / angle_num
    while True:
        color('red')
        begin_fill()
        fd(100)
        color('blue')
        left(180 - angle)
        fd(100)
        left(180 - angle)
        if abs(pos()) < 1:
            angle_num = angle_num + 1
            triangle_num = triangle_num + 1
            break
    i = i + 1

#k hieu sao cu khi nao so goc = le? thi no lai to lai mot luot?
