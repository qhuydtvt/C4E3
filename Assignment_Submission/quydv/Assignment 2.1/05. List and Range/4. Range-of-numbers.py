#4.1.
#copy tu bai 3
range1 = (0, 1, 2, 3, 4, 5, 6)
range2 = (1, 4, 7, 10)
range3 = (5, 4, 3, 2, 1)
range4 = (6, 4, 2, 0, -2)

range_name = (range1, range2, range3, range4)
range_list = []
for rangeNum in range_name:
    range_list.extend(rangeNum)
print(range_list)
print(sum(range_list))

#4.2.
S2 = []
i = 1
while i < 10:
    S2.append(1/i)
    i += 1
print("S2 =",sum(S2))

#4.3.
S3 = []
num_of_fractions = 1
n = int(input("Enter the number of fractions: "))
while num_of_fractions < n:
    S3.append(1/num_of_fractions)
    num_of_fractions += 1
print("S3 =", sum(S3))

#4.4.
S4 = []
num_of_fractions = 1
denominator = 1
n = int(input("Enter the number of fractions: "))
while num_of_fractions < n:
    denominator *= num_of_fractions
    S4.append(1/denominator)
    num_of_fractions += 1
    
print(S4)
print("S4 =", sum(S4))
