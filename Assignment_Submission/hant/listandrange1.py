color_list=["Blue","Red","Black","Pink","Brown","Yellow"]
print("My color list","\n",color_list)
print("color_list at index 3:",color_list[3])
i=int(input("Enter a number from 0-5:"))
print("Your color:",color_list[i])
print(color_list)
for x in color_list:
    print(x)
n=input('What is your favorite color?')
for p in color_list:
    if n==p:
        m=color_list.index(n)
        print('Your color is at index',m, 'in my list')
        break
    elif n!=p:
        print("Sorry, I could not find your color")
        break
