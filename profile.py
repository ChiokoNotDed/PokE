from functions import pause, affirm, clear
from replit import db

def ProfileView():
  if db['Type']==1:
    PT1 = "Normal"
  elif db['Type']==2:
    PT1 = "Grass"
  elif db['Type']==3:
    PT1 = "Water"
  elif db['Type']==4:
    PT1 = "Fire"
  elif db['Type']==5:
    PT1 = "Flight"
  elif db['Type']==6:
    PT1 = "Ground"
  elif db['Type']==7:
    PT1 = "Dark"
  elif db['Type']==8:
    PT1 = "Poison"
  elif db['Type']==9:
    PT1 = "Electric"
  elif db['Type']==10:
    PT1 = "Ice"
  elif db['Type']==11:
    PT1 = "Fighting"
  elif db['Type']==12:
    PT1 = "Psychic"
  elif db['Type']==13:
    PT1 = "Ghost"
  elif db['Type']==14:
    PT1 = "Bug"
  elif db['Type']==15:
    PT1 = "Rock"
  elif db['Type']==16:
    PT1 = "Dragon"
  elif db['Type']==17:
    PT1 = "Steel"
  elif db['Type']==18:
    PT1 = "Fairy"
  if db['Type2']==1:
    PT2 = "Normal"
  elif db['Type2']==2:
    PT2 = "Grass"
  elif db['Type2']==3:
    PT2 = "Water"
  elif db['Type2']==4:
    PT2 = "Fire"
  elif db['Type2']==5:
    PT2 = "Flight"
  elif db['Type2']==6:
    PT2 = "Ground"
  elif db['Type2']==7:
    PT2 = "Dark"
  elif db['Type2']==8:
    PT2 = "Poison"
  elif db['Type2']==9:
    PT2 = "Electric"
  elif db['Type2']==10:
    PT2 = "Ice"
  elif db['Type2']==11:
    PT2 = "Fighting"
  elif db['Type2']==12:
    PT2 = "Psychic"
  elif db['Type2']==13:
    PT2 = "Ghost"
  elif db['Type2']==14:
    PT2 = "Bug"
  elif db['Type2']==15:
    PT2 = "Rock"
  elif db['Type2']==16:
    PT2 = "Dragon"
  elif db['Type2']==17:
    PT2 = "Steel"
  elif db['Type2']==18:
    PT2 = "Fairy"
  elif db['Type2'] == 19:
    PT2 = ''
  PokeType2 = True
  if PT1 == PT2:
    PT2 = ""
    PokeType2 = False
  print("Selected pokemon:",db['PokemonName'])
  print(db['PokemonName']+"'s level:",db['EeveeLv'])
  xpnow = str(db['Encounters'])

  print(db['PokemonName']+"'s xp:",xpnow+"/"+str((db['EeveeLv'] * 100) + (db['EeveeLv']*5)))
  print(db['PokemonName']+"'s max hp:",db['EeveeLv']*2)
  if not PokeType2==True:
    print(db['PokemonName']+"'s type:",PT1)
  else:
    print(db['PokemonName']+"'s types:",PT1,"and",PT2)
  print("Money:",str(db['Money'])+"$")
  print('')
  print(f"Trophys: {db['Trophys']}")
  affirm()
  clear()
  return''