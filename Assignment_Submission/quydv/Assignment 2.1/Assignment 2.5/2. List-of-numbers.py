###2.1.
flock_size = [13, 22, 88, 141, 20, 56, 72, 1000]
##print(flock_size)
##
###2.2.
##print(str.format("Now the biggest sheep in my flock is {0} in size, let's sheer him moahaha", max(flock_size)))
##
###2.3.
##flock_size[flock_size.index(max(flock_size))] = 8
##print("After shearing, the sheeps have the following sizes:", flock_size)
##
###2.4.
##for sheep in flock_size:
##        new_size = sheep + 50
##        flock_size[flock_size.index(sheep)] = new_size
##
##print(flock_size)

#2.5.
def growth():
    for sheep in flock_size:
        new_size = sheep + 50
        flock_size[flock_size.index(sheep)] = new_size

i = 1
while i < 5:
    growth()
    print(str.format("Month {0} has passed, now the sheeps have sizes of: {1}", i, flock_size))
    print(str.format("Now the biggest sheep in my flock is {0} in size, let's sheer him moahahaha", max(flock_size)))
    flock_size[flock_size.index(max(flock_size))] = 8
    print(str.format("After shearing, the sheeps have the following sizes: {0} \n", flock_size))
    i = i + 1

#2.6.
print("My flock has size in total:", sum(flock_size))
print(str.format("I would get {0} * 2$ = {1}$", sum(flock_size), sum(flock_size) * 2))
    
