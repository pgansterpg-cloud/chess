def create_board():
    # ok so this makes the board the rows start from 0 and go to 7 
    board = [["--" for _ in range(8)] for _ in range(8)]
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

def move_piece(board, start, end): 
    start_row, start_column = start
    end_row, end_column = end
    board[end_row][end_column] = board[start_row][start_column] 
    board[start_row][start_column] = "--"

def is_empty(board,square):
    row, column = square
    return board[row][column] == "--"

def is_on_board(square):
    row, column = square
    return 0 <= row <= 7 and 0 <= column <= 7

def is_valid_rook_move(board,start,end): 
    start_row, start_column = start 
    end_row, end_column = end
    
    #if you are going down a column row is the only thing that should change and if you are going down a row only the end column should change
    if not ((start_row != end_row and start_column == end_column) or (start_row == end_row and start_column != end_column)):
        return False 

    if start_column == end_column:
        for check_row in range(min(start_row,end_row) +1, max(start_row,end_row)):
            if not is_empty(board,(check_row,start_column)):
                return False 
    else: 
        for check_column in range(min(start_column,end_column) + 1, max(start_column,end_column)):
            if not is_empty(board,(start_row,check_column)):
                return False
    return True


    


