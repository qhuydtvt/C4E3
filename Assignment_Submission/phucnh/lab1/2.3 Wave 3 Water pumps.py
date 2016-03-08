import datetime
now= datetime.datetime.now()
hour=now.hour
water=input('water is availabel or not? ')
if ((hour>=5)and(hour<=10)or (hour>=20)and(hour<=22)) and water=="co":
##    print('bay gio la',hour,' va co the bom nuoc')
    print(str.format('bay gio la {0} va co the bom nuoc',hour))
else:
    print ('khong bom')
        
