list0 = input('Import a list number: ')
list1 = list0.split()
list2 = [int(x) for x in list1]

list3 = [i for i in list2 if i%2 == 0]
print('The even number:', *list3)


