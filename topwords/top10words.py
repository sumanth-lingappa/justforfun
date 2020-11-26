filename = 't8.shakespeare.txt'
worddict = {}
with open(filename) as fo:
    for line in fo.readlines():
        for word in line.split():
            if len(word) > 2 and word not in ['the', 'The', 'an', 'An', 'and', 'And']:
                worddict[word] = worddict.get(word, 0) + 1

wordlist = [(word, count) for word, count in worddict.items()]
wordlist.sort(reverse = True, key=lambda x: x[1])

top10 = wordlist[:3]

for word, count in top10:
    print(word,'\t\t',count)

