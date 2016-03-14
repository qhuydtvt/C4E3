#3.  Write a Python program to compute the distance between two points

import math

def khoangcach(x1,x2,y1,y2):
   return math.sqrt( (x2 - x1)**2 + (y2 - y1)**2 )

x1 = int(input("nhap toa do A voi Ox la "))
x2 = int(input("nhap toa do A voi Oy la "))
y1 = int(input("nhap toa do B voi Ox la "))
y2 = int(input("nhap toa do B voi Oy la "))

print(str.format("Khoang cach giua A({0},{1}) va B({2},{3}) la {4}",x1,x2,y1,y2,khoangcach(x1,x2,y1,y2)))
