my_color=['Blue','red','green','yellow','purple']
print('my color list\n',my_color)
print('color_list at index 3: ',my_color[2])
i=int(input('enter a number from 0-4: '))
print('Your color ', my_color[i])
print(my_color)
for h in my_color:
    print(h)
a=input('what is your favorite color?')
for h in my_color:
    i=my_color.index(h)
    if h==a:
        print('your color is at ', i, ' in my list of color')
        break
    else:
        if i==len(my_color)-1:
            print('Sorry, i can not find your color')
    
    

