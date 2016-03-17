n=[int(x) for x in input('Enter size (column x row):').split()]

def pattern(x,y):
    for a in range(0,n[0]):
        for b in range(0,n[1]):
            print('*',end='  ')
        print('\n')       
        
pattern(n[0],n[1])
