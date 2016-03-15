#3. Write a Python program to extract the even numbers from a given list

def inChan(x):
    listChan=[]
    for phanTu in x:
        if phanTu%2==0:
            listChan.append(phanTu)
    return listChan

list_kiemTra=[2,3,4,5,6,12,19,20]
print ("In so chan cua list sau ",list_kiemTra)

for soChan in inChan(list_kiemTra):
    print(soChan)
