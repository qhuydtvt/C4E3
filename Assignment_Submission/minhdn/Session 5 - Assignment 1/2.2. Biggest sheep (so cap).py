sheep_list = [5, 7, 300, 90, 24, 50, 75]
print('Hello, my name is Minh and these are my sheep sizes \n', sheep_list)

i = 0
n = sheep_list[0]
x = len(sheep_list) - 1

while i < x:
    if n < sheep_list[i+1]:
        n = sheep_list[i+1]

    i = i + 1

if n < sheep_list[x]:
    n = sheep_list[x]
      
print(str.format('Now my biggest sheep has size {0} let\'s shear it', n))
