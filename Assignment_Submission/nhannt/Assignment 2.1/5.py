n = int(input("so thang tho sinh la? "))
i = 0
a = 1
b = 1
while i<n:
    print(str.format("Month {0}: {1} pair(s) of rabbits", i, a))
    i=i+1
    b=a-b
    a=b+a
