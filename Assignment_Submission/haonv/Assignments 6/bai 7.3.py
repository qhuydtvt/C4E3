def distance(xa,ya,xb,yb):
    return ((xa-xb)**2+(ya-yb)**2)**0.5
xa = int(input('xa = : '))
ya = int(input('ya = : '))
xb = int(input('yb = : '))
yb = int(input('yb = : '))
print(str.format('between a nd b {0}' ,distance(xa,ya,xb,yb)))
