color = ['Blue', 'Red', 'Black', 'Pink', 'Brown', 'Yellow']
print("My color list", "\n", color)
print("color_list at index 3:", color[3])
i = int(input("Enter a number from 0-5: "))
print("Your color:", color[i])

print (color)
for n in color:
    print(n)

n = input("What is your favorite color?")
if n in color:
    print("Your color is at index",color.index ('Red'), "in my list.")
else:
    print("Sorry, I could not find your color.")

