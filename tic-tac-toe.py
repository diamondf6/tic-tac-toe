def tboard(board):
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print(f"---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print(f"---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")

def play(board, name):
    while True:
        try:
            move = int(input("Enter the value from 0 to 8: "))

            if 0<= move < 9 and board[move] == " ":
                board[move] = name
                tboard(board)
                break
            else:
                print("Invalid Move")
        except ValueError:
            print("Enter the valid value")

def winner(board, name):
    win = [ [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
    
    for condition in win:
        if all(board[i] == name for i in condition):
            return True
    return False

def is_tie(board):
    return " " not in board


board = [" " for _ in range(9)]
tboard(board)

players = ["X", "O"]

turn = 0

while True:
    play(board, players[turn])

    if winner(board, players[turn]):
        print(f"Player {players[turn]} wins!!!")
        break
    if is_tie(board):
        print("The is at the equal and tied!!")
        break
    turn = 1- turn 



