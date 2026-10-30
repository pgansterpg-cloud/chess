from board import *

board = create_board() 
print_board(board)     

while True:
    player_input = input("Move: ")
    if player_input == 'quit':
        break
    
    start_move, end_move = player_input.split()
    
    start = parse_square(start_move) 
    end = parse_square(end_move)
        
    if is_empty(board, start):
        print("There's no piece on that square.")
        continue
    
    move_piece(board, start, end) 
    print_board(board) 