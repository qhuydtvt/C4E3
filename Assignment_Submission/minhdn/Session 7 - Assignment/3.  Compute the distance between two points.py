def distance():
    AB = ((xA-xB)**2 + (yA-yB)**2)**0.5
    return AB

xA = int(input('Enter xA: '))
yA = int(input('Enter yA: '))
xB = int(input('Enter xB: '))
yB = int(input('Enter yB: '))

print('The distance between A and B is:', distance())
