#1.1.
color_list = ["Blue", "Red", "Black", "Pink", "Brown", "Yellow", "Green", "Grey"]
print(color_list)

#1.2.
print(str.format("color_list at index 3: {0}", color_list[3]))

#1.3.
i = int(input("Enter a number from 0-5: "))
print(str.format("Your color: {0}",color_list[i]))

#1.4.
print(color_list)

for color in color_list:
    print(color)
    
#1.5.
check = True
while check:
    answer = input("What is your favorite color?")
    i = 0
    while True:
        if i >= len(color_list):
            print("Sorry, I could not find your color")
            break
        elif color_list[i] == answer:
            print(str.format("Your color is at index {0} in my list.", color_list.index(answer)))
            check = False
            break
        i += 1
