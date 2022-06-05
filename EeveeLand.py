from functions import affirm, clear, pause
from replit import db
def Eevee_Land():
  Eevee_Intro()

def Eevee_Intro():
  print('Welcome to Eevee Land. Where would you like to go? ')
  print('')
  lol = ''
  while lol != '1' and lol != '2' and lol != '3' and lol != '4':
    print('(1) Shiny Lab ')
    print('')
    print('(2) Training Grounds ')
    print('')
    print('(3) Upgrade Eevee Evolutions')
    print('')
    print('(4) Leave ')
    print('')
    lol = input()
    clear()
  if lol == '1':
    ShinyLab()
  elif lol == '2':
    TrainingGrounds()
  elif lol == '3':
    clear()
    EeveeBuff()
  elif lol == '4':
    clear()
    return ''
def EeveeBuff():
  print('Here you can buy upgrades that will only affect your Eevee and its Evolutions. (also works on the shiny versions).')
  affirm()
  clear()
  p = ''
  while p != '3':
    g = 2000 + (db['Upg'][0] * 250)
    h = 2000 + (db['Upg'][1] * 250)
    print(f"Money: {db['Money']}")
    print(f"Current Attack Boost: {db['Upg'][0]}%")
    print(f"Current Health Boost: {db['Upg'][1]}%")
    print('')
    print(f'(1) Increase Attack by 2 % [{g}$]')
    print('')
    print(f'(2) Increase HP by 2 % [{h}$]')
    print('')
    print('(3) Leave')
    p = input()
    if p == '1':
      if db['Money'] >= g:
        db['Upg'][0] = db['Upg'][0] + 2
        db['Money'] -= g
        print("You bought the upgrade! ")
        affirm()
        clear()
    elif p == '2': 
      if db['Money'] >= h:
        db['Upg'][1] = db['Upg'][1] + 2
        db['Money'] -= h
        print("You bought the upgrade! ")
        affirm()
        clear()
  clear()
  return ''
        
      
def ShinyLab():
  print('[Professor Shinqs] Welcome to my lab. How may I assist you? ')
  print('')
  print('(1) Learn about Shinys ')
  print('')
  print('(2) Get Quest ')
  print('')
  print('(3) Leave ')
  print('')
  p = input()
  clear()
  if p == '1':
    print('[Professor Shinqs] Well, Shinys are pokemon that have some more favorable traits. We are still studying why this occurs. ')
    affirm()
    clear()
    return ''
  elif p == '2':
    if db['Quests'] == 1:
      print('Coming Soon. Now SCRAM! ')
      affirm()
      clear()
      return ''
  else:
    clear()
    return ''
        
def TrainingGrounds():
  print('Welcome to the training grounds. ')
  print('Here you can gain double xp, and double money. Only twist is there are harder enemies. You cannot catch these pokemon either. ')
  wanna = True
  while wanna == True:
    if db['EeveeHP'] < 1: 
      return ''
    print('Do you want to train? (y/n)')
    x = input().strip()

    if x.lower() == 'y':
      clear()
      from encounter import braining
      braining()
      
    elif x.lower() == 'n':
      print('Bye! ')
      wanna = False
    else: 
      print('Invalid input ')
      affirm()
      clear()

    
  affirm()
  clear()
  return ''
  
  