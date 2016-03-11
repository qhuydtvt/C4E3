import datetime
n=input("Water is available or not? ")
now=datetime.datetime.now()
hour=now.hour
if n== "available":
 if hour >=5 and hour <=10:
   print("Pump is turn on ")
 elif hour >=20 and hour <=22:
   print("Pump is turn on")
 else:
    print("Pump is turn off")
if n=="not":
 print("water is not")
