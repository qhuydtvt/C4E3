input_num = input("Enter a list of number using comma as delimeter: ")
list_of_num = [int(x) for x in input_num.split(",")]

multiply_result = 1
for num in list_of_num:
    multiply_result *= num

print("result:", multiply_result)
