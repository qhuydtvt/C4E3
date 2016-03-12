n=input("Enter a list of numbers: ")
list_of_num = [int(x) for x in n.split()]
list_of_even = [x for x in list_of_num if x % 2 == 0]
print('The even number: ',*list_of_even)
