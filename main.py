from functions import affirm, clear, pause
from replit import db
import json
import replit
import battlemoves
import requests
import os
import time
import dino_info
import random
from move import Pokemon
import thorns #its a module in this game
import pokedex
import colorama
from colorama import *
import encounter
import pokemon
import colors
import time
from profile import ProfileView
from pokemon import berries, ingredients
from LonelyIsMe import Account, Friends

print(f'{colors.Red}This Game was made by leisiki 레이시키 and is copyrighted by Shiriganjisi


  {colors.reset}')
affirm()
clear()


_username = os.environ["REPL_OWNER"]
if _username == 'LeisikiSoKawaii' and 'MONEYBAG' not in db.keys():
  db['MONEYBAG'] = 0
  db['Money'] += 50000

userdata = {}
_userdata = [i for i in db]

for i in _userdata:
    userdata[i] = db[i]
# token = 'PokemonUltimates'
# def create_account(token):
#   # take note of data, which is a dictionary and contains the info you are sending to the server.
#   requests.post('https://gdb-server.austin2022.repl.co/adduser',data={"user":token})
#   return True
#Account()

def save_data(username):
    requests.post("https://S1lvered-DB.s1lveredprism.repl.co/update",
                  data={
                      "user": username,
                      "db": replit.database.dumps(userdata)
                  })

def load_data(username):
    _userdata = json.loads(
        requests.get("https://S1lvered-DB.s1lveredprism.repl.co/get",
                     data={
                         "user": username
                     }).text)
    db.clear()
    for i in _userdata:
        db[i] = _userdata[i]



if 'Loaded' in db.keys():
    print(
        '''\033[2mPls give me money on patreon btw. \033[0m\nYou have saved progress, would you like to keep it or delete it? Type "Yes" to clear all progress, and if not, press [Enter]'''
    )
    x = input()
    if (x.strip()).lower() == 'yes':
        db.clear()
        db['Reset'] = 'Ye Cleansed'

if not 'Roar' in db.keys():
    db['Roar'] = True
    db['Perfume'] = 0
    db['Pokemon2'] = []
    db['Pokemon3'] = []
    db['Pokemon4'] = []
    db['Pokemon5'] = []
# if not 'StarterChoice' in db.keys():
#   print('''Choose a starter from the list below''')
if not 'BRUH' in db.keys():
    db['BRUH'] = ''
    db['Pokemon2'] = {}
    db['Pokemon3'] = {}
    db['Pokemon4'] = {}
    db['Pokemon5'] = {}
    db['Pokemon6'] = {}

if not 'Cook' in db.keys():
       
  db['Cook'] = [['Leek', 0],['Apple', 0],['Bread', 0],['Steak', 0],['Fries', 0],['Instant Noodles', 0],['Rice', 0],['Chicken Broth', 0],['Cake', 0],['Slowpoke Tail', 0],['Fried Chicken', 0],['Moomoo Milk', 0],['Beans', 0],['Pasta', 0],['Sausage', 0],['Lettuce',0]]

if not 'New' in db.keys():
    db['New'] = True
    db['Pokemon'] = []
    db['Thorns'] = ''
    db['Tip'] = 0
    ThornsOption = ''


def Game():
    import battle
    battle.leader()
    global Thorns, ThornsOption
    import battlemoves
    while 1 == 1:
        input1 = ''
        thorns.Boss = False
        while input1.strip() != '1' and input1.strip() != '2' and input1.strip(
        ) != '3' and input1.strip() != '4' and input1.strip(
        ) != '5' and input1.strip() != '6' and input1.strip() != '7':
            x = (f'''
Area: {db['AreaName']}        
           
Level {db['EeveeLv']} {db['PokemonName']}'s HP: {db['EeveeHP']}  
           
Money: {db['Money']}$     

(1) Look for Pokemon 
(2) Explore {db['AreaName2']}
(3) Open Inventory  
(4) Tutorial   
(5) Heal {db['PokemonName']}
(6) PokeStore (Buy Items)
(7) View/Equip Pokemon
(8) Open Pokedex (See all Pokemon in the Game)
(9) Travel
(10) View Profile
(11) \033[0;34mJurassic World Online\033[0m
(12) Ranked Fights (Earn Trophys And Get on The Leaderboard!)
(13) Add friends (and no longer be lonely)
(14) Battle other Users
           
(s) Save Data
\033[2mData is auto saved, but this will keep data even if you log out of replit\033[0m
(l) Load Data
\033[2mIf you lost your progress, and use this, you will get all the data from 
your last manual save\033[0m
''')
            print(x)
            input1 = input().strip()
            clear()
            if input1 == '1':
                input1 = ''
                if db['EeveeHP'] > 0:
                    Pokemon()
                    clear()
                else:
                    print(
                        f"Heal up your {db['PokemonName']} before exploring! ")
                    affirm()
                    clear()
            elif input1 == 'UwU':
                print('UwU to you as well! ')
                affirm()
                clear()
            elif input1 == '2':
                if db['EeveeHP'] > 0:
                    if db['AreaName2'] == 'Thorn Palace':
                        thorns.ThornPalace()
                    elif db['AreaName2'] == 'Seascaper':
                        if not 'Kitty' in db.keys():
                            db['Kitty'] = True
                            db['Salve'] = False
                        from bigblue import City
                        City()
                    elif db['AreaName2'] == 'Fight Ultra-Kyogre':
                        clear()
                        print('You confront Ultra-Kyogre...')
                        from encounter import BPencounter6
                        import encounter
                        affirm()
                        clear()
                        BPencounter6()
                        if db['EeveeHP'] > 0:
                            clear()
                            print(
                                'Ultra-Kyogre calmed down, he stopped blocking the path to Vulpix Volcano!'
                            )
                            db['AreaName2'] == 'Seascraper'
                            db['Area'].append('Vulpix Vally')
                    elif db['AreaName2'] == 'Vulpix Sanctuary':
                        from vulpixvolcano import Volcano
                        Volcano()
                    elif db['AreaName2'] == 'Courtyard':
                        from EeveeLand import Eevee_Land
                        Eevee_Land()
                    elif db['AreaName2'] == 'Camp':
                        from camping import campsite
                        campsite()

                else:
                    print(
                        f"Heal up your {db['PokemonName']} before exploring! ")
                    affirm()
                    clear()

            elif input1 == '3':
                print(
                    f"You have {db['PokeBalls']} Pokeballs, {db['GreatBalls']} Great Balls, {db['UltraBalls']} Ultra Balls, {db['MasterBalls']} Master Balls, {db['Potions']} Potions, {db['SuperPotions']} Super Potions, {db['HyperPotions']} Hyper Potions, and {db['MasterPotions']} Max Potions.  "
                )
                affirm()
                clear()
            elif input1 == '4':
              
                print(
                    'Look for Pokemon to fight them, and earn money, xp to level up your pokemon, and items! For each ultimate, you will have an area to explore which will involve riddles, rooms, and pokemon fights. At the end of each explore, you will reach an Ultimate Pokemon which you must fight. If you die, you will have to go through the whole explore process again. After you finish exploring an area and beat the ultimate, you will be able to explore a new area! Your data will be saved AFTER you finish exploring an area, so do not quit in between exploring an area or reload the project. Have fun!  '
                )
                affirm()
                clear()

            elif input1 == '5':
                import encounter, battlemoves
                db['PP1'] = battlemoves.moves[battlemoves.movesid[db['MOVE1']]][6]
                db['PP2'] = battlemoves.moves[battlemoves.movesid[db['MOVE2']]][6]
                encounter.mpoison = False
                encounter.mburn = False
                encounter.mstun = False
                encounter.mfreeze = False
                encounter.mconfuse = False
                for i in [0, 1,2, 3, 4]:
                  db['PokeTeam'][i][2] = round(db['PokeTeam'][i][1] * 3)
                  db['PokeTeam'][i][3] = db['PokeTeam'][i][5]
                  db['PokeTeam'][i][4] = db['PokeTeam'][i][6]
                if 'Shiny' in db['PokemonName']:
                    if db['EeveeHP'] < (db['EeveeLv'] * 3):
                        db['EeveeHP'] = db['EeveeLv'] * 3
                        print(
                            f"Your {db['PokemonName']} was healed to full health! "
                        )
                        Up = db['EeveeHP'] / 100
                        Up = Up * db['Upg'][1]
                        db['EeveeHP'] += Up
                        db['EeveeHP'] = round(db['EeveeHP'])
                elif db['PokemonName'] == 'Chandelure' or db['PokemonName'] == 'Lampent' or db[
                        'PokemonName'] == 'Leafeon' or db['PokemonName'] == 'Noivern' or db[
                            'PokemonName'] == 'Raichu' or db['PokemonName'] == 'Weezing' or db[
                                'PokemonName'] == 'Furret' or db['PokemonName'] == 'Gyarados' or db[
                                    'PokemonName'] == 'Jigglypuff' or db['PokemonName'] == 'Sandslash' or db[
                                        'PokemonName'] == 'Polywhirl' or db['PokemonName'] == 'Charizard' or db[
                                            'PokemonName'] == 'Zekrom' or db[
                                                'PokemonName'] == 'Reshiram' or db[
                                                    'PokemonName'] == 'Vaporeon' or db[
                                                        'PokemonName'] == 'Flareon' or db[
                                                            'PokemonName'] == 'Umbreon' or db[
                                                                'PokemonName'] == 'Sylveon' or db[
                                                                    'PokemonName'] == 'Espeon' or db[
                                                                        'PokemonName'] == 'Jolteon' or db[
                                                                            'PokemonName'] == 'Glaceon' or db['PokemonName'] == 'Dragonite' or db['PokemonName'] == 'Lunala' or db['PokemonName'] == 'Solgaleo' or db['PokemonName'] == 'Arceus':

                    db['EeveeHP'] = round((db['EeveeLv'] * 3) * 1.5)
                    Up = db['EeveeHP'] / 100
                    Up = Up * db['Upg'][1]
                    db['EeveeHP'] += Up
                    db['EeveeHP'] = round(db['EeveeHP'])
                    print(
                        f"Your {db['PokemonName']} was healed to full health! "
                    )

                elif db['EeveeHP'] < (db['EeveeLv'] * 3):
                    print(
                        f"Your {db['PokemonName']} was healed to full health! "
                    )
                    db['EeveeHP'] = db['EeveeLv'] * 3
                    affirm()
                    Up = db['EeveeHP'] / 100
                    Up = Up * db['Upg'][1]
                    db['EeveeHP'] += Up
                    db['EeveeHP'] = round(db['EeveeHP'])
                    clear()
                else:

                    print(
                        f"Your {db['PokemonName']} is already at full health!")
                    affirm()
                    clear()

            elif input1 == '100k' and '100k' not in db.keys():
                db['100k'] = True
                db['Money'] += 100000
            elif input1 == '12':
              from trophy import fights
              clear()
              fights()
              clear()
              
            elif input1 == '1k':
                if not '1k' in db.keys():
                    db['1k'] = 'UwU'
                    db['Money'] += 10000
                    db['Perfume'] += 200
                    db['GreatBalls'] += 100
            elif input1 == '6':

                print("Welcome to the Pokestore! ")
                print('')
                print("Here is our current stock: ")
                print(
                    'Potions - 500$ (Restores up to 20 HP! ! 10 per purchase)')
                print('')
                print('Pokeballs - 200$ (You get 10 per purchase) ')
                print('')
                print('Great Balls - 750$ (You get 10 per purchase)')
                print('')
                print(
                    f"Rare candy - {1000 + (db['EeveeLv']*100)}$ (Increases pokemon level by 1! You get 1 per purchase)"
                )
                print('')
                print(
                    'Sheening Perfume - 1000$ (Doubles chance of finding Shiny Pokemon for 500 steps! [Stackable, and and effect applied on purchase])'
                )
                print('')
                print('Master Ball - 5000$ (100% Catch Accuracy)')
                print('')
                if db['Double'] == False:
                    print(
                        'Amulet Coin - 25000$ (Doubles Money earned from battles)'
                    )
                    print('')
                if db['FIGHT'] == False:
                    print('Critical Gem - 20000$ (Increases Damage Dealt)')
                    print('')
                print(f"You have {db['Money']}$!")

                print("(1) Buy 10 Potions (500$)")
                print("(2) Buy 10 Pokeballs (200$)")
                print("(3) Buy 10 Great Balls (750$)")
                print("(4) Buy Sheening Perfume (1000$)")
                print(f"(5) Buy Rare Candy ({1000 + (db['EeveeLv']*100)}$)")
                print("(6) Buy Master Ball (5000$)")
                if db['Double'] == False:
                    print("(7) Buy Amulet Coin (25000$)")
                if db['FIGHT'] == False:
                    print("(8) Buy Critical Gem (20000$")

                print("(Enter) Back")
                x = input('')
                x = x.strip()
                if x == '1':
                    if db['Money'] > 500:
                        print(
                            'You bought a Potion! It has been added to your inventory '
                        )
                        db['Money'] -= 500
                        db['Potions'] += 10
                        affirm()
                        clear()
                    else:
                        print('Oh noes! Not enough money! ')
                        affirm()
                        clear()
                if x == '2':
                    if db['Money'] > 200:
                        print(
                            'You bought 10 Pokeballs! They have been added to your inventory '
                        )
                        db['Money'] -= 200
                        db['PokeBalls'] += 10
                        affirm()
                        clear()
                    else:
                        print('Not enough money')
                        affirm()
                        clear()
                if x == '3':
                    if db['Money'] > 750:
                        print(
                            "You bought 10 Great Balls! They have been added to your inventory! "
                        )
                        db['GreatBalls'] += 10
                        db['Money'] -= 750
                        affirm()
                        clear()
                    else:
                        print('Oh Noes! Not enough money! ')
                        affirm()
                        clear()
                if x == '6':
                    if db['Money'] >= 5000:
                        print('You bought a Master Ball! ')
                        db['MasterBalls'] += 1
                        db['Money'] -= 5000
                        affirm()
                        clear()
                    else:
                        print('Oh Noes! Not enough money! ')
                        affirm()
                        clear()
                if x == '4':
                    if db['Money'] > 1000:
                        print(
                            "You bought a Sheening Perfume! The effect has been applied! "
                        )
                        db['Money'] -= 1000
                        db['Perfume'] += 500
                    else:
                        print('Not enough money')
                        affirm()
                        clear()
                if x == '7' and db['Double'] == False:
                    if db['Money'] >= 25000:
                        db['Double'] = True
                        db['Money'] -= 25000
                        print('You bought the Amulet Coin!')
                    else:
                        print('Not enough money ')
                        affirm()
                        clear()

                if x == '8' and db['FIGHT'] == False:
                    if db['Money'] >= 20000:
                        db['Money'] -= 20000
                        db['FIGHT'] = True
                        print('You bought the Critical Gem! ')
                        affirm()
                        clear()
                if x == '5':
                    if db['Money'] >= 1000 + (db['EeveeLv'] * 100):
                        db['EeveeLv'] += 1
                        print(
                            f"You bought a Rare Candy! Your {db['PokemonName']}  is now level",
                            db['EeveeLv'], "!")
                        db['Money'] -= 1000 + (db['EeveeLv'] * 100)
                        affirm()
                        clear()

                    else:
                        print('Not enough money')
                        affirm()
                        clear()
                else:
                    clear()
            elif input1 == 'gottacatchemall':
                if not 'EasterEgg1' in db.keys():
                    db['EasterEgg1'] = True
                    db['GreatBalls'] += 10
                    db['Potions'] += 10
                    db['Perfume'] += 50
                    print(
                        'You unlocked your one-time catch kit! You got 10 Great Balls, 10 Potions, and 50 turns worth of Sheeing Perfume! '
                    )
                    affirm()
                    clear()
                else:
                    db['Money'] -= round(db['Money'] / 10)
                    print(
                        "You greedy little bugger, you want this again? Well you just lost 10 percent of your money. LOL "
                    )
                    affirm()
                    clear()
            elif input1 == '7':
                clear()
                x = '2'
                if x == '2':
                    TeamSlot = ''
                    print(f'''Which slot would you like to change?
         (1)  Level {db['EeveeLv']} {db['PokemonName']} 

         (2)  Level {db['PokeTeam'][0][1]} {db['PokeTeam'][0][0]}
                          
         (3)  Level {db['PokeTeam'][1][1]} {db['PokeTeam'][1][0]}
                          
         (4)  Level {db['PokeTeam'][2][1]} {db['PokeTeam'][2][0]}
                          
         (5)  Level {db['PokeTeam'][3][1]} {db['PokeTeam'][3][0]}
                          
         (6)  Level {db['PokeTeam'][4][1]} {db['PokeTeam'][4][0]}
                          ''')
                    input2 = input()
                    try:
                      TeamSlot = int(input2)
                      if TeamSlot > 6:
                        return ''
                    except:
                      return ''
                    
                    clear()
                    print('Pokemon: ')
                    print('')

                    v = 0
                    for i in db['Pokemon']:
                        z = i.split(',')

                        print(f"({v}) Level {z[1]} {z[0]}")
                        v += 1
                    print('')
                    x = input('What pokemon would you like to equip?\n')
                    x = x.strip()
                    x = int(x)

                    y = db['Pokemon'][x]
                    if y in db['Pokemon']:
                      if TeamSlot == 1:

                        ColoredHue = (db['Pokemon'][x]).split(',')

                        db['Pokemon'].remove(y)
                        db['EeveeLv'] = str(db['EeveeLv'])
                        BeatYouUp = db['PokemonName'] + ',' + db['EeveeLv']
                        db['Pokemon'].append(BeatYouUp)
                        db['Encounters'] = 0

                        db['PokemonName'] = ColoredHue[0]
                        db['EeveeLv'] = int(ColoredHue[1])
                        db['NoShiny'] = ''
                        import pokemon

                        if 'Shiny-' in db['PokemonName']:
                          u = 0
                          for i in db['PokemonName']:
                           
                            u += 1 
                            if u >6:
                              db['NoShiny'] += i
                        else:
                          db['NoShiny'] = db['PokemonName']
                        db['Type'] = pokemon.pokemonn[db['NoShiny']][0]
                        db['Type2'] = pokemon.pokemonn[db['NoShiny']][1]
                        db['MOVE1'] = pokemon.pokemonn[db['NoShiny']][2]
                        db['MOVE2'] = pokemon.pokemonn[db['NoShiny']][3]
                        import battlemoves
                        db['PP1'] = battlemoves.moves[battlemoves.movesid[db['MOVE1']]][6]
                        db['PP2'] = battlemoves.moves[battlemoves.movesid[db['MOVE2']]][6]
                            
                            

                        
                      else:
                        ColoredHue = (db['Pokemon'][x]).split(',')
                        if 'Shiny-' in ColoredHue[0]:
                          u = 0
                          b = ''
                          for i in ColoredHue[0]:
                           
                            u += 1 
                            if u >6:
                              b += i
                        else:
                          b = ColoredHue[0]
                        
                        db['Pokemon'].remove(y)
                        
                        Slot = TeamSlot - 2
                        if db['PokeTeam'][Slot][0] != 'Empty':
                          bob = str(db['PokeTeam'][Slot][1])
                          me = db['PokeTeam'][Slot][0]
                          BeatYouUp = me + ',' + bob
                          db['Pokemon'].append(BeatYouUp)
                        db['PokeTeam'][Slot][0] = ColoredHue[0]
                        db['PokeTeam'][Slot][1] = int(ColoredHue[1])
                        db['PokeTeam'][Slot][2] = int(db['PokeTeam'][Slot][1] * 2)
                        import battlemoves,pokemon
                        move = pokemon.pokemonn[b][2]
                        move2 = pokemon.pokemonn[b][3]
                        db['PokeTeam'][Slot][3] = battlemoves.moves[battlemoves.movesid[move]][6]
                        db['PokeTeam'][Slot][4] = battlemoves.moves[battlemoves.movesid[move2]][6]
                        db['PokeTeam'][Slot][5] = db['PokeTeam'][Slot][3]
                        db['PokeTeam'][Slot][6] = db['PokeTeam'][Slot][4]
                        db['PokeTeam'][Slot][7] = 0
                        
                        
                      clear()
            elif input1 == '14':
              import battle
              battle.gui()
              clear()
            elif input1 == '8':
            
                pokedex.pokeOPEN()
            elif input1 == '9':
                from bigblue import City
                clear()
                print('Map:')
                print('')
                v = 0
                for key in db['Area']:
                    print(f'{v}: {key}', end='')
                    print('')
                    v += 1
                print('')
                print('')
                x = input('Where do you want to travel?\n')
                x = x.strip()
                x = int(x)
                y = db['Area'][x]
                if y in db['Area']:
                    if db['Area'][x] == 'Vine Vally':
                        db['AreaName'] = 'Vine Vally'
                        db['AreaName2'] = 'Thorn Palace'
                    elif db['Area'][x] == 'Big Blue':
                        db['AreaName'] = 'Big Blue'
                        db['AreaName2'] = 'Seascaper'
                        if db['Salve'] == 3:
                            db['AreaName2'] = 'Fight Ultra-Kyogre'
                    elif db['Area'][x] == 'Vulpix Vally':
                        db['AreaName'] = 'Vulpix Volcano'
                        db['AreaName2'] = 'Vulpix Sanctuary'
                    elif db['Area'][x] == 'Eevee Land':
                        db['AreaName'] = 'Eevee Land'
                        db['AreaName2'] = 'Courtyard'
                            
                    elif db['Area'][x] == 'Campsite':
                        db['AreaName'] = 'Campsite'
                        db['AreaName2'] = 'Camp'
                    else:
                        print('Unknown Location')
                        pause(1)
                        clear()
                    clear()
                else:
                    print('Unknown Location')
                    pause(1)
                    clear()
         
            elif input1 == '10':
                ProfileView()
            elif input1 == "s":
                _username = os.environ["REPL_OWNER"]
                save_data(_username)
                clear()
            elif input1 == "l":
                _username = os.environ["REPL_OWNER"]
                load_data(_username)
                clear()
            elif input1 == "11":

                def pokemoves(type):
                    if type == 1:
                        return "Tackle"
                    elif type == 2:
                        return "Vine Whip"
                    elif type == 3:
                        return "Bubble Beam"
                    elif type == 4:  # flamethrower = bleed
                        return "Flamethrower"
                    elif type == 5:  # WS = stun
                        return "Wing Slash"
                    elif type == 6:
                        return "Earthquake"
                    elif type == 7:  # DP = stun
                        return "Dark Pulse"
                    elif type == 8:  # PS = bleed
                        return "Poison Sting"
                    elif type == 9:  # TS = stun
                        return "Thunder Shock"
                    elif type == 10:  # Bliz = stun
                        return "Blizzard"
                    elif type == 11:  # DP = reduce dmg
                        return "Dynamic Punch"
                    elif type == 12:  # Barr = RD 4 now, shield later
                        return "Barrier"
                    elif type == 13:  # BB = bleed
                        return "Bug Bite"
                    elif type == 14:  # RS = stun
                        return "Rock Slide"
                    elif type == 15:  # night = stun
                        return "Nightmare"
                    elif type == 16:  # DR = 2x
                        return "Dragon Rage"
                    elif type == 17:  # IT = reduce dmg
                        return "Iron Tail"
                    elif type == 18:  # Heal
                        return "Heal"

                '''
        notes: (IcemasterEric)
        fix heal (later)
        '''
                clear()
                time.sleep(0.5)
                username = os.environ["REPL_OWNER"]
                Red = "\033[0;31m"
                Green = "\033[0;32m"
                Orange = "\033[0;33m"
                Blue = "\033[0;34m"
                Purple = "\033[0;35m"
                Cyan = "\033[0;36m"
                White = "\033[0;37m"
                reset = '\033[0m'
                bright_black = "\033[0;90m"
                bright_red = "\033[0;91m"
                bright_green = "\033[0;92m"
                bright_yellow = "\033[0;93m"
                bright_blue = "\033[0;94m"
                bright_magenta = "\033[0;95m"
                bright_cyan = "\033[0;96m"
                bright_white = "\033[0;97m"
                darken = "\033[2m"
                print(
                    f"{Blue}IcemasterEric:{reset} Welcome to {Blue}Jurassic World Online{reset}, {username}\n"
                )
                time.sleep(1)
                pokejwo = json.loads(
                    requests.get(
                        "https://JW-Server.icemastereric.repl.co/pokejwo-get").
                    text)
                if pokejwo["dino"] == False:
                    pass
                else:
                    pass
                if pokejwo['dino'] == True:
                    game = f"{bright_yellow}JW Online{reset}"
                else:
                    game = f"{bright_yellow}Pokemon Ultimates{reset}"
                print(
                    f"{darken}Leader:{reset} {Blue}{pokejwo['name']}{reset} - {game} Player {bright_magenta}{pokejwo['user']}{reset}"
                )
                time.sleep(0.7)
                action = input(
                    f"\n0: Leave\n1: Fight {Blue}{pokejwo['name']}{reset}\n\n")
                if action == "0":
                    pass
                elif action == "1":

                    def poke_battle(mob, mob_name):
                        def win():
                            clear()
                            print(
                                f"{Blue}You won! Your Pokemon is now the Champion!{reset}"
                            )
                            pokejwo_info = json.loads(
                                requests.get(
                                    "https://JW-Server.icemastereric.repl.co/pokejwo-get"
                                ).text)
                            poke_attacks = [
                                "Strike",
                                pokemoves(db['Type']), "Intimidate"
                            ]
                            pokejwo_info['dino'] = False
                            pokejwo_info["user"] = username
                            pokejwo_info["name"] = db['PokemonName']
                            pokejwo_info["stats"] = {
                                "hp":
                                round(db['EeveeHP'] * (db['EeveeLv'] / 17) +
                                      800),
                                "dmg":
                                round(db['EeveeDmg'] * 8.7),
                                "attacks":
                                poke_attacks,
                                "speed":
                                round(100 + db['EeveeLv'] * 0.38),
                                "armor":
                                1,
                                "type":
                                db['Type']
                            }
                            requests.post(
                                "https://JW-Server.icemastereric.repl.co/pokejwo-post",
                                data={
                                    "info": replit.database.dumps(pokejwo_info)
                                })
                            time.sleep(0.5)
                            input(f"\n[{Blue}ENTER{reset}]")
                            clear()
                            return

                        def lose():
                            clear()
                            print(f"{Red}You lost.{reset}\n")
                            time.sleep(0.5)
                            input(f"[{Blue}ENTER{reset}]")
                            clear()
                            return

                        used_attacks = {}
                        en_used_attacks = {}
                        # f = friendly e = enemy
                        fdino_name = db['PokemonName']
                        poke_attacks = [
                            "Strike",
                            pokemoves(db['Type']), "Intimidate"
                        ]
                        fdino = {
                            "hp":
                            round(db['EeveeHP'] * (db['EeveeLv'] / 15) + 800),
                            "dmg": round(db['EeveeDmg'] * 9.3),
                            "attacks": poke_attacks,
                            "speed": round(100 + db['EeveeLv'] * 0.38),
                            "armor": 1,
                            "type": db['Type']
                        }
                        edino = mob
                        edino_name = mob_name
                        fdino_effects = []
                        edino_effects = []

                        def plattack(attack):
                            nonlocal fdino
                            nonlocal edino
                            nonlocal fdino_effects
                            nonlocal edino_effects

                            fdino_damage_multiplier = 1

                            for i in fdino_effects:
                                if i[0] == "Wounded":  # ["Wounded",2]
                                    if i[1] > 0:
                                        fdino["hp"] -= round(edino["dmg"] *
                                                             0.5)
                                        print(
                                            f"Damage Over Time! ({round(edino['dmg'] * 0.5)} DMG)"
                                        )
                                        time.sleep(0.5)
                                        i[1] -= 1
                                    else:
                                        fdino_effects.remove(i)

                            if "Reduce Damage" in fdino_effects:
                                fdino_damage_multiplier = 0.5
                                fdino_effects.remove("Reduce Damage")

                            if "Stunned" in fdino_effects:
                                fdino_effects.remove("Stunned")

                            else:
                                if dino_info.battle_info(
                                        attack)["special"] == None:
                                    edino["hp"] -= fdino[
                                        "dmg"] * dino_info.battle_info(
                                            attack
                                        )["power"] * edino[
                                            "armor"] * fdino_damage_multiplier
                                    print(
                                        f"You used {attack}! ({round(fdino['dmg'] * dino_info.battle_info(attack)['power'] * edino['armor'] * fdino_damage_multiplier)} DMG)"
                                    )
                                    time.sleep(1)
                                elif dino_info.battle_info(
                                        attack)["special"] == "Stun":
                                    edino["hp"] -= fdino[
                                        "dmg"] * dino_info.battle_info(
                                            attack
                                        )["power"] * edino[
                                            "armor"] * fdino_damage_multiplier
                                    print(
                                        f"You used {attack}! ({round(fdino['dmg'] * dino_info.battle_info(attack)['power'] * edino['armor'] * fdino_damage_multiplier)} DMG)"
                                    )
                                    time.sleep(1)
                                    if random.randint(0, 1) == 1:
                                        edino_effects.append("Stunned")
                                        print("Enemy was Stunned!")
                                elif dino_info.battle_info(
                                        attack)["special"] == "Bypass Armor":
                                    edino["hp"] -= fdino[
                                        "dmg"] * dino_info.battle_info(attack)[
                                            "power"] * fdino_damage_multiplier
                                    print(
                                        f"You used {attack}! ({round(fdino['dmg'] * dino_info.battle_info(attack)['power'] * fdino_damage_multiplier)} DMG)"
                                    )
                                    time.sleep(1)
                                elif dino_info.battle_info(
                                        attack)["special"] == "Reduce Damage":
                                    edino["hp"] -= fdino[
                                        "dmg"] * dino_info.battle_info(
                                            attack
                                        )["power"] * edino[
                                            "armor"] * fdino_damage_multiplier
                                    print(
                                        f"You used {attack}! ({round(fdino['dmg'] * dino_info.battle_info(attack)['power'] * edino['armor'] * fdino_damage_multiplier)} DMG)"
                                    )
                                    edino_effects.append("Reduce Damage")
                                    time.sleep(0.5)
                                    print("You Reduced Enemy's Damage!")
                                    time.sleep(1)
                                elif dino_info.battle_info(
                                        attack)["special"] == "Slow":
                                    edino["hp"] -= fdino[
                                        "dmg"] * dino_info.battle_info(
                                            attack
                                        )["power"] * edino[
                                            "armor"] * fdino_damage_multiplier
                                    edino["speed"] = round(edino["speed"] *
                                                           0.75)
                                    print(
                                        f"You used {attack}! ({round(fdino['dmg'] * dino_info.battle_info(attack)['power'] * edino['armor'] * fdino_damage_multiplier)} DMG)"
                                    )
                                    time.sleep(1)
                                elif dino_info.battle_info(
                                        attack)["special"] == "Heal":
                                    print(
                                        f"You used {attack}! (+{fdino['dmg']} HP)"
                                    )
                                    fdino["hp"] += fdino["dmg"]

                                    time.sleep(1)
                                elif dino_info.battle_info(
                                        attack)["special"] == "Bleed":
                                    edino["hp"] -= fdino[
                                        "dmg"] * dino_info.battle_info(
                                            attack
                                        )["power"] * edino[
                                            "armor"] * fdino_damage_multiplier
                                    edino_effects.append(["Wounded", 2])
                                    print(
                                        f"You used {attack}! ({round(fdino['dmg'] * dino_info.battle_info(attack)['power'] * edino['armor'] * fdino_damage_multiplier)} DMG)"
                                    )
                                    time.sleep(0.5)
                                    print("Enemy was Wounded!")
                                    time.sleep(1)

                            fdino_damage_multiplier = 1  # Reset multiplier 4 dmg

                        def enattack(eattack):
                            nonlocal fdino
                            nonlocal edino
                            nonlocal fdino_effects
                            nonlocal edino_effects

                            edino_damage_multiplier = 1

                            for i in edino_effects:
                                if i[0] == "Wounded":  # ["Wounded",2]
                                    if i[1] > 0:
                                        edino["hp"] -= round(fdino["dmg"] *
                                                             0.5)
                                        print(
                                            f"Damage Over Time! ({round(fdino['dmg'] * 0.5)} DMG)"
                                        )
                                        time.sleep(0.5)
                                        i[1] -= 1
                                    else:
                                        edino_effects.remove(i)

                            if "Reduce Damage" in edino_effects:
                                edino_damage_multiplier = 0.5
                                edino_effects.remove("Reduce Damage")

                            if "Stunned" in edino_effects:
                                edino_effects.remove("Stunned")
                            else:
                                if dino_info.battle_info(
                                        eattack)["special"] == None:
                                    fdino["hp"] -= edino[
                                        "dmg"] * dino_info.battle_info(
                                            eattack
                                        )["power"] * fdino[
                                            "armor"] * edino_damage_multiplier
                                    print(
                                        f"Enemy used {eattack}! ({round(edino['dmg'] * dino_info.battle_info(eattack)['power'] * fdino['armor'] * edino_damage_multiplier)} DMG)"
                                    )
                                    time.sleep(1)
                                elif dino_info.battle_info(
                                        eattack)["special"] == "Stun":
                                    fdino["hp"] -= edino[
                                        "dmg"] * dino_info.battle_info(
                                            eattack
                                        )["power"] * fdino[
                                            "armor"] * edino_damage_multiplier
                                    print(
                                        f"Enemy used {eattack}! ({round(edino['dmg'] * dino_info.battle_info(eattack)['power'] * fdino['armor'] * edino_damage_multiplier)} DMG)"
                                    )
                                    time.sleep(1)
                                    if random.randint(0, 1) == 1:
                                        fdino_effects.append("Stunned")
                                        print("You were Stunned!")
                                elif dino_info.battle_info(
                                        eattack)["special"] == "Bypass Armor":
                                    fdino["hp"] -= edino[
                                        "dmg"] * dino_info.battle_info(
                                            eattack
                                        )["power"] * edino_damage_multiplier
                                    print(
                                        f"Enemy used {eattack}! ({round(edino['dmg'] * dino_info.battle_info(eattack)['power'] * edino_damage_multiplier)} DMG)"
                                    )
                                    time.sleep(1)
                                elif dino_info.battle_info(
                                        eattack)["special"] == "Reduce Damage":
                                    fdino["hp"] -= edino[
                                        "dmg"] * dino_info.battle_info(
                                            eattack
                                        )["power"] * fdino[
                                            "armor"] * edino_damage_multiplier
                                    print(
                                        f"Enemy used {eattack}! ({round(edino['dmg'] * dino_info.battle_info(eattack)['power'] * fdino['armor'] * edino_damage_multiplier)} DMG)"
                                    )
                                    fdino_effects.append("Reduce Damage")
                                    time.sleep(0.5)
                                    print("Enemy Reduced your Damage!")
                                    time.sleep(1)
                                elif dino_info.battle_info(
                                        eattack)["special"] == "Slow":
                                    fdino["hp"] -= edino[
                                        "dmg"] * dino_info.battle_info(
                                            eattack
                                        )["power"] * fdino[
                                            "armor"] * edino_damage_multiplier
                                    fdino["speed"] = round(fdino["speed"] *
                                                           0.75)
                                    print(
                                        f"Enemy used {attack}! ({round(edino['dmg'] * dino_info.battle_info(eattack)['power'] * fdino['armor'] * edino_damage_multiplier)} DMG)"
                                    )
                                    time.sleep(1)
                                elif dino_info.battle_info(
                                        eattack)["special"] == "Heal":
                                    print(
                                        f"Enemy used {eattack}! (+{edino['dmg']} HP)"
                                    )
                                    edino["hp"] += edino["dmg"]
                                    time.sleep(1)
                                elif dino_info.battle_info(
                                        eattack)["special"] == "Bleed":
                                    fdino["hp"] -= edino[
                                        "dmg"] * dino_info.battle_info(
                                            eattack
                                        )["power"] * fdino[
                                            "armor"] * edino_damage_multiplier
                                    fdino_effects.append(["Wounded", 2])
                                    print(
                                        f"Enemy used {eattack}! ({round(edino['dmg'] * dino_info.battle_info(eattack)['power'] * fdino['armor'] * edino_damage_multiplier)} DMG)"
                                    )
                                    time.sleep(0.5)
                                    print("You were Wounded!")
                                    time.sleep(1)

                            edino_damage_multiplier = 1  # reset again

                        while True:
                            clear()
                            print(
                                f"[{Blue}{username}{reset}] - {fdino_name}        [{Red}Enemy{reset}] - {edino_name}"
                            )
                            print(f"{Red}Health: {fdino['hp']}",
                                  " " * (len(username) + len(fdino_name)),
                                  f"{Red}Health: {edino['hp']}{reset}")
                            print(
                                f"{bright_green}Speed: {fdino['speed']}",
                                " " * (len(username) + len(fdino_name) + 1),
                                f"{bright_green}Speed: {edino['speed']}{reset}\n"
                            )
                            for idx, val in enumerate(fdino["attacks"]):
                                if val not in used_attacks:
                                    print(f"{idx+1}: ({Red}{val}{reset})")
                                else:
                                    if used_attacks[val][
                                            "turns"] >= dino_info.battle_info(
                                                val
                                            )["cooldown"]:  # turns = turns passed
                                        del used_attacks[val]
                                        print(f"{idx+1}: ({Red}{val}{reset})")
                                    else:
                                        used_attacks[val]["turns"] += 1

                            while True:
                                try:
                                    attack = input(
                                        f"\nChoose an {Red}Attack{reset}:\n")
                                    attack = fdino["attacks"][int(attack) - 1]
                                    if attack not in used_attacks:
                                        break
                                except:
                                    pass
                            if dino_info.battle_info(attack)["cooldown"] != 0:
                                used_attacks[attack] = {"turns": 0}

                            to_remove = []
                            for i in en_used_attacks:
                                if en_used_attacks[i][
                                        "turns"] >= dino_info.battle_info(
                                            i)["cooldown"]:
                                    to_remove.append(i)
                                else:
                                    en_used_attacks[i]["turns"] += 1
                            for i in to_remove:
                                del en_used_attacks[i]
                            to_remove = []

                            while True:
                                eattack = random.choice(edino["attacks"])
                                if eattack not in en_used_attacks:
                                    en_used_attacks[eattack] = {"turns": 0}
                                    break

                            if fdino["speed"] >= edino["speed"]:
                                plattack(attack)
                                if edino["hp"] <= 0:
                                    win()
                                    break
                                elif fdino["hp"] <= 0:
                                    lose()
                                    break
                                enattack(eattack)
                                if edino["hp"] <= 0:
                                    win()
                                    break
                                elif fdino["hp"] <= 0:
                                    lose()
                                    break
                            else:
                                enattack(eattack)
                                if edino["hp"] <= 0:
                                    win()
                                    break
                                elif fdino["hp"] <= 0:
                                    lose()
                                    break
                                plattack(attack)
                                if edino["hp"] <= 0:
                                    win()
                                    break
                                elif fdino["hp"] <= 0:
                                    lose()
                                    break

                            edino["hp"] = round(edino["hp"])
                            fdino["hp"] = round(fdino["hp"])
                            time.sleep(0.9)

                    clear()
                    if db['EeveeLv'] <= 120:
                        mob = pokejwo['stats']
                        poke_battle(mob, pokejwo['name'])
                    else:
                        print(
                            "You are not allowed to battle with this Pokemon!")
                        time.sleep(2)
                clear()
            elif input1=="13":
              Account()
              Friends()


clear()
if not 'Loaded' in db.keys():
  if 1 == 1:
    db['Loaded'] = 0
    db['NoShiny'] = 'Eevee'
    db['Move1'] = ''
    db['Move2'] = ''
    db['NextXP'] = 0
    db['Trophys'] = 0
    db['EeveeLv'] = 5
    db['EeveeHP'] = 10
    db['EeveeDmg'] = 2
    db['Money'] = 100
    db['Level'] = 0
    db['Upg'] = [0, 0]
    db['Prog'] = 0
    db['Quests'] = 1
    db['Completion'] = False
    db['PolarEgg'] = False
    db['FIGHT'] = False
    db['Thorns'] = ''
    db['Salve'] = ''
    db['Double'] = False
    db['Keys'] = True
    db['PokeBalls'] = 10
    db['GreatBalls'] = 0
    db['UltraBalls'] = 0
    db['MasterBalls'] = 0
    db['PokemonEvolution'] = 0
    db['Potions'] = 0
    db['SuperPotions'] = 0
    db['HyperPotions'] = 0
    db['MasterPotions'] = 0
    db['Encounters'] = 0
    db['Items'] = []
    db['PolarEgg'] = False
    db['PokemonName'] = 'Eevee'
    db['Type'] = 1
    db['Type2'] = 19
    db['AreaName'] = 'Vine Vally'
    db['AreaName2'] = 'Thorn Palace'
    db['Area'] = ['Vine Vally']
if not 'Eevee Land' in db['Area']:
    db['Area'].append('Eevee Land')
if not 'Campsite' in db['Area']:
    db['Area'].append('Campsite')
if not 'PokeTeam' in db.keys():
  db['PokeTeam'] = [['Empty', 0, 0, 'Empty', 'Empty', 'Empty', 'Empty', 'Empty'], ['Empty', 0, 0, 'Empty', 'Empty', 'Empty', 'Empty', 'Empty'], ['Empty', 0, 0, 'Empty', 'Empty', 'Empty', 'Empty', 'Empty'], ['Empty', 0, 0, 'Empty', 'Empty', 'Empty', 'Empty', 'Empty'], ['Empty', 0, 0, 'Empty', 'Empty', 'Empty', 'Empty', 'Empty']]
if not 'PP1' in db.keys():

  
  db['MOVE1'] = pokemon.pokemonn[db['NoShiny']][2]
  db['MOVE2'] = pokemon.pokemonn[db['NoShiny']][3]
  db['MOVE3'] = ''
  db['MOVE4'] = ''
  db['PP1'] = battlemoves.moves[battlemoves.movesid[db['MOVE1']]][6]
  db['PP2'] = battlemoves.moves[battlemoves.movesid[db['MOVE1']]][6]
  db['PP3'] = 10
  db['PP4'] = 10
if not 'LOL' in db.keys():
    db['LOL'] = ''
    db['AreaName'] = 'Vine Vally'
    db['AreaName2'] = 'Thorn Palace'
    db['Area'] = ['Vine Vally', 'Campsite']
    db['Type'] = 1
    db['Type2'] = 19
    x = ''
    while x != '1' and x != '2' and x != '3' and x != '4':
            clear()
            print('List of starter pokemon:')
            print('(1) Eevee (Normal)')
            print('(2) Caikit (Grass)')
            print('(3) Chocleon (Fire)')
            print('(4) Soadapup (Water)')
            x = input('Select a starter pokemon\n')
            if x == '1':
                    pokemonewhomsthavebeengevenbyyourfatherforyourpokemonjourneytodefeatthe19ultimates = 'Eevee'
                    db['PokemonName'] = 'Eevee'
                    db['NoShiny'] = 'Eevee'
            elif x == '2':
                    pokemonewhomsthavebeengevenbyyourfatherforyourpokemonjourneytodefeatthe19ultimates = 'Caikit'
                    db['PokemonName'] = 'Caikit'
                    db['NoShiny'] = 'Caikit'
            elif x == '3':
                    pokemonewhomsthavebeengevenbyyourfatherforyourpokemonjourneytodefeatthe19ultimates = 'Chocleon'
                    db['PokemonName'] = 'Chocleon'
                    db['NoShiny'] = 'Chocleon'
            elif x == '4':
                    pokemonewhomsthavebeengevenbyyourfatherforyourpokemonjourneytodefeatthe19ultimates = 'Soadapup'
                    db['PokemonName'] = 'Soadapup'
                    db['NoShiny'] = 'Soadapup'
            else:
                    pass
    clear()
    print(
        f'Welcome to Pokemon Ultimates! There are 19 ultimate pokemon that have taken over the Ultrae Region, and it is your goal to stop them! You are given a {pokemonewhomsthavebeengevenbyyourfatherforyourpokemonjourneytodefeatthe19ultimates} by your father to train and fight alongside to take down the ultimates! Good Luck! This game automatically saves your progress, so you can come back to it anytime! To see how to play the game, just use the tutorial option! '
    )
    print('')
    print(
        f"This program was created by S1lveredPrism, {Fore.LIGHTBLUE_EX}HyperAlternative, IcemasterEric,  {Fore.BLUE}IMeanBusiness, {Fore.RED}C{Fore.LIGHTYELLOW_EX}o{Style.DIM + Fore.LIGHTGREEN_EX}lor{Style.BRIGHT + Fore.CYAN}ed{Style.DIM + Fore.BLUE}Hue,{Fore.RESET + Style.RESET_ALL} and {Style.DIM + Fore.BLUE}ColinKirsch! "
    )
    print(Fore.RESET + Style.RESET_ALL + Back.RESET)
    print(
        f'Additional Mentions go to: {Style.BRIGHT + Fore.LIGHTYELLOW_EX}DotAccount!{Fore.RESET + Style.RESET_ALL}'
    )
    affirm()
    clear()
    while 1 == 1:
      Game()
else:
    print(
        f"This program was created by S1lveredPrism, {Fore.LIGHTBLUE_EX}HyperAlternative, IcemasterEric, {Fore.BLUE}IMeanBusiness,  {Fore.RED}C{Fore.LIGHTYELLOW_EX}o{Style.DIM + Fore.LIGHTGREEN_EX}lor{Style.BRIGHT + Fore.CYAN}ed{Style.DIM + Fore.BLUE}Hue,{Fore.RESET + Style.RESET_ALL} {Style.DIM + Fore.BLUE}ColinKirsch{Fore.RESET + Style.RESET_ALL}, and {Fore.BLUE}IcemasterEric{Fore.RESET}! "
    )
    print(Fore.RESET + Style.RESET_ALL + Back.RESET)
    print(
        f'Additional Mentions go to: {Style.BRIGHT + Fore.LIGHTYELLOW_EX}DotAccount!{Fore.RESET + Style.RESET_ALL}'
    )
    affirm()
    db['Money'] = round(db['Money'])
    clear()
    while 1 == 1:
      Game()
