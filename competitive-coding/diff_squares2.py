import sys


def find_squares(start, end):
    squares = []
    i = -1
    while True:
        i += 1
        if i*i < start:
            continue
        elif i*i in range(start, end+1):
            squares.append(i*i)
        else:
            break
    return squares

if "__main__" == __name__:
    start = int(sys.argv[1])
    end = int(sys.argv[2])


    squares = find_squares(start, end)
    # 0 1 4 9
    # 1 10 -> 1 4 9 3 8 5
    diff_list=[]

    for i in range(len(squares)):
        for j in range(i+1, len(squares)):
            diff_list.append(squares[j]-squares[i])

    print(diff_list)
