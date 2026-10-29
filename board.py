def create_board():
    board = [["  " for _ in range(8)] for _ in range(8)]
    board[0] = ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"]
    board[1] = ["bP" for _ in range(8)]
    board[6] = ["wP" for _ in range(8)] 
    board[7] = ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
    return board

def print_board(board):
    for row in board:
        print(" ".join(row)) 

