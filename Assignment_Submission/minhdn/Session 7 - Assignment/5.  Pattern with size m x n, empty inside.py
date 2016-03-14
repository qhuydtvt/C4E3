def pattern():
    for i in range(1, n+1):
        if i == 1 or i == n:
            print('* ' * m)
        else:
            print('*', ' '*m, '*')

m = int(input('Column: m = '))
n = int(input('Row: n = '))
pattern()     
