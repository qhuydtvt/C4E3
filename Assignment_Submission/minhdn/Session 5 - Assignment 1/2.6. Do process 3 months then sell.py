flock = [5, 7, 300, 90, 24, 50, 75]
print('Hello, my name is Minh and here is my flock \n', flock)

def grow():
    i = 0
    for sheep in flock:
        flock[i] += 50
        i += 1
    print('One month has passed, now here is my flock \n', flock)

def biggest():
    print(str.format('Now my biggest sheep has size {0} let\'s shear it', max(flock)))

def shear():
    flock[flock.index(max(flock))] = 8
    print('After shearing, here is my flock \n', flock)

biggest()
shear()

def month(a):
    x = 1
    while x <= a:
        print('\nMONTH', x, ':')
        grow()
        biggest()
        shear()
        x += 1
month(2)

print('\nMONTH', 3, ':')
grow()

tong = 0
for sheep in flock:
    tong += sheep
tien = tong * 2
print('My flock has size in total:', tong)
print(str.format('I would get {0} * 2$ = {1}$', tong, tien)) 
    
    
    
