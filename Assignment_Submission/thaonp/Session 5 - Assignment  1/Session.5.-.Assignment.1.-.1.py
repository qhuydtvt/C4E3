#1.1
color_list=['Blue','Red', 'Black', 'Pink', 'Brown', 'Yellow']
print(str.format('My color list \n{0}',color_list))
#1.2
print(str.format('Color_list at index 3: {0}', color_list[3]))
#1.3
i=int(input('Enter a number from 0-5: '))
print(str.format('Your color: {0}', color_list[i]))
#1.4
print(color_list)
for n in color_list:
    print(n)
1.5
fav=input('What is your favorite color? ')
i=0
for color in color_list:
    if fav!=color:
        i=i+1
    else:
        print ("Your color is at index",i,"in my list")
        break
    if i==len(color_list)-1:
        print ("Sorry, I could not find your color")
