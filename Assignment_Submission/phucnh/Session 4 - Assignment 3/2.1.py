


while True:
    i=2
    number=int( input ('Enter a number: '))
    if number==1 :
        print (number,'is a prime nuber')
    if number==2:
        print (number,'is NOT a prime nuber')
    while i<=number-1:
        if number%i==0:
            print (number,'is NOT a prime nuber')
            break
        else:
            i=i+1
            
    if i>number-1 and i>2:
        print (number,'is a prime nuber')

        

