done = False
while not done:
    num = int(input("Enter a perfect number: "))
    i = 0
    total = 0
    while True:
        if total <= num:          
            i = i + 1
            if num % i == 0 and i <= num:
                total = total + i
                if total == num:
                    print(str.format("{0} is a perfect number.", num))
                    done = True
                    break
        else:
            print(str.format("{0} is NOT a perfect number.", num))
            break
