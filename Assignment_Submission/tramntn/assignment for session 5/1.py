
color_list=['blue','red','black','pink','brown','yellow']
print('My color list \n',color_list)

print("color_list at index 3:",color_list[3])

n=int(input('Enter a number from 0-5:'))
print('your color: ',color_list[n])
    
print(color_list)

for i in color_list:
    print('\n',i)
    
n=input('what is your favorite color')
for i in color_list:
    if n==i:
      print(str.forward('your color is at index{0} of my list',len(i))
    elif i!=len(color_list):
      print('sorry, icould not find your color')
