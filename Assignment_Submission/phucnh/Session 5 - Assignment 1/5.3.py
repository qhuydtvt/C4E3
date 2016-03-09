def print_range(ten,x,y,z):
    my_range=range(x,y,z)
    range_list=[]
    range_list.extend(my_range)
    print(ten, range_list)

print_range("range1",0,7,1)
print_range("range2",1,11,3)
print_range("range3",5,0,-1)
print_range("range4",6,-3,-2)
