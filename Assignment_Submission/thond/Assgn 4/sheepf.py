sheepn = [1, 20, 30,100, 150,250,300, 175,275, 500]

print("Hello, my name is Tho and these are my sheep sizes",sheepn)    
month = int(input("How many months have passed?"))
i = 0 
while i < month:
    print("MONTH", i +1)
    sheep2 = [i +50 for i in sheepn]
    print("One month has passed, now here is my flock",sheep2)
    m = max(sheep2)
    print("Now my biggest sheep has size",m,"Let's shear it.")
    b = sheep2.index(m)
    sheep2[b]=8
    print("After shearing, here is my flock",sheep2)
    sheepn = sheep2
    i += 1


s = 0
for n in sheepn:
    s += n
print("My flock size total is:", s)
d = s*2
print("I would get", s,"*2 =",d)
