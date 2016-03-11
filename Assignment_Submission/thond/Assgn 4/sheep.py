sheep = [1, 20, 30,100, 150,250,300, 175,275, 500]
print("Hello, my name is Tho and these are my sheep sizes",sheep)    

n = max(sheep)
print("Now my biggest sheep has size",n,"Let's shear it.")

a = sheep.index(n)
sheep[a]=8
print("After shearing, here is my flock",sheep)

sheep1 = []
for i in sheep:
    y = i + 50
    sheep1.append(y)
print("One month has passed, now here is my flock",sheep1)




