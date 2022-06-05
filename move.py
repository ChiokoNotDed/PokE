from replit import clear, db
from functions import affirm
import board
from getkey import getkey, keys
import random
from encounter import Pencounter2
import colors

def update():
	clear()

def Pokemon():
  board.board = [
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
  board.spawn_pokemon()
  board.spawn_pokemon()
  board.spawn_pokemon()
  board.spawn_pokemon()
  board.spawn_pokemon()
  board.print_board()
  counter = db['Perfume']
  while True:
    
    if db['EeveeHP'] > 0:
      if counter > 0:
        print(f'Your Shiny Perfume will wear off in {counter} steps..  ')
      print("Use arrow keys or WASD to move\n\nClick 'e' to go back to main page. ")
      key = getkey()
      counter -= 1
      
      if key == keys.LEFT or key == keys.A:
        
        board.left(counter)
        z = random.randint(1, 4)
        if z == 4:
          board.spawn_pokemon()
        
      elif key == keys.RIGHT or key == keys.D:

        board.right(counter)
        z = random.randint(1, 4)
        if z == 4:
          board.spawn_pokemon()
      elif key == keys.UP or key == keys.W:

        board.up(counter)
        z = random.randint(1, 4)
        if z == 4:
          board.spawn_pokemon()
      elif key == keys.DOWN or key == keys.S:

        board.down(counter)
        z = random.randint(1, 4)
        if z == 4:
          board.spawn_pokemon()
      elif key == keys.E:
        db['Perfume'] = counter
        clear()
        return ''
    else:
      return ''