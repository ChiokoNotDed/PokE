import random
from encounter import Pencounter2
from functions import clear
from replit import db


board = [
  ["+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ "],
  ["+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ "],
  ["+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ "],
  ["+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ "],
  ["+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ "],
  ["+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ "],
  ["+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ "],
  ["+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","@ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ "],
  ["+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ "],
  ["+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ "],
  ["+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ "],
  ["+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ "],
  ["+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ "],
  ["+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ "],
  ["+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ ","+ "]
]
MyShiny = False


def find_loc():
  for y in range(len(board)):
    for x in range(len(board[y])):
      if board[y][x] == "@ ":
        return y,x

def spawn_pokemon():
  global board
  pokemon_count = 0
  for y in board:
    for x in y:
      if x == "\u001b[34;1m!\u001b[0m ":
        pokemon_count += 1
  if pokemon_count < 8:
    while True:
      x_loc = random.randint(0,len(board[0])-1)
      y_loc = random.randint(0,len(board)-1)
      if board[y_loc][x_loc] == "+ ":
        z = random.randint(1,2048)
        if db['Perfume'] > 0 and z == 2048:
          z = 1
        if z == 1:
          board[y_loc][x_loc] = "\u001b[31;1m!\u001b[0m "
        else:  
          board[y_loc][x_loc] = "\u001b[34;1m!\u001b[0m "
        print_board()
        break

def print_board():
  out = ""
  for y in board:
    for x in y:
      out += x
    out += "\n"
  clear()
  print(out)

def up(counter):
  global board
  loc = find_loc()
  MyShiny = False
  try:
    if board[loc[0]-1][loc[1]] == "\u001b[34;1m!\u001b[0m ":
      db['Perfume'] = counter
      Pencounter2(MyShiny)
      board[loc[0]-1][loc[1]] = "+ "
    elif board[loc[0]-1][loc[1]] == "\u001b[31;1m!\u001b[0m ":
      MyShiny = True
      db['Perfume'] = counter
      Pencounter2(MyShiny)
      board[loc[0]-1][loc[1]] = "+ "
    else:
      board[loc[0]-1][loc[1]] = "@ "
      board[loc[0]][loc[1]] = "+ "
  except IndexError:
    pass
  print_board()

def down(counter):
  global board
  MyShiny = False
  loc = find_loc()
  try:
    if board[loc[0]+1][loc[1]] == "\u001b[34;1m!\u001b[0m ":
      db['Perfume'] = counter
      Pencounter2(MyShiny)
      board[loc[0]+1][loc[1]] = "+ "
    elif board[loc[0]+1][loc[1]] == "\u001b[31;1m!\u001b[0m ":
      MyShiny = True
      db['Perfume'] = counter
      Pencounter2(MyShiny)
      board[loc[0]+1][loc[1]] = "+ "
    else:
      board[loc[0]+1][loc[1]] = "@ "
      board[loc[0]][loc[1]] = "+ "
  except IndexError:
    pass
  print_board()

def left(counter):
  global board
  MyShiny = False
  loc = find_loc()
  try:
    if board[loc[0]][loc[1]-1] == "\u001b[34;1m!\u001b[0m ":
      db['Perfume'] = counter
      Pencounter2(MyShiny)
      board[loc[0]][loc[1]-1] = "+ "
    elif board[loc[0]][loc[1]-1] == "\u001b[31;1m!\u001b[0m ":
      MyShiny = True
      db['Perfume'] = counter
      Pencounter2(MyShiny)
      board[loc[0]][loc[1]-1] = "+ "
    else:
      board[loc[0]][loc[1]-1] = "@ "
      board[loc[0]][loc[1]] = "+ "
  except IndexError:
    pass
  print_board()

def right(counter):
  global board
  MyShiny = False
  loc = find_loc()
  try:
    if board[loc[0]][loc[1]+1] == "\u001b[34;1m!\u001b[0m ":
      db['Perfume'] = counter
      Pencounter2(MyShiny)
      board[loc[0]][loc[1]+1] = "+ "
    elif board[loc[0]][loc[1]+1] == "\u001b[31;1m!\u001b[0m ":
      MyShiny = True
      db['Perfume'] = counter
      Pencounter2(MyShiny)
      board[loc[0]][loc[1]+1] = "+ "
    else:
      board[loc[0]][loc[1]+1] = "@ "
      board[loc[0]][loc[1]] = "+ "
  except IndexError:
    pass
  print_board()