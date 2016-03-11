#2.1
flock_size=[6,96,9,6969,696,96,69,9966,669,996]
print(str.format("hello, my name is Tu and these are my ship sizes \n {0}",flock_size)) 
###2.2
##print(str.format("Now my biggest sheep has size {0} let's shear it",max(flock_size)))
###2.3
##flock_size[flock_size.index(max(flock_size))]=8
##print(str.format("After shearing, here is my flock:\n{0}",flock_size))
#2.4
def growth():
    for sheep in flock_size:
        new_size = sheep +50
        flock_size[flock_size.index(sheep)] = new_size
##print(str.format("One month has passed, now here is my flock: \n{0}",flock_size))
#2.5
i=1
while i<5:
    growth()
    print(str.format("MONTH{0}:\nOne month has passed, now here my flock:\n{1}",i,flock_size))
    print(str.format("Now my biggest sheep has size {0} let shear it",max(flock_size)))
    flock_size[flock_size.index(max(flock_size))]=8
    print(str.format("After shearing, here is my flock:\n{0}",flock_size))
    i += 1
##em muon bai 2.4 de them "def growth"
#2.6
print(str.format("My flock has size in total:{0}",sum(flock_size)))
money=sum(flock_size)*2
print(str.format("I would get {0} * 2$ = {1}$",sum(flock_size),money))
print("Let's go to travel =))")
