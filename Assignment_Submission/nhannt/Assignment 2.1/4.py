b = int(input("How many B bacterias are there? "))
a = int(input("How much time will we wait? "))
c=b*(a//2)*2
print(str.format("After {0} minutes we would have {1} bacterias", a, c))
