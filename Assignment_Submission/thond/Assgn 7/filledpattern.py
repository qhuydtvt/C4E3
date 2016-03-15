def fpat():
    n = int(input("Enter length: "))
    m = int(input("Enter width: "))
    for i in range(m):
        print("*", end = ' ')
        for j in range(n-1):
            print("*", end = ' ')
        print("\n")
fpat()
