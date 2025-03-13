# Tic-Tac-Toe Game in Python

# Initialize the board
board = [" " for _ in range(9)]  # 3x3 board stored as a list

# Function to display the board
def display_board():
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

# Function to check for a winner
def check_winner():
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]             # Diagonals
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] and board[condition[0]] != " ":
            return board[condition[0]]  # Return 'X' or 'O'
    return None


# Function to check if the board is full (draw)
def is_draw():
    return " " not in board

# Function to handle player moves
def player_move(player):
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
            if 0 <= move <= 8 and board[move] == " ":
                board[move] = player
                break
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Please enter a number between 1 and 9.")

# Main game loop
def play_game():
    current_player = "X"
    while True:
        display_board()
        player_move(current_player)
        
        winner = check_winner()
        if winner:
            display_board()
            print(f"Player {winner} wins!")
            break

        if is_draw():
            display_board()
            print("It's a draw!")
            break

        # Switch player
        current_player = "O" if current_player == "X" else "X"

# Start the game
play_game()
