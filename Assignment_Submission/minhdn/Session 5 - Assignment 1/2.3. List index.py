flock = [5, 7, 300, 90, 24, 50, 75]
print('Hello, my name is Minh and here is my flock \n', flock)

x = max(flock)
print(str.format('Now my biggest sheep has size {0} let\'s shear it', x))

n = flock.index(x)
flock[n] = 8
print('After shearing, here is my flock \n', flock)
