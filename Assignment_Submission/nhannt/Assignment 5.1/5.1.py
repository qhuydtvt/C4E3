#1.1
color = ['red','blue','black','white','yellow']
print('My color list \n',color)
#1.2
print('color_list at index 3:',color[3])
#1.3
i=int(input('enter a number from 1 to 5:'))
print('your color:',color[i])
#1.4
print(color)
for u in color:
    print(u)
#1.5
m = input('what is your favorite color?')
n=0
while n<len(color):
    if m==color[n]:
        print(str.format("your color is at index {0} in my list",n))
        break
    else:
        n=n+1
if n==len(color) and m!=color[-1]:
    print("Sorry, i could not find your color")
        
