
from functions import pause, affirm, clear
from replit import db

def Volcano():
  print("you go into a mysterious cave when you encounter a strange pokemon. ")
  affirm()
  clear()
  if db['Salve'] == True:
    db['Salve'] = 6
  if db['Salve'] == 3:
    print('you are challenged by the strange pokemon. ')
    affirm()
    clear()
    from encounter import BPencounter4
    BPencounter4()
    if db['EeveeHP'] > 0:
      db['Salve'] = 4
      print('[Poken] Poke Poke Poke! Tumph, you dont think ill let you off that easy, do you? You owe me now, your antics will cost me a lot. ')
      affirm()
      clear()
      print('[Poken] Poke Poke Poke! Whats that? your too ¨poor¨? Whatever, I dont care, you can pay me another way then- ')
      affirm()
      clear()
      print('[Poken] I want a home, this cave is awfully unsatistfying, im sure you have a much much better place to live, right? ')
      affirm()
      clear()
      print('[Poken] ... ')
      affirm()
      clear()
      print('[Poken] Your not in good enough shape, your weak, a wimp. ')
      affirm()
      clear()
    
      
    else:
      print('[Poken] Come back when you are stronger, come back when your more worthy of my presence, mutt. ')
      affirm()
      clear()
  elif db['Salve'] == 4:
    print('[Poken] Hello again, ... you wouldnt mind bringing me Sweet Berries, right, I really like those. ')
    affirm()
    clear()
  elif db['Salve'] == 5:
    print('[Poken] Why thankyou! Its clear you´ve improved your abilities a lot. ')
    affirm()
    clear()
    print('[Poken] As promised, I feel your worthy of my eternal presence. So.. ')
    Entry = 'Poken,1'
    db['Pokemon'].append(Entry)
    db['Salve'] =6
    print('[Poken] Why lets get going, shall we? ')
    affirm()
    clear()
  elif db['Salve'] > 5:
    print("[Poken]...  ")
    affirm()
    clear()
