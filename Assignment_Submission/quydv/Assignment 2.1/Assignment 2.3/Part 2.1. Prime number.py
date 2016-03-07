
while True:
    num = int(input("Enter a prime number: "))
    if num > 0 and num % 2 == 1 and num % 3 != 0 and num % 5 != 0 and num & 7 != 0:
        print(str.format("{0} is a prime number.", num))
        break
    else:
        print(str.format("{0} is NOT a prime number.",num))
        continue
