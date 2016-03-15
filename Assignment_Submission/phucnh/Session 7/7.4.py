#4.  Write a Python function to print out the following pattern with size m x n


def pattern(x,y):
    for i in range(x):
        day=""
        for j in range(y):
            day=day+"*  "
        print(day)

hang= int(input("so hang: "))
cot= int(input("so cot: "))

pattern(hang,cot)



