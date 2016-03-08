import datetime

n = str(input("Water is available or not? "))
if n == "no":
    print("Water is not available")
elif n == "yes":
    now = datetime.datetime.now()
    hour = now.hour
    
    if hour >= 5 and hour <= 10:
        print("Bay gio la", hour, "gio.", "Pump is turned on")
    elif hour >= 20 and hour <= 22:
        print("Bay gio la", hour, "gio.", "Pump is turned on")
    else:
        print("Bay gio la", hour, "gio.", "Pump is turned off")





