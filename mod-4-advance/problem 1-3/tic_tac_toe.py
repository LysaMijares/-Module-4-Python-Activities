# string of the board 0-15 for 4x4
board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


# board print using list
def tic_tac_toe(board):
    print(f"{board[0]} | {board[1]} | {board[2]} | {board[3]} |")
    print("---------------")
    print(f"{board[4]} | {board[5]} | {board[6]} | {board[7]} |")
    print("---------------")
    print(f"{board[8]} | {board[9]} | {board[10]} | {board[11]} |")
    print("---------------")
    print(f"{board[12]} | {board[13]} | {board[14]} | {board[15]} |")


# Checks the arguments whether the game is finished or not
def is_game_over(board):
    # Check rows
    for i in range(0, 16, 4):
        if board[i] == board[i + 1] == board[i + 2] == board[i + 3] and board[i] != ' ':
            return True

    # Check columns
    for i in range(4):
        if board[i] == board[i + 4] == board[i + 8] == board[i + 12] and board[i] != ' ':
            return True

    # Check diagonals
    if board[0] == board[4] == board[8] and board[i + 12] != ' ':
        return True
    elif board[2] == board[4] == board[8] == board[12] and board[15] != ' ':
        return True

    # Check for tie
    if ' ' not in board:
        return True

    # Game is not over yet; returns to the game
    return False


# Define the main game loop
player = 'X'
while not is_game_over(board):
    # Prints the game board
    tic_tac_toe(board)

    # Ask the player for their move
    move = int(input(f"Player {player}, enter your move (1-16): ")) - 1

    # Check if the move is valid
    if board[move] != ' ':
        print("Invalid move, try again")
        continue

    # Update the game board
    board[move] = player

    # Switch to the other player
    player = 'O' if player == 'X' else 'X'

# Print the final game board
print(tic_tac_toe(board))

# Check who won or if it's a tie
if ' ' not in board:
    print("NO WINNER")

else:
    print(f"Player {player} won!")
