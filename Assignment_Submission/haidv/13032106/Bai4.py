def prinout(m,n):
    for i in range(0,m):
        print('*  ',end='')
    print('\n')
    for i in range(0,n-2):
        print('*  ',end='')
        for i in range(0,m-2):
            print('   ',end='')
        print('*\n')
    for i in range(0,m):
        print('*  ',end='')
        
prinout(9,10)
