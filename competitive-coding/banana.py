"""
https://www.hackerrank.com/challenges/the-minion-game
"""

def minion_game(string):
    vowels = 'aeiouAEIOU'
    # your code goes here
    kevin = stuart = 0
    strlen = len(string)
    for i, char in enumerate(string):
        if char in vowels:
            kevin += strlen - i
        else:
            stuart += strlen - i
    if kevin > stuart:
        print('Kevin', kevin)
    elif stuart > kevin:
        print('Stuart', stuart)
    else:
        print('Draw')


# def minion_game(string):
#     vowels_list = set(['a','e','i','o','u','A','E','I','O','U'])
#     consonants = 0
#     vowels = 0

#     n = len(string)
#     for i, l in enumerate(string):
#         print(l)
#         if l in vowels_list:
#             vowels += n-i
#         else:
#             consonants += n-i

#     if vowels == consonants:
#         print("Draw")
#     elif vowels > consonants:
#         print("Kevin {}".format(vowels))
#     else:
#         print("Stuart {}".format(consonants))


if __name__ == '__main__':
    s = 'BANANAa'
    print(list(enumerate(s)))
    # minion_game(s)