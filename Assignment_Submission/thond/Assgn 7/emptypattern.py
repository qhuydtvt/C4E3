def mpat():
    n = int(input("Enter length: "))
    m = int(input("Enter width: "))
    for i in range(m):
        print("*", end=" ")
        for j in range(n-2):
            if i == 0 or i == m - 1:
                print("*", end=" ")
            else:
                print(" ",end=" ")
        print("*", end = "")
        print("\n")
mpat()
