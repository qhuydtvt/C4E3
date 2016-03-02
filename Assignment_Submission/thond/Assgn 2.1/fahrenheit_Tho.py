while True:
    c = int(input("Enter the temperature in Celsius?"))
    f = (c*(9/5))+ 32
    print(str.format("{0} (C) = {1} (F)",c,f))
