while True:
    b=0
    a=int(input('Please enter the number to check '))
    i=1
            
    while i<a:
        if a%i==0:
             b=b+i
               
        i=i+1
    if b==a:
        print(str.format('{0} is a perfect number',a))
    else:
        print(str.format('{0} is not a perfect number',a))

