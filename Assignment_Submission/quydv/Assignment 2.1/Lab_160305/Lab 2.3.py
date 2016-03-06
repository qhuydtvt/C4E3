import datetime

current = datetime.datetime.now()
hour = current.hour
print(hour)
avail = input("water is available or not (yes or no)?")
if avail == "yes":
    if (hour >= 5 and hour < 10) or (hour >= 20 and hour < 22):
        print("Yes, pump the water.")
    elif avail == "no":
        print("Water is not available")
else:
    print(str.format("Current time is {0}. Water is available but no need to pump",current))
