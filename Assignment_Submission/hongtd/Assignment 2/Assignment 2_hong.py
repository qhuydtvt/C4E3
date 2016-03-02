#1:type(value)
#hehe@="abcxyz"
#while="abcxyz"
#1234="abcxyz"


#2
n=input("radius?")
i=3.14*int(n)
print("Area=", i)

#3
n=input("Enter the temperature in Celcius?")
k=5*int(n)
print(k)

#4
n=input("How many B bacterias are there?")
i=input("How much time will we wait?")
k=int(n)*int(i)/2
print("After", i, "minutes we would have", k, "bacterias")



#5
a, b = 0, 1
n=0
while n<5:
    print("Month",n, ":", b, "pairs of rabbits")
    a, b = b, a+b
    n=n+1
