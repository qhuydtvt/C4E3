def distance(xA,yA,xB,yB):
    return ((xA-xB)**2+(yA-yB)**2)**0.5
xA=int(input('Enter xA= '))
yA=int(input('Enter yA= '))
xB=int(input('Enter xB= '))
yB=int(input('Enter yB= '))
print(str.format('The distance between A and B is {0}',distance(xA,yA,xB,yB)))
