# Write a Python function to multiply all the numbers in a list

list_mult=[1,4,5,-6,7,8]

def mult_list(x):
    kq_nhan=1;
    for nhan in x:
        kq_nhan=kq_nhan*nhan
    return kq_nhan

print(list_mult)
print("multiply all the numbers in a list is ",mult_list(list_mult))
