# To-Do:
# Polywrath miniboss
# Bug fix
from functions import affirm, clear, pause
from replit import db
def City():
  print('A sprawling city, complete with tall skyscrapers is is viewable underneath the ocean... ')
  affirm()
  clear()
  if db['Salve'] == True:
    print('You give the Revival Herb to the Polywhirls guarding the docks. You tell them what it is for. ')
    pause(2)
    print('After inspecting the Revival Herb, they hand it back and let you get on the boat. ')
    pause(3)
    print('When the boat arrives above the city, you are given a scuba helmet, you start swimming to the city.')
    pause(2)
    print('After a long swim, you are brought to the underwater throne room of Vaporeon.')
    affirm()
    pause(1)
    clear()
    print('A Polywhirl walks up and challenges you!')
    from encounter import BPencounter5
    import encounter
    affirm()
    clear()
    BPencounter5()
    clear()
    if db['EeveeHP'] < 1:
      Escape()
      encounter.Boss = False
    if db['EeveeHP'] > 1:
      print("You head over to the Vaporeon's Throne Room...")
      encounter.Boss = False
      affirm()
      clear()
    pause(1)
    clear()
    print('[Vaporeon] Why have my guards let you in?')
    affirm()
    clear()
    print('[Vaporeon] Ah, Leafeon has given me a Revival Herb, let me try it. ')
    affirm()
    clear()
    print('[Vaporeon] Ah, yes! My awful cold is gone!')
    affirm()
    clear()
    print('You tell Vaporeon of the journey Leafeon sent you on.')
    affirm()
    clear()
    print('[Vaporeon] Well then, we should battle to test your strength to see if your ready for what lies ahead.')
    from encounter import BPencounter3
    import encounter
    affirm()
    clear()
    BPencounter3()
    clear()
    db['Salve'] = 2
    print('[Vaporeon] Leave and heal up, come back afterwards. I have something important to tell you.')
    encounter.Boss = False
    affirm()
    clear()
  elif db['Salve'] == 2:
    db['AreaName2'] = 'Fight Ultra-Kyogre'
    print('[Vaporeon] Well you have proved to be strong.')
    affirm()
    clear()
    print("[Vaporeon] I think you're ready to fight Ultra-Kyogre!")
    affirm()
    clear()
    print("[Vaporeon] Ultra-Kyogre is blocking the way to Vulpix Vally, you're going to have to beat it to get there.")
    affirm()
    clear()
    print('[Vaporeon] Oh! About that travel charm of mine, umm, it broke.')
    affirm()
    clear()
    print("[Vaporeon] Well... errr, uh... I'm sure Jolteon can fix it, just give it to him. Jolteon should be at Chick-fil-a (placeholder), just behind Vulpix Volcano.")
    db['Salve'] = 3
  elif db['Salve'] > 2:
    print("[Vaporeon] Well? Move out of the way, I've got work to do!")
    affirm()
    clear()
    
    
  else:
    print("You head over the to the docks to see how to enter the city. The Polywhirl at the dock shakes his head and informs you that Vaporeon, their king, is sick.")
    print('He denies you entry, Maybe Leafeon can help? ')
    db['Tip'] = 2
  affirm()
  clear()

def Escape():
  clear()
  