input_list = input("Enter a list of number using space as delimeter: ")
list_of_num = [int(x) for x in input_list.split()]
list_of_even = [x for x in list_of_num if x % 2 == 0]
print("the even numbers:", list_of_even)
