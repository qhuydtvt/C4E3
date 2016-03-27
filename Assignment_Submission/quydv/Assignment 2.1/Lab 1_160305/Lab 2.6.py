while True:
    num = int(input("enter an even number"))
    if num % 2 == 0:
        square = num ** (1/2)
        if square == (square // 1):
            print("Day la so chinh phuong.")
            break
