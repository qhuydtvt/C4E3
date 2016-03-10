

while True:
    so=int(input('Dien so vao? '))
    laydu=so%2
    if laydu==0:
        print('Day la so chan')
        if (so**1/2)%2==0:
            print('Day la so chinh phuong')
        break
       
    else:
        print('Day la so le')
    

        
