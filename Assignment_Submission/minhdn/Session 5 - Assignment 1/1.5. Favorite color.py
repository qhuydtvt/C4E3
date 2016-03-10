color_list = ['Blue', 'Red', 'White', 'Yellow', 'Orange', 'Purple']

n = input('What is your favorite color? ')
i = 0

for a in color_list:
    if i <= len(color_list):
        if n == a:
            print(str.format('Your color is at index {0} in my list', i))
            break
        else:
            i = i + 1

    if i == (len(color_list) - 1):
        print('Sorry I coult not find your color')
        
    
