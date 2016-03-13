from turtle import *
import turtle

def coordinates(x1,y1,x2,y2):
    distance = ((y2 - y1)**2 + (x2 - x1)**2)**(1/2)
    return distance

A = input("Enter the coordinates of the first point using comma as delimiter: ")
B = input("Enter the coordinates of the second point using comma as delimiter: ")
A = [int(x) for x in A.split(",")]
B = [int(x) for x in B.split(",")]

x1 = int(A[0])
y1 = int(A[1])
x2 = int(B[0])
y2 = int(B[1])

print("The distance between the two points is:", coordinates(x1, y1, x2, y2))
