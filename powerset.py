

name = "BANANA"

for i in range(len(name)):
    for j in range(i):
        sub = name[j:i]
        print(sub, name.count(sub))
