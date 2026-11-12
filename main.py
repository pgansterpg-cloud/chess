from board import *

board = create_board() 
print_board(board)

current_turn = "w" 

while True:
    player_input = input("Move: ")
    if player_input == 'quit':
        break

    try:
        start_move, end_move = player_input.split()
    except ValueError:
        print("Type a move like e2 e4.") 
        continue

    try:
        start = parse_square(start_move) 
        end = parse_square(end_move)
    except ValueError: 
        print("That isn't a valid square")
        continue

    if not is_on_board(start) or not is_on_board(end):
        print("That move is not on the board")
        continue
        
    if not is_legal_move(board, start, end, current_turn):
        print("That is not a legal move.") 
        continue

    move_piece(board, start, end) 
    print_board(board)

    #Switching from white to black pieces 
    if current_turn == "w": 
        current_turn = "b" 
    else: 
        current_turn = "w" 

    if is_in_check(board, current_turn):
        print("Check!") 