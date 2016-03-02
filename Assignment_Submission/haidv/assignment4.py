while True:
    a=int(input('How many Bacteria are there?'))
    b=float(input('How much time will we wait?'))
    c=b//2
    d=a*2**c
    print(str.format('After {0} minutes we would have {1}',b,d))

