from board import *

board = create_board() 
print_board(board)     

while True:
    player_input = input("Move: ")
    if player_input == 'quit':
        break
    
    start_move, end_move = player_input.split()
    move_piece(board, parse_square(start_move), parse_square(end_move))
    print_board(board) 