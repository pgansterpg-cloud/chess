from board import *

board = create_board() 
move_piece(board, parse_square("e2"), parse_square("e4"))
print_board(board) 