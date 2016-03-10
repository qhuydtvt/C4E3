

#1
flock=[5,7,300,90,24,50,75]
print ("Hello, my name is Hiep and these are my ship sizes \n",flock)

#2
flock_max=max(flock)
print ("Hello, my biggest sheep has size",flock_max,"let's shear it")

#3
max_index=flock.index(flock_max)
flock[max_index]=8
print ("After shearing, here is my flock \n", flock)

#4
i=0
for sheep in flock:
    flock[i]=flock[i]+50
    i=i+1
print("One month has passed, now here is my flock \n",flock)
flock_max=max(flock)

#5
print("\n\n#5")

def tang_50():
    i=0
    for sheep in flock:
        flock[i]=flock[i]+50
        i=i+1
    print("One month has passed, now here is my flock \n",flock)

def xen_max():
    flock_max=max(flock)
    print ("Now my biggest sheep has size",flock_max,"let's shear it")
    max_index=flock.index(flock_max)
    flock[max_index]=8
    print ("After shearing, here is my flock \n", flock)
    
def one_month(month):
    x=1
    while x<=month:
        print("\nMONTH",x)
        tang_50()       
        xen_max()
        x=x+1

flock=[5,7,300,90,24,50,75]
print ("Hello, my name is Hiep and these are my ship sizes \n",flock)
one_month(3)

#6
print("\n\n#6")

flock=[5,7,300,90,24,50,75]
print ("Hello, my name is Hiep and these are my ship sizes \n",flock)
xen_max()
one_month(2)

print("MONTH",3)
tang_50()
total=0
for sheep in flock:
    total=total+sheep
print("My flock has size in total:",total)
print(str.format("I would get {0} * 2$ = {1}$",total, total*2))

        
