#1
flock=[13,12,2000,69,420,50,75]
print ('Hello, my name is Thao and these are my sheep sizes \n',flock)

#2
m=max(flock)
print ('Hello, my biggest sheep has size', m,'lets shear it')

#3
index=flock.index(m)
flock[index]=8
print ('After shearing, here is my flock \n', flock)

#4
i=0
for sheep in flock:
    flock[i]=flock[i]+50
    i=i+1
print("One month has passed, now here is my flock \n",flock)

#5
def grow():
    i=0
    for sheep in flock:
        flock[i]=flock[i]+50
        i=i+1
    print("One month has passed, now here is my flock \n",flock)

def shear():
    m=max(flock)
    print ("Now my biggest sheep has size",m,"let's shear it")
    index=flock.index(m)
    flock[index]=8
    print ("After shearing, here is my flock \n", flock)
    
def one_month(month):
    x=1
    while x<=month:
        print("\nMONTH",x)
        grow()       
        shear()
        x=x+1
        
one_month(6)

#6
total=0
for sheep in flock:
    total=total+sheep
print("My flock has size in total:",total)
print(str.format("I would get {0} * 2$ = {1}$",total, total*2))
