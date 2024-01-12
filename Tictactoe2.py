# Variables
board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']
currentPlayer = "X"
winner = 0  # 0 for tie, 1 for Player X, 2 for Player O
gameRunning = True

# Printing the board
def make_board(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("-" * 9)
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("-" * 9)
    print(board[6] + " | " + board[7] + " | " + board[8])

# Player input
def p_input(board):
    while True:
        player_symbol = "X" if currentPlayer == "X" else "O"
        inp = int(input(f"Pick a number from 1-9 Player ({player_symbol}): "))
        if 1 <= inp <= 9 and board[inp-1] == "-":
            board[inp-1] = currentPlayer
            break
        else:
            print(f"Pick another player ({player_symbol})! ")
            make_board(board)

# Checking for win or tie
def c_win():
    global winner
    if c_diagonal() or c_horizontal() or c_row():
        winner = 1 if currentPlayer == "X" else 2
        make_board(board)

# Checking horizontal win
def c_horizontal():
    return (board[0] == board[1] == board[2] != "-"
            or board[3] == board[4] == board[5] != "-"
            or board[6] == board[7] == board[8] != "-")

# Checking row win
def c_row():
    return (board[0] == board[3] == board[6] != "-"
            or board[1] == board[4] == board[7] != "-"
            or board[2] == board[5] == board[8] != "-")

# Checking diagonal win
def c_diagonal():
    return (board[0] == board[4] == board[8] != "-"
            or board[2] == board[4] == board[6] != "-")

# Checking for a tie
def c_tie():
    global gameRunning
    if "-" not in board:
        make_board(board)
        print("It's a tie!")
        gameRunning = False

# Switching the player
def s_player():
    global currentPlayer
    currentPlayer = "O" if currentPlayer == "X" else "X"

# Main game loop
def main():
    global winner
    while gameRunning:
        make_board(board)
        if winner != 0:
            print(f"The winner is Player {winner}")
            break
        p_input(board)
        c_win()
        c_tie()
        s_player()

# Run the game
main()