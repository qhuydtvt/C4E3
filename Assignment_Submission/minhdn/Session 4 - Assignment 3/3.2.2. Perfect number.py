n = int(input('Enter a number: '))
if n == 0:
    print('0 is NOT perfect number!')

else:    
    tong = 0
    i = 1
    while i <= n:
        if n%i == 0:
            tong = tong + i
        i = i + 1

    if n == (tong/2):
        print(str.format('{0} is perfect number!', n))
    else:
        print(str.format('{0} is NOT perfect number!', n))
    
