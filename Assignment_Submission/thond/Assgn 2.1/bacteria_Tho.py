while True:
    b = int(input("How many B baterias are there?"))
    t = int(input("How long will we wait?"))
    et = t//2
    n = b*(2**et)
    print(str.format("After {0} minutes we would have {1} B bacterias",t,n))
    
