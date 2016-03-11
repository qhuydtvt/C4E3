#1.1
color_list=["blue","white","black","gray","..."]
print("My color list \n",color_list)
#1.2
print("color_list at index 3:",color_list[3])
#1.3
n=int(input("Enter a munber from 0-5:"))
print(str.format("Your color:{0}",color_list[n]))
#1.4
print(color_list)
for color in color_list:
    print(color)
#1.5
while True:
    n=input("what is your favorite color?")
    i=0
    while True:
        if i >= len(color_list):
            print("Sorry, I could not find your color")
            break
        elif color_list[i] == n:
            print(str.format("Your color is at index {0} in my list",color_list.index(n)))
            break
        i += 1
