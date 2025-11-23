8def sum(a, b, c):
    return a + b + c

def printBoard(xState, zState):
    zero = 'x' if xState[0] else ('0' if zState[0] else 0)
    one = 'x' if xState[1] else ('0' if zState[1] else 1)
    two = 'x' if xState[2] else ('0' if zState[2] else 2)
    three = 'x' if xState[3] else ('0' if zState[3] else 3)
    four = 'x' if xState[4] else ('0' if zState[4] else 4)
    five = 'x' if xState[5] else ('0' if zState[5] else 5)
    six = 'x' if xState[6] else ('0' if zState[6] else 6)
    seven = 'x' if xState[7] else ('0' if zState[7] else 7)
    eight = 'x' if xState[8] else ('0' if zState[8] else 8)

    print(f"{zero} | {one} | {two}")
    print("--|---|--")
    print(f"{three} | {four} | {five}")
    print("--|---|--")
    print(f"{six} | {seven} | {eight}")

def cWin(xState, zState):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], 
            [0, 3, 6], [1, 4, 7], [2, 5, 8], 
            [0, 4, 8], [2, 4, 6]]
    
    for win in wins:
        if(sum(xState[win[0]], xState[win[1]], xState[win[2]]) == 3):
            print("X Won the match")
            return 1
        if(sum(zState[win[0]], zState[win[1]], zState[win[2]]) == 3):
            print("O Won the match")
            return 0
    return -1

if __name__ == "__main__":
    xState = [0] * 9
    zState = [0] * 9
    turn = 1  # 1 for X, 0 for O
    print("Welcome to Tic Tac Toe\n")

    while True:
        printBoard(xState, zState)
        if turn == 1:
            print("X's Turn")
            value = int(input("Enter position (0-8): "))
            if xState[value] == 0 and zState[value] == 0:
                xState[value] = 1
            else:
                print("Position already taken. Try again.")
                continue
        else:
            print("O's Turn")
            value = int(input("Enter position (0-8): "))
            if xState[value] == 0 and zState[value] == 0:
                zState[value] = 1
            else:
                print("Position already taken. Try again.")
                continue

        winner = cWin(xState, zState)
        if winner != -1:
            printBoard(xState, zState)
            print("Match Over!")
            break

        turn = 1 - turn
