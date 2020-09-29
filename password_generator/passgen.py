import random

import sys

minlen = int(sys.argv[1])
maxlen = int(sys.argv[2])

islowercase = True
isuppercase = True
isspecialchar = True
isnumbers = True


lowercase_chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
uppercase_chars = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
special_chars = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',  '*', '(', ')']
number_chars = ['1', '2', '3', '4', '6', '7', '8', '9', '0']


possible_password_chars = []
if islowercase: possible_password_chars += lowercase_chars
if isuppercase: possible_password_chars += uppercase_chars
if isspecialchar: possible_password_chars += special_chars
if isnumbers: possible_password_chars += number_chars


password = random.choices(possible_password_chars, k=random.randint(minlen, maxlen))

print(''.join(password))
