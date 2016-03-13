#0,1,2,3,4,5,6
range1 = range(0, 7)
my_list = []
my_list.extend(range1)
print('range1', my_list)


#1,4,7,10
a = 0
x = 1
while a < 4:
    x += 3
    a += 1
range2 = range(1, x, 3)
my_list = []
my_list.extend(range2)
print('range2', my_list)


#5,4,3,2,1
range3 = range(1, 6)
my_list = []
my_list.extend(range3)
my_list.reverse()
print('range3', my_list)


#6,4,2,0,-2
b = 0
y = -2
while b < 5:
    y += 2
    b += 1
range4 = range(-2, y, 2)
my_list = []
my_list.extend(range4)
my_list.reverse()
print('range4', my_list)
