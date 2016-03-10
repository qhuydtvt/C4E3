# bai 5.1
# 5.1.1
list_color = ['Blue', 'Red', 'Black' , 'Brown' , 'Yellow',]
print(list_color)
#5.1.2
print(str.format('list_color : {}', list_color[3]))
#5.1.3
i= int(input('Enter a number from 0 - 5 : '))
print(str.format('Your color : {0}', list_color[i]))
#5.1.4
print(list_color)
for color in list_color:
    print(color)
#5.1.5
    
while True:
    n_nhap = input('What is your favorite color ? ')
    i = 0
    while True:
        if i >len(list_color):
            print('Sorry , i could not find your color')
            break
        elif color_list[i]==n_nhap: 
            print('your color is at ', i, ' in my list of color')
            break
        i += 1
                
