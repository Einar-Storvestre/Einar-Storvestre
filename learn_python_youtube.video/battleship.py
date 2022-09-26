import random

board = []

for x in range(0, 5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print(" ".join(row))


print("Let's play Battleship!")
print_board(board)


def random_row(board):
    return random.randint(0, len(board) - 1)


def random_col(board):
    return random.randint(0, len(board[0]) - 1)


ship_row = random_row(board)
ship_col = random_col(board)
print(ship_row)
print(ship_col)

for turn in range(4):
    guess_row = input("Guess Row:")
    guess_col = input("Guess Col:")

    if guess_row == ship_row and guess_col == ship_col:
        print ("Congratulations! You sunk my battleship!")
        break
    else:
        if turn == 3:
            board[int(guess_row)][int(guess_col)] = "X"
            print_board(board)
            print("Game Over")

            print("My ship was here: [" + str(ship_row) + "][" + str(ship_col) + "]")

        else:
            if (int(guess_row) < 0 or int(guess_row) > 4) or (int(guess_col) < 0 or int(guess_col) > 4):
                print("Oops, that's not even in the ocean.")

            elif (board[int(guess_row)][int(guess_col)] == "X"):
                print("You guessed that one already.")
                
            else:
                print("You missed my battleship!")
                board[int(guess_row)][int(guess_col)] = "X"
            print(turn + 1)
            print_board(board)