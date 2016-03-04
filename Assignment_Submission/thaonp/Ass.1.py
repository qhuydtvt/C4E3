#1.
#Check variable's type: Type(variable) 
#3 cases that we will get SyntaxError from the compiler telling:
 #Begin with number. Eg: 1312Pt
 #Contains an illegal character. Eg: @hjhjdongok@
 #Use Python's keywords: Eg: andthenelse
#2.
r=int(input("Radius = "))
S=3.14*r*r
print("Area =",S)

#3.
C=int(input("Enter the temperature in Celcius? "))
F= C*1.8+32
print(C,"(C) = ", F,"(F)")

#4.
nobb=int(input("How many B bacterias are there ? "))
time=int(input("How much time will we wait ? "))
noba=nob*2**(time//2)
print ("After", time,"minutes we would have",noba,"bacterias") 

#5.
tho_lon=1
tho_be=1
i=0
while i<=4:
    print(str.format("Month {0}: {1} pair(s) of rabbits", i, tho_be))
    tho_lon=tho_be
    tong=tho_lon+tho_be
    i=i+1

	


