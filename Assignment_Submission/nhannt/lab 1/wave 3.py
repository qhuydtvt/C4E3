import datetime
now = datetime.datetime.now()
hour = now.hour
print(hour)
n=input("water is available or not? ")
if ((hour<=10 and hour >=5) or (hour>=20 and hour<=22)) and n=="yes":
    print(str.format("Current time is {0}. Water is available",hour))
elif ((hour<=10 and hour >=5) or (hour>=20 and hour<=22)) and n=="no":
    print(str.format("Current time is {0}. Water is available but not this time",hour))    
else:
    print(str.format("Current time is {0}. Water is available but not this time",hour))
