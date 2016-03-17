n=[int(x) for x in input('Coordinates of two point in order(x1,y1,x2,y2):').split()]
def confuse(x1,y1,x2,y2):
    a = ((n[0]-n[2])**2 + (n[1]-n[3])**2)**0.5
    print('The distance between two points is:',a)
    return a

confuse(n[0],n[1],n[2],n[3])
