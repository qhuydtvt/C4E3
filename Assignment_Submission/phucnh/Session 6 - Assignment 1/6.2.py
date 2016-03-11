#2. Write a Python function to calculate the factorial of a number (non-negative integer).
#The function accept the number as an argument.

def giaiThua(x):
    ketQua=1
    for i in range(1,x+1):
        ketQua=ketQua*i
    return ketQua

n=int(input("Tinh giai thua cua n, n= "))
print("Giai thua cua ",n,"la ",giaiThua(n))
