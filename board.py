def create_board():
    # ok so this makes the board the rows start from 0 and go to 7 
    board = [["  " for _ in range(8)] for _ in range(8)]
    board[0] = ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"]
    board[1] = ["bP" for _ in range(8)]
    board[6] = ["wP" for _ in range(8)] 
    board[7] = ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
    return board

def print_board(board):
    for row in board:
        print(" ".join(row))

def parse_square(text):
    column = ord(text[0].lower()) - ord('a')
    row = 8 - int(text[1])
    return row, column


