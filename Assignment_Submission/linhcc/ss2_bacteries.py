b=int(input("How many B baterias are there?"))
t=int(input("How long will we wait?"))
y=b*(2**(t/2))
print(str.format("After {0} minutes we would have {1} B bacterias",t,y))
