mature = 1
immature = 0
time = 0
print(str.format('After {0} month(s): There are {1} pairs of mature rabbit.', time, mature))
while time < 4:
    time = time + 1
    new_mature = immature
    new_immature = mature 
    immature = new_immature 
    mature = mature + new_mature
    print(str.format('After {0} month(s): There are {1} pairs of mature rabbit.', time, mature))
