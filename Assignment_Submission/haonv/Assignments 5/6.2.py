#lay so chan trong danh sach
n = input('import a list number')
list_num = [int(x) for x in n.split()]
for x in list_num:
    if x % 2 == 0:
        print ('the even number : ' , x)
