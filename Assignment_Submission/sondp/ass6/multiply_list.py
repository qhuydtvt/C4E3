def multiply_list(list):
    length = len(list)
    list=[int(i) for i in list]
    n=0
    s=1
    while n<length :
        s = s * list[n]
        n=n+1
        continue
    print("Tich cac so trong danh sach la: ",s)
    return s

        
    
