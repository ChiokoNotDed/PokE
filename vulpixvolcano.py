from functions import pause, affirm, clear
from replit import db

def Volcano():
  print("Plumes of gray smoke bellow out from the Volcano, you attempt to enter the volcano, when a Ninetails appears in front of you. ")
  affirm()
  clear()
  if db['Salve'] == True:
    db['Salve'] = 6
  if db['Salve'] == 3:
    print('You are challenged by the Ninetails. ')
    affirm()
    clear()
    from encounter import BPencounter4
    BPencounter4()
    if db['EeveeHP'] > 0:
      db['Salve'] = 4
      print('[Ninetails] Well, you might be the one we have been looking for. Recently, our leader Flareon went missing. ')
      affirm()
      clear()
      print('[Ninetails] Many believe she has been kidnapped, but I believe otherwise. ')
      affirm()
      clear()
      print('[Ninetails] I think that Flareon used the travel charm given to her by Vaporeon to escape to the scorched forest. ')
      affirm()
      clear()
      print('[Ninetails] When you are looking for pokemon in this region, could you please keep an eye out for Princess Flareon? ')
      affirm()
      clear()
      print('[Ninetails] She may be cranky, and you might have to defeat her, but it is what must be done to return her to the throne. ')
      affirm()
      clear()
    
      
    else:
      print('[Ninetails] Come back when you are stronger, you cannot help us in your current state. ')
      affirm()
      clear()
  elif db['Salve'] == 4:
    print('[Ninetails] Please find Princess Flareon, you might find her when looking for pokemon in our region. The fate of Vulpix Volcano depends on you! ')
    affirm()
    clear()
  elif db['Salve'] == 5:
    print('[Ninetails] Well. Thank you for returning the princess to us. You may have her travel charm. I have given her a stern talking to, and hopefully she will not go off again. ')
    affirm()
    clear()
    print('[Ninetails] Well... As my gift to you, I will gift you a Pokemon. You must have heard of the legendary pokemon. Well, we recently found an egg of the Ancient Reshiram. We have raised it, and now I would like to put her into your care. ')
    Entry = 'Reshiram,1'
    db['Pokemon'].append(Entry)
    db['Salve'] =6
    print('[Ninetails] Good Luck. Go back to Queen Leafeon for the next part of your journey. ')
    affirm()
    clear()
  elif db['Salve'] > 5:
    print("[Princess Flareon] Well, I can't help. Ask Leafy Queen ")
    affirm()
    clear()
  