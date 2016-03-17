def dis():
    import turtle
    t = turtle
    n = input("Enter the first point's coordinate (x,y): ")
    l = n.split(",")
    a = []
    for i in l:
        i = int(i)
        a.append(i)
    m = input("Enter the second point's coordinate (x,y): ")
    k = m.split(",")
    b = []
    for j in k:
        j = int(j)
        b.append(j)
    dis = ((b[0]-a[0])**2+(b[1]-a[1])**2)**.5
    print("The distance between your two points is", dis)
dis()
