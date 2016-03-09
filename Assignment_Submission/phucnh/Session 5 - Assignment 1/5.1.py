#1
color_list=["Blue","Red", "Black", "Pink", "Brown", "Yellow"]
print("My color list \n",color_list)
#2
print("color_list at index 3",color_list[3])

#3
index = int(input("Enter a number from 0-5: "))
print("Your color: ", color_list[3])

#4
print (color_list)
for color in color_list:
    print (color)

#5
like = input("What is your favorite color: ")
i=0
for color in color_list:
    
    if like!=color:
        i=i+1
    else:
        print ("Your color is at index ",i,"in my list")
        break
    if i==len(color_list)-1:
        print ("Sorry, I could not find your color")
