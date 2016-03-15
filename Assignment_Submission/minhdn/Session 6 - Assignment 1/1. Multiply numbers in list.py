list0 = input('Input a list of number: ')
list1 = list0.split(' ')
list2 = [int(x) for x in list1]

result = 1
for n in list2:
    result *= n
print('Result:', result)
    
