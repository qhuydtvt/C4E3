i = 0
m0 = 1
n0 = 0
print ("Month 0: 1 pair of rabbits")
while i < 10 :
    i = i + 1
    m1 = m0 + n0
    n1 = m0
    tong =  m1 + n1
    print(str.format("Month {0}: {1} pairs of rabbits", i, tong))
    m0 = m1
    n0 = n1


#m0, m1 la mature thang truoc, mature thang sau
#n0, n1 la newborn thang truoc, newborn thang sau
    
    
