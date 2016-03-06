n = int(input("How many B bacterias are there? "))
t = int(input("How much time will we wait? "))
x = (n**(t/2 + 1))
print (str.format("After {0} minutes we would have {1} B bacterias", t, x)) 


