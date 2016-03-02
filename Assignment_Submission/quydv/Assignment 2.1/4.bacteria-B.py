initial = int(input('How many B bacteria are there?'))
time = int(input('How much time will we wait (in minutes)?'))
#Sao cho nay neu thu dien time = 4.8 lai kkhong dc? Binh thuong thi int(4.2) van
#ra la 4?
after = int(initial * (2 ** (time/2)))
print('After', time, 'minutes we would have', after, 'bacteria.')
