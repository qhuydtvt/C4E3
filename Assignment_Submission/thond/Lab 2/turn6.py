l = ["abc", "xyz", "bcd"]
print("My playlist is:") 
for i in l:
    print(str.format("{0}: {1}",l.index(i),i))
n = input("Enter song name here: ")
n = n.lower()
if n in l:
    print("Play")
else:
    print("Ehhhh!!!")
