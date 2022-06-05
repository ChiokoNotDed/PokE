import json, time, os, replit, random
from getkey import getkey, keys
from replit import db
from functions import affirm
USER = os.environ["REPL_OWNER"]
def Account():
  if not 'JASON' in db.keys():
    with open(USER+".env", "w") as outfile:
      Var1 = "E"
      json.dump(Var1, outfile)
    db['Fre'] = ('PokeBot')
    db['JASON'] = True 
    LOL = ""
    db['No'] = 1
  else: 
    with open(USER+".env") as infile:
      Var2 = json.load(infile)
      if not Var2=="E":
        if not Var2 in db['Fre']:
          print("Would you like to add",Var2,"as a friend? 1: YES 2: NEVER")
          Var69 = input("Response:")
          if Var69=="1":
            db['Fre'].append(Var2)
            db['No']+=1
          else:
            print(f"I pity {Var2} .")
            time.sleep(2)
          with open(USER+".env", "w") as outfile:
            Var1 = "E"
            json.dump(Var1, outfile)
        else:
          pass

def Friends():
  LOL = ""
  No2 = 0
  while True:
    replit.clear()
    LOL = db['Fre'][No2]
    print("Total friends:",db['No'])
    print(LOL)
    print("Press a or left arrow to move left. Press d or right arrow to move right. Get new friends by pressing L! Press E to exit")
    Urmum = getkey()
    while True:
      if Urmum=='a' or keys.LEFT:
        if No2!=0:
          No2-=1
        break
      elif Urmum=='d' or keys.RIGHT:
        if No2!=(db['No']-1):
          No2+=1
        break
      elif Urmum=="l":
        print("Input the name of the person you would like to add:")
        AFR = input("---->")
        if not AFR == USER:
          try:
            with open(AFR+".env", "w") as outfile:
              json.dump(USER, outfile)
              print("Sent!")
              affirm()
          except FileNotFoundError:
            print("User not found.")
            affirm()
        else:
          print("You ccan't friend yourself, dummy!")
          affirm()
      elif Urmum=="e":
        replit.clear()
        return
      else:
        pass
      break