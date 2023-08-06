# board
board  = ["_","_","_",
          "_","_","_",
          "_","_","_"]

game_still_going = True

#who won or tie?
winner = None

#who is playing?
current_player = "X"

# display board
def display_board():
  print(board[0]+ " | "+board[1]+" | "+board[2])
  print(board[3]+ " | "+board[4]+" | "+board[5])
  print(board[6]+ " | "+board[7]+" | "+board[8])

#play a game of tic tac toe
def play_game():
  #display the initial board
  display_board()

  #while the game is still going
  while game_still_going:

    #handle a single turn of an arbitrary player
    handle_turn(current_player)

    #check if the game has ended
    check_if_game_over()

    #game over
    if winner == "X" or winner == "0":
      print(winner +  " won.")
    elif winner == None:
      print("Tie.")

    #flip to the other player
    flip_player()


def handle_turn(player):
  position = input("Choose position bewteen 1 to 9: ")
  position = int(position) - 1

  board[position] = player
  display_board()

def check_if_game_over():

  check_if_win()
  check_if_tie()

def check_if_win():

  #set up global variables
  global winner

  #check rows
  row_winner = check_rows()
  #check columns
  column_winner = check_columns()
  #check diagonals
  diagonal_winner = check_diagonals()
  if row_winner:
    #there was a winner
    winner = row_winner
  elif column_winner:
    #there was a winner
    winner = column_winner
  elif diagonal_winner:
    #there was a winner
    winner = diagonal_winner
  else:
    #there was no win
    winner = None
  return

def check_rows():
  #set up global variables
  global game_still_going

  #check if any of the row has same value and is not empty
  row_1 = board[0] == board[1] == board[2] != "_"
  row_2 = board[3] == board[4] == board[5] != "_"
  row_3 = board[6] == board[7] == board[8] != "_"

  if row_1 or row_2 or row_3:
      game_still_going = False
  #return the winner
  if row_1:
    return board[0]
  elif row_2:
    return board[3]
  elif row_3:
    return board[6]
  return

def check_columns():
  # set up global variables
  global game_still_going

  # check if any of the column has same value and is not empty
  column_1 = board[0] == board[3] == board[6] != "_"
  column_2 = board[1] == board[4] == board[7] != "_"
  column_3 = board[2] == board[5] == board[8] != "_"

  if column_1 or column_2 or column_3:
    game_still_going = False
  # return the winner
  if column_1:
    return board[0]
  elif column_2:
    return board[1]
  elif column_3:
    return board[2]
  return

def check_diagonals():
  # set up global variables
  global game_still_going

  # check if any of the row has same value and is not empty
  diagonal_1 = board[0] == board[4] == board[8] != "_"
  diagonal_2 = board[2] == board[4] == board[6] != "_"

  if diagonal_1 or diagonal_2:
    game_still_going = False
  # return the winner
  if diagonal_1:
    return board[0]
  elif diagonal_2:
    return board[2]
  return

def check_if_tie():
  if "_" not in board:
    game_still_going = False
def flip_player():
  global current_player

  if current_player == "X":
    current_player = "O"
  elif current_player == "O":
     current_player = "X"
  return

play_game()

