s = input()
logodict = {}
for char in s:
    logodict[char] = logodict.get(char, 0) + 1
logolist = [(word, count) for word, count in logodict.items()]
logolist = sorted(logolist, key=lambda x: (-x[1], x[0]))
print(logolist)
top3 = logolist[:3]

for word, count in top3:
    print(word, count)


