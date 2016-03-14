p=input('Please, enter the list of numbers: ')
listnumber=[int(x)for x in p.split()]
listeven=[x for x in listnumber if x%2==0]
print(listeven)
