import os



def clear():
    if os.name == 'nt': os.system('cls')
    elif os.name == 'posix': os.system('clear')
    else: print("Unknown OS")


table = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]


def print_game():
    clear()
    print( f"""
  | 0  1  2
-------------
0 | {table[0][0]}  {table[0][1]}  {table[0][2]}
1 | {table[1][0]}  {table[1][1]}  {table[1][2]}
2 | {table[2][0]}  {table[2][1]}  {table[2][2]}
""")


#    for row in table:
#        for cell in row:
#            print(cell,'  ', end='')
#        print()
#


def is_gamedraw():
    for r in table:
        for c in r:
            if c == "-":
                return False
    return True


def is_gamesolved():
    # game is solved if all items in a row has same symbol
    # game is solved if all items in a column has same symbol
    # game is solved if all items in a diagonal has same symbol

    # row game over
    if table[0][0] == table[0][1] == table[0][2] == "0":
        return (True, "0")
    if table[1][0] == table[1][1] == table[1][2] == "0":
        return (True, "0")
    if table[2][0] == table[2][1] == table[2][2] == "0":
        return (True, "0")

    # column game over
    if table[0][0] == table[1][0] == table[2][0] == "0":
        return (True, "0")
    if table[0][1] == table[1][1] == table[2][1] == "0":
        return (True, "0")
    if table[0][2] == table[1][2] == table[2][2] == "0":
        return (True, "0")

    # diagonal game over
    if table[0][0] == table[1][1] == table[2][2] == "0":
        return (True, "0")
    if table[0][2] == table[1][1] == table[2][0] == "0":
        return (True, "0")

    # row game over
    if table[0][0] == table[0][1] == table[0][2] == "X":
        return (True, "X")
    if table[1][0] == table[1][1] == table[1][2] == "X":
        return (True, "X")
    if table[2][0] == table[2][1] == table[2][2] == "X":
        return (True, "X")

    # column game over
    if table[0][0] == table[1][0] == table[2][0] == "X":
        return (True, "X")
    if table[0][1] == table[1][1] == table[2][1] == "X":
        return (True, "X")
    if table[0][2] == table[1][2] == table[2][2] == "X":
        return (True, "X")

    # diagonal game over
    if table[0][0] == table[1][1] == table[2][2] == "X":
        return (True, "X")
    if table[0][2] == table[1][1] == table[2][0] == "X":
        return (True, "X")

    return (False, -1)


def update_table(r, c, player):
    global table
    table[r][c] = player


def take_input(player):
    print_game()
    r, c = tuple(map(int, input(f"user {player} Play: ").split()))
    update_table(r, c, player)
    if is_gamedraw():
        print_game()
        print("Game Drawn")
        exit()
    result, winner = is_gamesolved()
    if result:
        print_game()
        print(f"{winner} won!")
        exit()


while True:
    take_input("X")
    take_input("0")
