###1
import turtle
turtle.right
turtle.forward(10)

#2
import turtle
turtle.right

turtle.forward(50)

turtle.right(90)

turtle.forward(30)

turtle.right(90)

turtle.forward(50)

turtle.right(90)

turtle.forward(30)
    
turtle.right(90)

#3
import turtle
i=0
while i<4:
    turtle.right
    turtle.forward(50)
    turtle.right(90)
    i=i+1

#4
import turtle
i=0
while i<10:
    turtle.forward(30)
    turtle.penup()
    turtle.forward(30)
    turtle.pendown()
    i=i+1

5
import turtle
i=0
n=100
while i<3:
    turtle.forward(n)
    turtle.penup()
    turtle.forward(n)
    turtle.pendown()
    n = n+100
    i=i+1
##    

#6
import turtle
while True:
    n=input("right or left")
    if n=="right":
        turtle.right(60)
        turtle.forward(100)
    elif n=="left":
        turtle.right(60)
        turtle.forward(100)
##    

#7

##1.F
##2.T
##3.T
##4.F
##5.F

#8
import datetime
x=datetime.datetime.now
n=input("Water is available or not?")
k=input("What time is it?")
if 5<int(k)<10 and n=="no":
    print("Pump is off")
elif 5<int(k)<10 and n=="yes":
    print("Pump is on")
elif (int(k)>10 or int(k)<5) and n=="no":
    print("Pump is off")
elif (int(k)>10 or int(k)<5) and n=="yes":
    print("Pump is off")
elif 20<int(k)<22 and n=="no":
    print("Pump is off")
elif 20<int(k)<22 and n=="yes":
    print("Pump is on")
elif (int(k)>22 or int(k)<20) and n=="no":
    print("Pump is off")
elif (int(k)>22 or int(k)<20) and n=="yes":
    print("Pump is off")


#9
while True: 
    n=int(input("enter a number"))
    if n%2==0:
        print("even")
    else:
        print('odd')
        break  
#10
while True:
    n=int(input("number?"))
    if (n%2)==0:
        print("even")
        if((n**(1/2))%2)==0:
        #rsq=n**0.5
        #if (rsq==(rsq//1))
            print("square")
            break
        else:
            print("not square")
    else:
        print("odd")
        break
    

#11

while True:
    n=input("enter your username:")
    if len(n)==0:
        print("must enter your username")
    elif n=="bighero6":
        while True:
            x=input("enter your password")
            if x=="codethechange":
                print("welcome to techkids")
                break
            elif x=="":
                print("must enter password")
            else:
                print("invalid password")
    else:
        print("invalid username")
    break
    
    


    

    
    
