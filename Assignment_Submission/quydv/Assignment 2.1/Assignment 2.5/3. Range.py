range1 = (0, 1, 2, 3, 4, 5, 6)
range2 = (1, 4, 7, 10)
range3 = (5, 4, 3, 2, 1)
range4 = (6, 4, 2, 0, -2)

range_name = (range1, range2, range3, range4)
range_list = []
for rangeNum in range_name:
    range_list.extend(rangeNum)
print(range_list)
