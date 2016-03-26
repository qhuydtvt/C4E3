def stars_around(m, n):
    i = 0
    star = "*"
    tab  = "\t"
    while i in range(m+1):
        if i == 0 or i == m:
            print((star + tab) * n)
        else:
            print(star + (n-1) * tab + star)
        i += 1

stars_around(4,5)
