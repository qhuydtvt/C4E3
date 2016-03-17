n = [int(x) for x in input('input point one and point two:').split()]
m= input('operation:')
def calculate(number1,number2,operation):
    if m=='add':
        a=n[0]+n[1]
        print(str.format('{0} + {1} = {2}',n[0],n[1],a))
        return a
    if m=='subtract':
        a=n[0]-n[1]
        print(str.format('{0} - {a} = {2}',n[0],n[1],a))
        return a
    if m=='multiply':
        a=n[0]*n[1]
        print(str.format('{0} x {1} = {2}',n[0],n[1],a))
        return a
    if m=='divede':
        a=n[0]+n[1]
        print(str.format('{0} : {1} = {2}',n[0],n[1],a))
        return a
calculate(n[0],n[1],m)
