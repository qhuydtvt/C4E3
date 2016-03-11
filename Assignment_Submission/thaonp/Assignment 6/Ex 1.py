n=input("Enter a list of numbers: ")
numlst = [int(x) for x in n.split()]

result = 1
for num in numlst:
    result *= num

print("Result:", result)

