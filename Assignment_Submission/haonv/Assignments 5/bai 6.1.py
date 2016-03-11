n = input('enter a list of number : ')
num_list = [int(x) for x in n.split()]
i = 1
for a in num_list:
    i *= a
print('result' , i)

