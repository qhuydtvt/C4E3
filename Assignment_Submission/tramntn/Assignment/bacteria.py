a=int(input("how many B bacterias are there?"))
b=int(input("how much time will we wait?"))
t=b/2
e=a*(2**t)
print(str.format("After {0} minutes we would have {1} bacterias",b,e))
