import datetime
import time
while True:
    a = input("Is water available? yes or no?")
    now = datetime.datetime.now ()
    hour = now.hour
    if n == "yes":
        if 5 <= hour <=10 or 20 <= hour <=22:
            print (str.format("
