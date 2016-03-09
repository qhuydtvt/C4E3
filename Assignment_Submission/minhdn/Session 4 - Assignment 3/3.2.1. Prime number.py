n = int(input('Enter a number: '))
if n <= 1:
    print(str.format('{0} is NOT a prime number', n))
elif n == 2:
    print(str.format('{0} is a prime number', n))
else:        
    i = 2
    while True:
        if i < n:
            if n%i == 0:
                print(str.format('{0} is NOT a prime number', n))
                break
            else:
                i = i + 1 
        else:
            print(str.format('{0} is a prime number', n))
            break
            
                  
                    
                
       
           
    

    
        
    
        
