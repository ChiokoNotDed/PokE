from replit import db
from functions import affirm, clear, pause
import json
import replit
import requests
import os
import random
import colorama
import colors
from colorama import *
requests.packages.urllib3.disable_warnings()

token = 's1lveredisthebest2'

requests.post("https://gdb-server.austin2022.repl.co/adduser",data={"user":token})

def getDB():
  db = json.loads(requests.get('https://gdb-server.austin2022.repl.co/get', data={"user":token},verify=False).text)
  return db

def postDB(leaderboard):
  requests.post('https://gdb-server.austin2022.repl.co/update',data={"user":token, "db":json.dumps(leaderboard)})

def leader():
  username = os.environ["REPL_OWNER"]
  teams = ''
  po = 0
  for i in db['PokeTeam']:
    x = db['PokeTeam'][po][0]
    if 'Shiny-' in x:
                          u = 0
                          b = ''
                          for i in x:
                           
                            u += 1 
                            if u >6:
                              b += i
                          z = b
                          teams += z
                          teams += ','
    elif x == 'Empty':
      pass
    else:
                          z = x
                          teams += z
                          teams += ','
    po += 1
  if 'Shiny-' in db['NoShiny']:
                          u = 0
                          b = ''
                          for i in db['NoShiny']:
                           
                            u += 1 
                            if u >6:
                              b += i
                          z = b
  teams += db['NoShiny']


  db[username] = {"MyTeam": teams}
  leaderboard = getDB()
  leaderboard[username] = db[username]["MyTeam"]
  postDB(leaderboard)




def gui():
  print(f"""
        (1) Battle Specific Trainer
        
        (2) Battle Random Trainer
        
        (3) Upload Yourself/Team to Server

        (4) Return to Main Page
        
       """)
  choice = input()

  if choice == '1':
    leaderboard = getDB()
    print('Who would you like to battle? Enter their username. Users are case sensitive. ')
    x = input()
    Characters = []
    for i in leaderboard:
      Characters.append(i)
    if x in Characters:
      Him = x
      Team = leaderboard[Him]
      from encounter import Brop
      Brop(Team, Him)
    else:
      print('User not in server. ')
      affirm()
      clear()
  elif choice == '2':
    from encounter import Brop
    leaderboard = getDB()
    Characters = []
    for i in leaderboard:
      Characters.append(i)
    Him = random.choice(Characters)
    Team = leaderboard[Him]
    Brop(Team, Him)
  elif choice == '3':
    leader()
  elif choice == '4':
    return ''
  clear()
  gui()
  