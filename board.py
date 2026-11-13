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

def is_valid_bishop_move(board,start,end): 
    start_row, start_column = start 
    end_row, end_column = end 

    #start row - end row have to equal the same amount as start column - end_column
    #wrap it around an abs so all numbers are postives
    # you have to move the bishop so start and end cannot be the same 
    if not abs(start_row - end_row) ==  abs(start_column - end_column) or (start_row == end_row and start_column == end_column): 
        return False
    
    if start_row > end_row: 
        row_step = -1 
    else:
        row_step = 1

    if start_column > end_column: 
        column_step = -1 
    else: 
        column_step = 1 

    distance = abs(start_row - end_row)

    for step in range(1, distance):
        check_row = start_row + step * row_step 
        check_column = start_column + step * column_step 
        if not is_empty(board,(check_row,check_column)):
            return False
  
    return True


def is_valid_queen_move(board,start,end):    
     #queen is able to move like a rook or a bishop so we can just check if it is valid for either of those pieces
    return is_valid_rook_move(board,start,end) or is_valid_bishop_move(board,start,end)

def is_valid_knight_move(board,start,end): 
    start_row, start_column = start
    end_row, end_column = end

    #knight movement logic
    return (abs(start_row - end_row) == 2 and abs(start_column - end_column) == 1) or (abs(start_row - end_row) == 1 and abs(start_column - end_column) == 2) 

def is_valid_king_move(board,start,end): 
    start_row, start_column = start
    end_row, end_column = end 

    row_distance = abs(start_row - end_row) 
    column_distance = abs(start_column - end_column) 
    #king can move 1 in any direction
    return ((row_distance <= 1) and (column_distance <= 1) and ((row_distance != 0) or (column_distance != 0)))

def find_king(board, color):
    for row in range(8):
        for column in range(8): 
           square = board[row][column] 
           if square == (color + "K"):
               return (row, column)  

def is_in_check(board, color):
    king_location = find_king(board, color) 

    if color == "w":
        enemy_color = "b"
    else: 
        enemy_color = "w" 
    
    return is_square_attacked(board, king_location, enemy_color)


def is_valid_pawn_move(board,start,end):
    start_row, start_column = start 
    end_row, end_column = end
    piece = board[start_row][start_column]  


    if piece[0] == 'w':
        direction = -1
        if start_row == 6:
            # 1 row up move or 2 row move on first move
            if (
                (end_row == start_row + direction 
                 and start_column == end_column 
                 and is_empty(board,end)) 
                 or 
                 (end_row == start_row + (2 * direction) 
                  and start_column == end_column 
                  and is_empty(board, (start_row + direction, start_column)) 
                  and is_empty(board,end))
            ):
                 return True 
            
        else:
            # 1 row up move 
            if (end_row == start_row + direction and start_column == end_column and is_empty(board,end)): 
                return True 
            
    elif piece[0] == 'b': 
        direction = 1
        if start_row == 1: 
            # 1 row up move or 2 row move on first move
            if(
                (end_row == start_row + direction 
                 and start_column == end_column 
                 and is_empty(board,end)) 
                 or 
                 (end_row == start_row + (2 * direction) 
                  and start_column == end_column 
                  and is_empty(board, (start_row + direction, start_column)) 
                  and is_empty(board,end))
            ):
                return True
             
        else: 
            # 1 row up move  
            if (end_row == start_row + direction and start_column == end_column and is_empty(board,end)):
                return True
            
    target = board[end_row][end_column]

    if (
        (end_row == start_row + direction)
        and (abs(start_column - end_column) == 1)
        and (target != "--") 
        and (target[0] != piece[0]) 
        ):
        return True
   
    return False

def is_square_attacked(board, square, attacker_color):
    for row in range(8):
        for column in range(8):
            piece = board[row][column]
            if piece[0] == attacker_color:
                if piece[1] == "P" and is_valid_pawn_move(board, (row, column), square):
                    return True
                if piece[1] == "R" and is_valid_rook_move(board, (row, column), square):
                    return True
                if piece[1] == "N" and is_valid_knight_move(board, (row, column), square):
                    return True
                if piece[1] == "B" and is_valid_bishop_move(board, (row, column), square):
                    return True
                if piece[1] == "Q" and is_valid_queen_move(board, (row, column), square):
                    return True
                if piece[1] == "K" and is_valid_king_move(board, (row,column), square): 
                    return True 
                
    return False

def is_legal_move(board, start, end, color): 
       if is_empty(board, start):
           return False   
                                
       row, column = start                                              
       piece = board[row][column]  

       if piece[0] != color:                                     
           return False
                                                        
       end_row,end_column = end                                         
       target = board[end_row][end_column]  

       if target[0] == color:                                    
           return False           
                                                 
       #check if piece is a rook if it is run rook logic                
       if piece[1] == "R" and not is_valid_rook_move(board,start,end ):
           return False
                                                        
       #check if piece is a bishop if it is run bishop logic            
       if piece[1] == "B" and not is_valid_bishop_move(board,start,end):
           return False
                                                            
       #check if piece is a queen if it is run queen logic              
       if piece[1] == "Q" and not is_valid_queen_move(board,start,end): 
           return False
                                                            
       #check if piece is a knight if it is run knight logic            
       if piece[1] == "N" and not is_valid_knight_move(board,start,end):
           return False
                                                            
       #check if piece is a king if it is run king logic                
       if piece[1] == "K" and not is_valid_king_move(board,start,end):  
           return False
                                                            
       #check if piece is a pawn if it is run pawn logic                
       if piece[1] == "P" and not is_valid_pawn_move(board,start,end):  
           return False                                
                                     
       test_board = [row[:] for row in board]                           
       move_piece(test_board, start, end) 

       if is_in_check(test_board, color):                        
           return False
       
       return True

def has_legal_move(board,color):

    for start_row in range(8):
        for start_column in range(8):
            for end_row in range(8):
                for end_column in range(8):
                    start = (start_row, start_column) 
                    end = (end_row, end_column) 
                    if is_legal_move(board, start, end, color):
                        return True 
    return False
