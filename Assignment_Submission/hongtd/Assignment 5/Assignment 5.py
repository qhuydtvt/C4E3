###1
##name_list=["blue", "red", "black", "pink", "brown", "yellow"]
##print("My color list")
##print(name_list)
##
##x=name_list[3]
##print("color_list at index 3:", x)
##
##i=int(input("Enter a number from 0-5"))
##k=name_list[i]
##print("your color:", k)
##
##print(name_list)
##
##for name in name_list:
##    print(name)
##    
##a=input("whats ur favorite color")
##if a in name_list:
##    k=name_list.index(a)
##    print("ur color is at index", k, "in my list")
##else:
##    print("sr, cannot find ur color")

#2
##flock_number=["5", "7", "300", "90", "24", "50", "75"]
##print("hi, my name is abc and my sheep sizes")
##print(flock_number)
##x=max(flock_number)
##print("now my biggest sheep has size", x, "lets shear it")
##
##flock_number[flock_number.index(max(flock_number))]=8
##print("After shearing, here is my flock", flock_number)
##
##for sheep in flock_number:
##    new_size = int(sheep) + 50
##    flock_number[flock_number.index(sheep)] = new_size
##print(flock_number)
##
##
##
##i=1
##while i<5:
##    for sheep in flock_number:
##        new_size = int(sheep) + 50
##        flock_number[flock_number.index(sheep)] = new_size
##    print(str.format("Month {0} has passed, now the sheeps have size of: {1}", i, flock_number))
##    print(str.format("Now the biggest sheep in my flock is {0} in size, let's shear", max(flock_number)))
##    flock_number[flock_number.index(max(flock_number))] = 8
##    print(str.format("After shearing, the sheeps have the sizes: {0}", flock_number))
##    i = i + 1
##
##print("Total:", sum(flock_number))
##x=sum(flock_number)*2
##print("Revenue", x)
        
#3
range1 = (0, 1, 2, 3, 4, 5, 6)
range2 = (1, 4, 7, 10)
range3 = (5, 4, 3, 2, 1)
range4 = (6, 4, 2, 0, -2)
my_range=(range1, range2, range3, range4)
my_list=[]
my_list.extend(my_range)
print(my_list)

