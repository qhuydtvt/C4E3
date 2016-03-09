while True:
    i = int(input("enter a number?"))
    if i>0 and i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0:
        print(str.format("{0} is a prime number.",i))
        break
    else:
        print(str.format("{0} is NOT a prime number.",i))
        continue

