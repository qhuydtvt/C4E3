mysheepsize=[90,80,17,67,47,38,49,68]
print('hello, my name is Hai and these are ship sizes\n',mysheepsize)
i=0
while i<3:
    b=[]
    for h in mysheepsize:
        b.append(h+50)
    mysheepsize=b
    print('MONTH', i+1)
    print( 'one month has passed, now is my flock', mysheepsize)
    h=max(mysheepsize)
    print('now my biggest sheep has size',h,'lets shear it')
    t=mysheepsize.index(h)
    mysheepsize.insert(t,8)
    mysheepsize.remove(h)
    print('After shearing, here is my flock', mysheepsize)
    i=i+1
g=0
for h in mysheepsize:
    g=g+h
print('My flock has size in total:', g)
print('I would get', g*2)


