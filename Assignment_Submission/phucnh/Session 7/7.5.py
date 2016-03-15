#5


def pattern(x,y):
    for i in range(x):
        
        day=""
        for j in range(y):
            if (i==0)or(i==x-1)or(j==0)or(j==y-1):
                day=day+"*  "
            else:
                day=day+"   "
        print(day)

hang= int(input("so hang: "))
cot= int(input("so cot: "))

pattern(hang,cot)



