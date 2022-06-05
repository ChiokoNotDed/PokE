from replit import db
from functions import affirm, clear, pause
from encounter import trophycounter
import json
import replit
import requests
import os
import colorama
import colors
from colorama import *
requests.packages.urllib3.disable_warnings()

token = 's1lveredisthebest'

requests.post("https://gdb-server.austin2022.repl.co/adduser",data={"user":token})

def getDB():
  db = json.loads(requests.get('https://gdb-server.austin2022.repl.co/get', data={"user":token},verify=False).text)
  return db

def postDB(leaderboard):
  requests.post('https://gdb-server.austin2022.repl.co/update',data={"user":token, "db":json.dumps(leaderboard)})

def leader():
  username = os.environ["REPL_OWNER"]
  db[username] = {"trophy": db['Trophys']}
  leaderboard = getDB()
  print(leaderboard, type(leaderboard))
  leaderboard[username] = db[username]["trophy"]
  postDB(leaderboard)
  affirm()
  clear()
def view():
  clear()
  leaderboard = getDB()
  t9 = 0
  h = []
  
  
  for i in leaderboard:
    if i in ['GoogleMeet4']:
    
      
      h.append(i)
  for g in h:
    del leaderboard[g]
    
  postDB(leaderboard)
  liste = []
  for i in leaderboard:
    liste.append([i, leaderboard[i]])
  liste.sort(key = lambda liste: liste[1])
  liste.reverse()
  # leaderboard.sort(reverse=True, key = lambda, leaderboard: leaderboard[1])

  for i in liste:
    if i[0] in ['Pokesus', 'a-repl-user', 'AlanLeyfer']:
      x = f'{colors.Purple}{colors.bold}[Shiny Tamer] {colors.reset}'
    elif i[0] in ['HyperAlternative', 'IcemasterEric', 'ColoredHue', 'S1lveredPrism']:
      x = f'{colors.Cyan}{colors.bold}[Developer] {colors.reset}'
    else:
      x = ''
    if t9 < 10:
      t9 += 1
      if t9 == 1:
        print(f'{x}{Fore.GREEN}{i[0]} | {leaderboard[i[0]]} trophys {Fore.RESET}')
      elif t9 == 2:
        print(f'{x}{Fore.YELLOW}{i[0]} | {leaderboard[i[0]]} trophys {Fore.RESET}')
      elif t9 == 3:
        print(f'{x}{Fore.RED}{i[0]} | {leaderboard[i[0]]} trophys {Fore.RESET}' )
      else:
        print(f'{x}{Fore.RESET}{i[0]} | {leaderboard[i[0]]} trophys {Fore.RESET}')

      

  affirm()
  clear()
def fights():
  g = '' 
  while g.lower() != 'n' and db['EeveeHP'] > 0:
    print(f'''
  Trophys: {db['Trophys']}
  (y) Battle
  (n) Leave
  (p) Add Data to Leaderboard
  (v) View Leaderboard
          ''')
    g = input().strip()
    if g.lower() == 'y':
      trophycounter()
      clear()
    elif g.lower()== 'p':
      leader()
    elif g.lower()== 'v':
      view()
    else:
      clear()
      return ''
  clear()
  return ''


