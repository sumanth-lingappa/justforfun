import sys

string = sys.argv[1] # user input can be taken using input()
print()

# positive_indexing
print(' ',end='')
for positive_index in range(len(string)):
    print(f'{positive_index:^3} ', end='')
print()
    
# negative_indexing
print(' ',end='')
for negative_index in range(-len(string),0):
    print(f'{negative_index:^3} ', end='')
print()

# top border
print('+' + '---+'*len(string))

# middle row with letters
print('|',end='')
for letter in string:
    print(f' {letter} |', end='')
print()

# bottom border 
print('+' + '---+'*len(string))

print()
