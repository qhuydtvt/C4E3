
def uoc(x):
    list_uoc=[]
    for i in range(1,x+1):
        if x%i==0:
            list_uoc.append(i)
    return list_uoc

lay_uoc= int(input("so lay uoc: "))
list_uoc= uoc(lay_uoc)

print("uoc cua ",lay_uoc, " la: ")
for x in list_uoc:
    print (x)
