"""
input: 2 integers - start, end
output: list of differences between adjacent perfect square numbers between start and end (both included)
Eg:
input: 2 30
Output: [5 7 9]
"""

import sys

def find_squares(start, end):
    squares = []
    i = 0
    while True:
        i += 1
        if i*i < start:
            continue
        elif i*i in range(start, end+1):
            squares.append(i*i)
        else:
            break
    return squares

if __name__ == '__main__':
    start = int(sys.argv[1])
    end = int(sys.argv[2])
    squares = find_squares(start, end)
    print("Perfect squares: ", squares)
    adj_diff_list = []
    for i in range(len(squares)):
        j = i + 1
        if j < len(squares):
            adj_diff_list.append(squares[j] - squares[i])
    #print("Differece between adjacent perfect squares: ", adj_diff_list)

    diff_set = set() 
    for i in squares: #range(len(squares)):
        for j in squares: #range(i+1, len(squares)):
            #diff_set.add(squares[j] - squares[i])
            diff_set.add(j - i)

    print("Differece between all perfect squares: ", diff_set)
            
