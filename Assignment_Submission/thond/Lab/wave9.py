import datetime
import time
while True:
    a = input("Is water available? yes or no?")
    now = datetime.datetime.now ()
    hour = now.hour
    if a == "yes":
        if 5 <= hour <=10 or 20 <= hour <=22:
            print (str.format("Current time is {0}. Water is available at this time.",now))
        else:
            print (str.format("Current time is {0}. Water is available but not at this time.",now))
    if a == "no":
        print (str.format("Current time is {0}. Water is not available.",now))

    

