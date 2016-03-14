flock = [5, 7, 300, 90, 24, 50, 75]
print('Hello, my name Minh and here is my flock', flock)

##i = 0
##for sheep in flock:
##    flock[i] = flock[i] + 50
##    i += 1
##print('MONTH 1: \nOne month has passed, now here is my flock \n', flock)
##
##print(str.format('Now my biggest sheep has size {0} let\'s shear it', max(flock)))
##
##flock[flock.index(max(flock))] = 8
##print('After shearing, here is my flock \n', flock)


def grow():
    i = 0
    for sheep in flock:
        flock[i] = flock[i] + 50
        i += 1
    print('One month has passed, now here is my flock \n', flock)

def biggest():
    print(str.format('Now my biggest sheep has size {0} let\'s shear it', max(flock)))

def shear():
    flock[flock.index(max(flock))] = 8
    print('After shearing, here is my flock \n', flock)

def month(a):
    x = 1
    while x <= a:
        print("\nMONTH", x, ':')
        grow()
        biggest()
        shear()
        x += 1
        
month(4)
    
    
    

    
