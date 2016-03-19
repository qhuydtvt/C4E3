def munu ():
    n = input("Enter a series of number (using space as buffers inbetween numbers): ")
    m = n.split(" ")
    l = [int(i) for i in m]
    p = 1
    for a in l:
        p *= a
    return print("result: ", p)
munu()

