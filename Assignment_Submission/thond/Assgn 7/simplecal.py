def cal():
    n = input("Enter a calculation: ")
    m = n.split(" ")
    l = []
    for i in m:
        if i not in ['*', '+', '/', '-']:
            i = int(i)
        l.append(i)
    for i in l:
        if i == '*':
            print(l[0]*l[2])
        elif i == '+':
            print(l[0]+l[2])
        elif i == '-':
            print(l[0]-l[2])
        elif i == '/':
            print(l[0]/l[2])
cal()

