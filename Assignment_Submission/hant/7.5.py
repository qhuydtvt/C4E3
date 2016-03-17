n=int(input('column:'))
m=int(input('row:'))
def pattern(x,y):
    for i in range(0,n):
        print('*',end='  ')
    print('\n')
    for i in range(0,m-2):
        a='  '*(n-1)
        print('*',a,'*',end='  ')
        print('\n')
    for i in range(0,n):
        print('*',end='  ')                   

pattern(n,m)
        
    
