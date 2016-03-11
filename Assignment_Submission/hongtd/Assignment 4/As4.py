#1
##import turtle
##turtle.color("red")
##i=0
##while i<4:
##    turtle.right(30)
##    turtle.backward(50)
##    turtle.left(60)
##    turtle.backward(50)
##    turtle.left(120)
##    turtle.backward(50)
##    turtle.left(60)
##    turtle.backward(50)
##    turtle.left(60)
##    i=i+1

#2
##import turtle
##i=0
##n=30
##turtle.color("green")
##while i<10:
##    turtle.circle(n)
##    i=i+1
##    n=n+30

#3
##import turtle
##n=4
##while n<10:
##    i=0
##    while i<n:
##        if i%2==0:
##            turtle.forward(20)
##            turtle.left(360/n)
##            turtle.color("red")
##        else:
##            turtle.forward(20)
##            turtle.left(360/n)
##            turtle.color("blue")
##        i=i+1
##    n=n+1
##

#4
##import turtle
##i=0
##while i<4:
##    turtle.forward(150)
##    turtle.right(90)
##    i=i+1
##    
##turtle.color("red")
##turtle.begin_fill()    
##turtle.left(60)
##turtle.forward(150)
##turtle.right(120)
##turtle.forward(150)
##turtle.end_fill()
##
##turtle.penup()
##turtle.right(30)
##turtle.forward(150)
##turtle.right(90)
##turtle.forward(100)
##turtle.pendown()
##
##turtle.color("blue")
##turtle.begin_fill()
##turtle.right(90)
##turtle.forward(100)
##turtle.right(90)
##turtle.forward(30)
##turtle.right(90)
##turtle.forward(100)
##turtle.end_fill()
##
##turtle.penup()
##turtle.backward(120)
##turtle.left(90)
##turtle.forward(30)
##turtle.color("yellow")
##turtle.begin_fill()
##turtle.pendown()
##turtle.forward(30)
##turtle.right(90)
##turtle.forward(30)
##turtle.right(90)
##turtle.forward(30)
##turtle.right(90)
##turtle.forward(30)
##turtle.end_fill()

#5
##n=int(input("Enter a number")
##i=n-1
##if n>1:
##      if (n%i)==0:
##          print("not a prime number")
##      else:
##          print("prime number")
##else:
##      print("not a prime number")

#6     
n=int(input("Enter a number")
i=0
x=0
while True:
      if x<n:
          i=i+1
          if (n%i)==0 and i<n:
              x=x+1
              if x==n:
                  print("perfect")
      else:
          print("not perfect")
    
      

    


