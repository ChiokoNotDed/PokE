import Evolutions
import time
import random
from replit import db
from functions import pause, affirm, clear
import pokemon
import battlemoves
from colorama import *
from pokemon import ingredients, berries

message = ''

def switch():
  g = 0
  hello = []
  for i in db['PokeTeam']:
    
    if i[0] != 'Empty' and i [2] > 0:
      print(f"({g}) Level {i[1]} {i[0]} | {i[2]} HP")
      yu = str(g)
      hello.append(yu)
      
    g += 1
  v = ''
  if len(hello) == 0:
    return False
  while v not in hello:
    
    v = input('Who do you want to switch to? ')

  try:
    v = int(v)
    if db['PokeTeam'][v][0] != 'Empty' and db['PokeTeam'][v][2] > 1:
      Bruh = db['PokeTeam'][v]
      db['PokeTeam'][v][0] = db['PokemonName']
      db['PokeTeam'][v][1] = db['EeveeLv']
      db['PokeTeam'][v][2] = db['EeveeHP']
      db['PokeTeam'][v][3] = db['PP1']
      db['PokeTeam'][v][4] = db['PP2']
      db['PokeTeam'][v][5] = battlemoves.moves[battlemoves.movesid[db['MOVE1']]][6]
      db['PokeTeam'][v][6] = battlemoves.moves[battlemoves.movesid[db['MOVE2']]][6]
      db['PokeTeam'][v][7]= db['Encounters']
      db['EeveeHP'] = Bruh[2]
      db['PokemonName'] = Bruh[0]
      db['EeveeLv'] = Bruh[1]
      db['Encounters'] = Bruh[7]
      db['PP1'] = Bruh[3]
      db['PP2'] = Bruh[4]
      if 'Shiny-' in db['PokemonName']:
                          u = 0
                          b = ''
                          for i in db['PokemonName']:
                           
                            u += 1 
                            if u >6:
                              b += i
                          db['NoShiny'] = b
      else:
                          db['NoShiny'] = db['PokemonName']
      db['Type'] = pokemon.pokemonn[db['NoShiny']][0]
      db['Type2'] = pokemon.pokemonn[db['NoShiny']][1]
      db['MOVE1'] = pokemon.pokemonn[db['NoShiny']][2]
      db['MOVE2'] = pokemon.pokemonn[db['NoShiny']][3]
      MYNAME = db['PokemonName']
      global mdmg, mdef
      if MYNAME in [
            'Noivern', 'Umbreon', 'Jolteon', 'Espeon', 'Sylveon', 'Glaceon',
            'Flareon', 'Vaporeon', 'Leafeon', 'Gabite', 'Quagsire',
            'Charmeleon', 'Wartortle', 'Pikachu', 'Clefairy', 'Furret',
            'Weezing', 'Slowbro', 'Dewgong', 'Vibrava', 'Ninetails', 'Gyrados'
    ]:
        mdmg = 5
        mdef = 5
      elif MYNAME in [
            'Blastoise',  'Charizard', 'Zygarde', 'Dragonite',
            'Raichu', 'Garchomp'
    ]:
          mdmg = 10
          mdef = 10
      elif MYNAME in ['Lunala', 'Solgaleo', 'Zekrom', 'Arceus']:
        mdmg = 13
        mdef = 13
      clear()
  except:
    return ''
  
    
def crit(damage):
    global message
    crit = random.randint(1, 10000)
    damage1 = damage
    message = ''
    if crit <= 625:
        damage1 = damage1 * 2
        message = 'Critical Hit! '
        return damage1
    else:
        message = ''
        return damage1


def attack(movetype, type1, type2, damage):
    if movetype == 1:  #Normal
        weaktypes = []
        strongtypes = [11, 14]
        if type1 in weaktypes:
            damage = damage * 2
        if type2 in weaktypes:
            damage = damage * 2
        if type1 in strongtypes:
            damage = round(damage / 2)
        if type2 in strongtypes:
            damage = round(damage / 2)
    elif movetype == 2:  #Grass
        weaktypes = [3, 6, 14]
        strongtypes = [4, 5, 10, 13, 17]
        if type1 in weaktypes:
            damage = damage * 2
        if type2 in weaktypes:
            damage = damage * 2
        if type1 in strongtypes:
            damage = round(damage / 2)
        if type2 in strongtypes:
            damage = round(damage / 2)
    elif movetype == 3:  #Water
        weaktypes = [4, 6, 14]
        strongtypes = [2, 9]
        if type1 in weaktypes:
            damage = damage * 2
        if type2 in weaktypes:
            damage = damage * 2
        if type1 in strongtypes:
            damage = round(damage / 2)
        if type2 in strongtypes:
            damage = round(damage / 2)
    elif movetype == 4:  #Fire
        weaktypes = [2, 10, 13, 17]
        strongtypes = [3, 6, 14]
        if type1 in weaktypes:
            damage = damage * 2
        if type2 in weaktypes:
            damage = damage * 2
        if type1 in strongtypes:
            damage = round(damage / 2)
        if type2 in strongtypes:
            damage = round(damage / 2)
    elif movetype == 5:  #Flight
        weaktypes = [2, 11, 13]
        strongtypes = [9, 10, 14, 17]
        if type1 in weaktypes:
            damage = damage * 2
        if type2 in weaktypes:
            damage = damage * 2
        if type1 in strongtypes:
            damage = round(damage / 2)
        if type2 in strongtypes:
            damage = round(damage / 2)
    elif movetype == 6:  #Ground
        weaktypes = [4, 9, 10]
        strongtypes = [2, 3]
        if type1 in weaktypes:
            damage = damage * 2
        if type2 in weaktypes:
            damage = damage * 2
        if type1 in strongtypes:
            damage = round(damage / 2)
        if type2 in strongtypes:
            damage = round(damage / 2)
    elif movetype == 7:  #Dark
        weaktypes = [12, 15]
        strongtypes = [11, 13, 18]
        if type1 in weaktypes:
            damage = damage * 2
        if type2 in weaktypes:
            damage = damage * 2
        if type1 in strongtypes:
            damage = round(damage / 2)
        if type2 in strongtypes:
            damage = round(damage / 2)
    elif movetype == 8:  #Poison
        weaktypes = [2, 18]
        strongtypes = [6, 8, 14, 15]
        if type1 in weaktypes:
            damage = damage * 2
        if type2 in weaktypes:
            damage = damage * 2
        if type1 in strongtypes:
            damage = round(damage / 2)
        if type2 in strongtypes:
            damage = round(damage / 2)
    elif movetype == 9:  #Electric
        weaktypes = [3, 5]
        strongtypes = [6]
        if type1 in weaktypes:
            damage = damage * 2
        if type2 in weaktypes:
            damage = damage * 2
        if type1 in strongtypes:
            damage = round(damage / 2)
        if type2 in strongtypes:
            damage = round(damage / 2)
    elif movetype == 10:  #Ice
        weaktypes = [2, 5, 6, 16]
        strongtypes = [3, 4, 10, 17]
        if type1 in weaktypes:
            damage = damage * 2
        if type2 in weaktypes:
            damage = damage * 2
        if type1 in strongtypes:
            damage = round(damage / 2)
        if type2 in strongtypes:
            damage = round(damage / 2)
    elif movetype == 11:  #Fighting
        weaktypes = [7, 10, 14, 17]
        strongtypes = [5, 12, 18]
        if type1 in weaktypes:
            damage = damage * 2
        if type2 in weaktypes:
            damage = damage * 2
        if type1 in strongtypes:
            damage = round(damage / 2)
        if type2 in strongtypes:
            damage = round(damage / 2)
    elif movetype == 12:  #Psychic
        weaktypes = [4, 8]
        strongtypes = [7, 13, 15]
        if type1 in weaktypes:
            damage = damage * 2
        if type2 in weaktypes:
            damage = damage * 2
        if type1 in strongtypes:
            damage = round(damage / 2)
        if type2 in strongtypes:
            damage = round(damage / 2)
    elif movetype == 13:  #Bug
        weaktypes = [2, 7, 12]
        strongtypes = [4, 5, 14]
        if type1 in weaktypes:
            damage = damage * 2
        if type2 in weaktypes:
            damage = damage * 2
        if type1 in strongtypes:
            damage = round(damage / 2)
        if type2 in strongtypes:
            damage = round(damage / 2)
    elif movetype == 14:  #Rock
        weaktypes = [4, 5, 10, 13]
        strongtypes = [6, 11, 17]
        if type1 in weaktypes:
            damage = damage * 2
        if type2 in weaktypes:
            damage = damage * 2
        if type1 in strongtypes:
            damage = round(damage / 2)
        if type2 in strongtypes:
            damage = round(damage / 2)
    elif movetype == 15:  #Ghost
        weaktypes = [12, 15]
        strongtypes = [1, 7]
        if type1 in weaktypes:
            damage = damage * 2
        if type2 in weaktypes:
            damage = damage * 2
        if type1 in strongtypes:
            damage = round(damage / 2)
        if type2 in strongtypes:
            damage = round(damage / 2)
    elif movetype == 16:  #Dragon
        weaktypes = [16]
        strongtypes = [17, 18]
        if type1 in weaktypes:
            damage = damage * 2
        if type2 in weaktypes:
            damage = damage * 2
        if type1 in strongtypes:
            damage = round(damage / 2)
        if type2 in strongtypes:
            damage = round(damage / 2)
    elif movetype == 17:  #Steel
        weaktypes = [10, 14, 18]
        strongtypes = [3, 9]
        if type1 in weaktypes:
            damage = damage * 2
        if type2 in weaktypes:
            damage = damage * 2
        if type1 in strongtypes:
            damage = round(damage / 2)
        if type2 in strongtypes:
            damage = round(damage / 2)
    elif movetype == 18:  #Fairy
        weaktypes = [7, 11, 16]
        strongtypes = [8, 17]
        if type1 in weaktypes:
            damage = damage * 2
        if type2 in weaktypes:
            damage = damage * 2
        if type1 in strongtypes:
            damage = round(damage / 2)
        if type2 in strongtypes:
            damage = round(damage / 2)
    return damage


def executemove(move, HPa, level, us, them, who, mydmg, mydef, urdmg, urdef):
    global HP, dmg, sdef, mdmg, mdef, mpoison, mburn, mstun, mfreeze, mconfuse, epoison, eburn, estun, efreeze, econfuse, type1, type2, etype1, etype2, message
    data = battlemoves.moves[move]
    accuracy = data[0]
    ac = random.randint(1, 100)

    if accuracy < ac:
        print(f"{us}'s {move} missed! ")
        affirm()
        clear()
    else:
        print(f'{us} used {move}! ')
        pause(1)
        zp = random.randint(1,2)
        if zp == 1:
 
          damage = round(((2 * level)/5 * data[1]) *((mdmg/30)/(mdef/30))/50) + random.randint(1,3)
        else:
          damage = round(((2 * level)/5 * data[1]) *((mdmg/30)/(mdef/30))/50) + random.randint(1, 3)
        if move == 'Double Kick':
            damage = damage * 2
            print('Double Kick hit twice! ')
        elif move == 'Comet Punch':
            f = random.randint(2, 5)
            damage = damage * f
            print(f"Comet Punch hit {f} times! ")

        elif move == 'Hone Claws':
            if who == False:
                dmg += 5
                print(
                    f"{us} used Hone Claws! {us}'s attack sharply increased! ")
            elif who == True:
                mdmg += 5
                print(
                    f"{us} used Hone Claws! {us}'s attack sharply increased! ")
        elif move == "Developer's Fury":
          pass
        if who == True:

            if damage > 0:
          
                if move == 'Fissure':
                    damage = HP

                damage = attack((battlemoves.moves[move][5]), etype1, etype2,
                                damage)
                damage = crit(damage)
                if damage > HP:
                  damage = HP
                if damage < 1:
                    damage = 1
                HP = HP - damage
                print(
                    f"{message}{us} did {damage} damage! Foe {them} has {HP} HP left! "
                )
        elif who == False:

            if damage > 0:
            
                damage = attack((battlemoves.moves[move][5]), type1, type2,
                                damage)
                damage = crit(damage)
                if move == 'Fissure':
                    damage = db['EeveeHP']
                if damage < 1:
                    damage = 1
                if damage > db['EeveeHP']:
                  damage = db['EeveeHP']
                db['EeveeHP'] = db['EeveeHP'] - damage
                print(
                    f"{message}{us} did {damage} damage! Foe {them} has {db['EeveeHP']} HP left! "
                )

        if move == 'Absorb' or move == 'Mega Drain' or move == 'Leech Life' or move == 'Draining Kiss':
            print(f'{us} regained {round(damage/2)} HP! ')
            if who == False:
                HP += round(damage / 2)
            elif who == True:
                db['EeveeHP'] += round(damage / 2)
        elif move == 'Blizzard' or move == 'Aurora Beam' or move == 'Ice Punch' or move == 'Ice Beam':
            t = random.randint(1, 5)
            if t == 1:
                if who == True:
                    efreeze = True
                elif who == False:
                    mfreeze = True
                print(f'{them} was frozen!')
        elif move == 'Ember' or move == 'Fire Spin' or move == 'Flamethrower' or move == 'Fire Blast':
            t = random.randint(1, 5)
            if t == 1:
                if who == True:
                    eburn = True
                elif who == False:
                    mburn = True
                print(f'{them} was burned! ')
        elif move == 'Body Slam' or move == 'Lick' or move == 'Thunder Shock' or move == 'Thunder Punch' or move == 'Nuzzle' or move == 'Prismatic Lazer':
            t = random.randint(1, 5)
            if t == 1:
                if who == True:
                    estun = True
                elif who == False:
                    mstun = True
                print(f'{them} was paralyzed! ')
        elif move == 'Poison Fang':
            t = random.randint(1, 5)
            if t == 1:
                if who == True:
                    epoison = True
                elif who == False:
                    mpoison = True
                print(f'{them} was poisoned! ')
        elif move == 'Poison Powder':
            if who == True:
                epoison = True
            elif who == False:
                mpoison = True
            print(f'{them} was poisoned! ')

        elif move == 'Confuse Ray':
            if who == True:
                econfuse = True
            elif who == False:
                mconfuse = True
            print(f"{them} was confused! ")
        elif move == 'Confusion':
            t = random.randint(1, 5)
            if t == 1:
                if who == True:
                    econfuse = True
                elif who == False:
                    mconfuse = True
                print(f"{them} was confused! ")
        elif move == 'Barrier':
            if who == True:

                mdef += 5
            elif who == False:
                sdef += 5
            print(f"{us}'s defense increased! ")

        affirm()
        clear()


trainers = ['ColoredHue', 'Steven', 'Eevee Kid', 'Pikachu Kid', 'Gary', 'Ash Ketchum', 'Mecha Micah', 'Misty', 'Brock', 'Jessie', 'James'] 
'''
Normal: 1
Grass: 2
Water: 3
Fire: 4
Flight: 5
Ground: 6
Dark: 7
Poison: 8
Electric: 9
Ice: 10
Fighting: 11
Psychic: 12
Bug: 13
Rock: 14
Ghost: 15
Dragon: 16
Steel: 17
Fairy: 18
'''
level = ''
HP = ''
x = ''
dmg = 1
sdef = 1
mdmg = ''
mdef = ''
mpoison = False
mburn = False
mstun = False
mfreeze = False
mconfuse = False
epoison = False
eburn = False
estun = False
efreeze = False
econfuse = False
type1 = ''
type2 = ''
etype1 = ''
etype2 = ''
Boss = ''
Training = ''
BossNume = ''
Battle = ''
Trophy = ''
move = True
emove = True
Bro = False

def trophycounter():
    global Boss, DisablePB, Trophy
    MyShiny = False
    Boss = False
    DisablePB = True
    Trophy = True
    Pencounter(MyShiny, [], '')


def braining():
    global DisablePB, Training, Boss, Trophy
    Trophy = False
    DisablePB = True
    MyShiny = False
    Training = True
    Boss = False
    Pencounter(MyShiny, [], '')


def BPencounter():
    global Boss, BossNum, DisablePB
    MyShiny = False

    Boss = True
    DisablePB = True
    BossNum = 1
    Pencounter(MyShiny, [], '')


def BPencounter2():
    global Boss, BossNum
    MyShiny = False
    Boss = True
    BossNum = 2

    Pencounter(MyShiny, [], '')


def BPencounter3():
    global Boss, BossNum
    MyShiny = False
    Boss = True
    BossNum = 3
    Pencounter(MyShiny, [], '')


def BPencounter4():
    global Boss, BossNum
    Boss = True
    MyShiny = False
    BossNum = 4
    Pencounter(MyShiny, [], '')


def BPencounter5():
    global Boss, BossNum
    Boss = True
    MyShiny = False
    BossNum = 5
    Pencounter(MyShiny, [], '')


def BPencounter6():
    global Boss, BossNum
    Boss = True
    BossNum = 6
    MyShiny = False
    Pencounter(MyShiny, [], '')


def Pencounter2(MyShiny):
    global Boss, Training, Trophy, DisablePB, Bro
    Trophy = False
    DisablePB = False
    Training = False
    Boss = False
    Bro = False
    Pencounter(MyShiny, [], '')
def Brop(Team, Trainer):
  global Bro
  
  Bro = True
  MyShiny = False
  Pencounter(MyShiny, Team, Trainer)
def DamageCalculation():
    global mdmg, mdef
    MYNAME = db['NoShiny']
  
    if MYNAME in [
            'Noivern', 'Umbreon', 'Jolteon', 'Espeon', 'Sylveon', 'Glaceon',
            'Flareon', 'Vaporeon', 'Leafeon', 'Gabite', 'Quagsire',
            'Charmeleon', 'Wartortle', 'Pikachu', 'Clefairy', 'Furret',
            'Weezing', 'Slowbro', 'Dewgong', 'Vibrava', 'Ninetails', 'Gyrados', 'Cocoaleon', 'Softipop', 'Caikatat'
    ]:
        mdmg = 5
        mdef = 5
    elif MYNAME in [
            'Blastoise',  'Charizard', 'Zygarde', 'Dragonite',
            'Raichu', 'Garchomp', 'Choclameleon', 'Poplipup'
    ]:
        mdmg = 10
        mdef = 10
    elif MYNAME in ['Lunala', 'Solgaleo', 'Zekrom', 'Arceus', 'Mega-Leafeon']:
      mdmg = 13
      mdef = 13
    elif MYNAME in ['Rainbow-Leafeon GX']:
      mdmg = 18
      mdef = 18

def Pencounter(Shiny, TTeam, CTR):
    clear()

    global level, HP, x, dmg, sdef, mdmg, mdef, mpoison, mburn, mstun, mfreeze, mconfuse, epoison, eburn, estun, efreeze, econfuse, type1, type2, etype1, etype2, Battle, trainers, Trophy, move, emove, DisablePB, Bro, Trainer
    PokemonTeam = []
  
    Trainer = ''
    type1 = db['Type']
    type2 = db['Type2']
    mdmg = 1
    mdef = 1
    MYNAME = db['NoShiny']
  
    if MYNAME in [
            'Noivern', 'Umbreon', 'Jolteon', 'Espeon', 'Sylveon', 'Glaceon',
            'Flareon', 'Vaporeon', 'Leafeon', 'Gabite', 'Quagsire',
            'Charmeleon', 'Wartortle', 'Pikachu', 'Clefairy', 'Furret',
            'Weezing', 'Slowbro', 'Dewgong', 'Vibrava', 'Ninetails', 'Gyrados'
    ]:
        mdmg = 5
        mdef = 5
    elif MYNAME in [
            'Blastoise',  'Charizard', 'Zygarde', 'Dragonite',
            'Raichu', 'Garchomp'
    ]:
        mdmg = 10
        mdef = 10
    elif MYNAME in ['Lunala', 'Solgaleo', 'Zekrom', 'Arceus', 'Mega-Leafeon', 'Rainbow-Leafeon GX']:
      mdmg = 13
      mdef = 13
    Polar = 0

    Battle = False
    x = ''
    if Boss == False and Bro == False:
        uo = random.randint(1, 12)
        if uo == 13:
            Battle = True
          
        if db['AreaName'] == 'Eevee Land':
            x = random.choice([
                'Umbreon', 'Eevee', 'Sylveon', 'Espeon', 'Leafeon', 'Jolteon',
                'Vaporeon', "Flareon", 'Glaceon'
            ])
        elif db['AreaName'] == 'Vine Vally':
            x = random.choice([
                'Dragonite', 'Noivern', 'Raichu', 'Slowbro', 'Weezing',
                'Furret', 'Leafeon', 'Gyarados', 'Jigglypuff', 'Sandslash',
                'Charmeleon', 'Ratatta', 'Bulbasaur', 'Squirtle', 'Charmander',
                'Pidgey', 'Sandshrew', 'Sandile', 'Skorupi', 'Pikachu',
                'Spheal', 'Machop', 'Abra', 'Caterpie', 'Rolycoly', 'Litwick',
                'Dreepy', 'Aron', 'Clefairy', 'Magnemite', "Farfetch'd",
                'Eevee', 'Charizard'
            ])
            yt = random.randint(1, 2000)
            if yt == 1:
                x = 'Zekrom'
            if yt == 2:
                x = 'Solgaleo'
            if yt == 3:
                x = 'Lunala'
        elif db['AreaName'] == 'Big Blue':
            x = random.choice([
                'Blastoise', 'Piethon', 'Porygon2', 'Gloom', 'Kricketune', 'Arbok',
                'Dewgong', 'Vaporeon', 'Kadabra', 'Golduck', 'Kingler',
                'Wartortle', 'Oddish', 'Voltorb', 'Lickitung', 'Poliwag',
                'Bellsprout', 'Tentacool', 'Seel', 'Horsea', 'Rhyhorn',
                'Magicarp', 'Dratini', 'Gastly', 'Doduo', 'Psyduck', 'Onix',
                'Grimer', 'Shellder', 'Azurill', "Wooper", 'Garchomp',
                'Charizard'
            ])
            yt = random.randint(1, 2000)
            if yt == 1:
                x = 'Zekrom'
            if yt == 2:
                x = 'Solgaleo'
            if yt == 3:
                x = 'Lunala'
        elif db['AreaName'] == 'Vulpix Volcano':
            x = random.choice([
                'Blastoise', 'Piethon', 'Porygon2', 'Gloom', 'Kricketune', 'Arbok',
                'Dewgong', 'Vaporeon', 'Kadabra', 'Golduck', 'Kingler',
                'Wartortle', 'Oddish', 'Voltorb', 'Lickitung', 'Poliwag',
                'Bellsprout', 'Tentacool', 'Seel', 'Horsea', 'Rhyhorn',
                'Magicarp', 'Dratini', 'Gastly', 'Doduo', 'Psyduck', 'Onix',
                'Grimer', 'Shellder', 'Azurill', "Wooper", 'Garchomp',
                'Charizard'
            ])
            yt = random.randint(1, 2000)
            if yt == 1:
                x = 'Zekrom'
            if yt == 2:
                x = 'Solgaleo'
            if yt == 3:
                x = 'Lunala'
        level = random.randint((db['EeveeLv'] - 1), (db['EeveeLv'] + 1))
        t = x
        
        if Polar == 1:
            x = 'Polarized-' + x
        
            
        if Trophy == True:
            level = round(level * 3)
        if Training == True:
            level = round(level * 2)
        HP = level * 3
        if Shiny == True:
          x = 'Shiny-' + x
          HP = round(HP * 1.5)
        
        if Battle == True:
            Trainer = random.choice(trainers)
            import godtrainers
            PokemonTeam1 = godtrainers.TheBestCoders[Trainer]
            PokemonTeam = PokemonTeam1
            x = PokemonTeam[0]
            PokemonTeam.remove(x)
            t = x
            print(
                f'You encounter trainer {Trainer}!')
            affirm()
            clear()
            print(f"{Trainer} sent out {x}! ")
        else:
            PokemonTeam = [x]
            PokemonTeam.remove(x)
            print(f'You encountered a wild level {level} {x}!')  

        affirm()
        clear()

    elif Boss == True:
        Trophy = False
        DisablePB == True
        if BossNum == 1:
            x = 'Serperior'
            level = 25
        elif BossNum == 2:
            x = 'Leafeon'
            level = 50
        elif BossNum == 5:
            x = 'Polywrath'
            level = 100
        elif BossNum == 6:
            x = 'Ultra-Kyogre'
            level = 250
        elif BossNum == 4:
            x = 'Ninetails'
            level = 300
        elif BossNum == 3:
            x = 'Vaporeon'
            level = 150
        HP = level * 3
        t = x

    elif Bro == True:
      T = TTeam.split(',')
      level = random.randint((db['EeveeLv'] - 1), (db['EeveeLv'] + 1))
      x = T[0]
      PokemonTeam = T
      PokemonTeam.remove(x)
      t = x
      Trainer = CTR
      HP = level * 3
      print(f'{Trainer} sends out {t}! ')
      
      
    if db['Salve'] == 4:
        u = random.randint(1, 3)
        if u == 2:
            x = 'Princess Flareon'
            level = 500
            DisablePB = True
            t = x
    etype1 = pokemon.pokemonn[t][0]

    etype2 = pokemon.pokemonn[t][1]

    dmg = 0
    sdef = 0
    # if db['PokemonName'] == (polarized):
    # Polar = random.randint(1,3)
    global bruh
    bruh = 7
    while bruh == 7:
        StopMe()
        if move == True:
            print(f'''
  {db['PokemonName']}: {db['EeveeHP']}
  {x}: {HP}
  
  (1) {battlemoves.movesid[pokemon.pokemonn[db['NoShiny']][2]]} | PP: {db['PP1']}/{battlemoves.moves[battlemoves.movesid[db['MOVE1']]][6]}
  
  (2) {battlemoves.movesid[pokemon.pokemonn[db['NoShiny']][3]]} | PP: {db['PP2']}/{battlemoves.moves[battlemoves.movesid[db['MOVE2']]][6]}
  
  (3) Open Backpack

  (4) Switch Pokemon
  
  
        ''')
            key = input()
            if key == '1' and db['PP1'] > 0:
                db['PP1'] -= 1
                clear()
                executemove(
                    battlemoves.movesid[pokemon.pokemonn[db['NoShiny']][2]],
                    HP, db['EeveeLv'], db['PokemonName'], x, True, mdmg, mdef,
                    dmg, sdef)
            elif key == '2' and db['PP2'] > 0:
                db['PP2'] -= 1
                clear()
                executemove(
                    battlemoves.movesid[pokemon.pokemonn[db['NoShiny']][3]],
                    HP, db['EeveeLv'], db['PokemonName'], x, True, mdmg, mdef,
                    dmg, sdef)
            elif key == '4':
              kl = 0
              for i in [0,1,2,3,4]:
                if db['PokeTeam'][i][2] > 1:
                  kl += 1
              if kl > 0:
                switch()
            elif key == '3':
                clear()
                print('Type whatever is in the Parenthesis to chose item')
                print('')
                if db['PokeBalls'] > 0:
                    print(f"(PokeBalls) - {db['PokeBalls']}")
                if db['GreatBalls'] > 0:
                    print(f"(GreatBalls) - {db['GreatBalls']}")
                if db['UltraBalls'] > 0:
                    print(f"(UltraBalls) - {db['UltraBalls']}")
                if db['MasterBalls'] > 0:
                    print(f"(MasterBalls) - {db['MasterBalls']}")
                if db['Potions'] > 0:
                    print(f"(Potion) - {db['Potions']}")
                if db['SuperPotions'] > 0:
                    print(f"(SuperPotions) - {db['SuperPotions']}")
                if db['HyperPotions'] > 0:
                    print(f"(HyperPotions) - {db['HyperPotions']}")
                if db['MasterPotions'] > 0:
                    print(f"(MaxPotions) - {db['MaxPotions']}")
                y = input('')
                y = (y.strip()).lower()
                clear()
                if y == 'masterballs' and DisablePB == False:
                    if db['MasterBalls'] > 0:
                        db['MasterBalls'] -= 1
                        print('You throw a Master Ball! ')
                        pause(2)
                        level = str(level)
                        Entry = x + ',' + level
                        db['EeveeDmg'] = round(db['EeveeLv'] / 2)
                        db['Pokemon'].append(Entry)
                        print(f"Gotcha! You caught the {x}! ")
                        affirm()
                        clear()
                        return ''

                    else:
                        print('Invalid Option.')
                        affirm()
                        clear()

                elif y == 'greatballs' and DisablePB == False:
                    if db['GreatBalls'] > 0:
                        db['GreatBalls'] -= 1
                        print('You throw a Great Ball! ')
                        pause(2)
                        chance = random.randint(1, 10)
                        chance = chance - HP
                        if 'Shiny-' in x:
                            chance - 5
                        if chance > -15:
                            z = random.randint(1, 20)
                            if z > 4:
                                print(f"Gotcha! You caught the {x}! ")
                                Level = str(level)
                                Entry = x + ',' + Level
                                db['EeveeDmg'] = round(db['EeveeLv'] / 2)
                                db['Pokemon'].append(Entry)
                                affirm()
                                clear()
                                return ''
                            else:
                                print("Oh no! The Pokemon escaped!")
                                affirm()
                                clear()
                        elif chance > -30 and chance < -16:
                            z = random.randint(1, 20)
                            if z > 16:
                                print(f"Gotcha! You caught the {x}! ")
                                Level = str(Level)
                                Entry = x + ',' + Level
                                db['EeveeDmg'] = round(db['EeveeLv'] / 2)
                                db['Pokemon'].append(Entry)
                                affirm()
                                clear()
                                return ''
                            else:
                                print("Oh no! The Pokemon escaped!")
                                affirm()
                                clear()

                    else:
                        print('Invalid Option.')
                        affirm()
                        clear()
                elif y == 'potions':
                  if db['Potions'] > 0:
                    db['Potions'] -=1
                    db['EeveeHP'] += 20
                    print(f"{db['PokemonName']} gained 20 HP! It has {db['EeveeHP']} HP now!")
                    affirm()
                    clear()
              
                elif y == 'pokeballs' and DisablePB == False:
                    if db['PokeBalls'] > 0:
                        db['PokeBalls'] -= 1
                        print('You throw a pokeball! ')
                        pause(2)
                        chance = random.randint(1, 10)
                        chance = chance - HP
                        if 'Shiny-' in x:
                            chance - 5
                        if chance > -5:
                            z = random.randint(1, 20)
                            if z > 12:
                                print(f"Gotcha! You caught the {x}! ")
                                Level = str(level)
                                Entry = x + ',' + Level
                                db['EeveeDmg'] = round(db['EeveeLv'] / 2)
                                db['Pokemon'].append(Entry)
                                affirm()
                                clear()
                                return ''
                            else:
                                print("Oh no! The Pokemon escaped!")
                                affirm()
                                clear()
                        elif chance > -20 and chance < -5:
                            z = random.randint(1, 20)
                            if z > 18:
                                print(f"Gotcha! You caught the {x}! ")
                                Level = str(Level)
                                Entry = x + ',' + Level
                                db['EeveeDmg'] = round(db['EeveeLv'] / 2)
                                db['Pokemon'].append(Entry)
                                affirm()
                                clear()
                                return ''
                            else:
                                print("Oh no! The Pokemon escaped!")
                                affirm()
                                clear()

                    else:
                        print('Invalid Option.')
                        affirm()
                        clear()

        move = True
        MyEffects()
        if db['EeveeHP'] < 1:
            kl = 0
            for i in [0,1,2,3,4]:
              if db['PokeTeam'][i][2] > 1:
                kl += 1
            if kl > 0:
              switch()
            else:
              bruh = 6
              Loss()
 
              return ''
        elif HP < 1:
            if len(PokemonTeam) == 0:
              bruh = 6
              Win(level)
              return ''
            else:
              x = PokemonTeam[0]
              PokemonTeam.remove(x)
              t = x
              HP = level * 2
              print(f'{Trainer} sent out {x}! ')
              t = x
              MYNAME = t
              if MYNAME in [
            'Noivern', 'Umbreon', 'Jolteon', 'Espeon', 'Sylveon', 'Glaceon',
            'Flareon', 'Vaporeon', 'Leafeon', 'Gabite', 'Quagsire',
            'Charmeleon', 'Wartortle', 'Pikachu', 'Clefairy', 'Furret',
            'Weezing', 'Slowbro', 'Dewgong', 'Vibrava', 'Ninetails', 'Gyrados'
    ]:
                dmg = 5
                sdef = 5
              elif MYNAME in [
            'Blastoise',  'Charizard', 'Zygarde', 'Dragonite',
            'Raichu', 'Garchomp'
    ]:
                dmg = 10
                sdef = 10
              elif MYNAME in ['Lunala', 'Solgaleo', 'Zekrom', 'Arceus']:
                dmg = 13
                sdef = 13
              epoison = False
              eburn = False
              estun = False
              efreeze = False
              econfuse = False
              affirm()
              clear()
            
          
        ESTOP()
        if emove == True:
            omove = random.randint(1, 2)
            if omove == 1:
                executemove(battlemoves.movesid[pokemon.pokemonn[t][2]],
                            db['EeveeHP'], level, x, db['PokemonName'], False,
                            dmg, sdef, mdmg, mdef)
            elif omove == 2:
                executemove(battlemoves.movesid[pokemon.pokemonn[t][3]],
                            db['EeveeHP'], level, x, db['PokemonName'], False,
                            dmg, sdef, mdmg, mdef)

        emove = True
        if db['EeveeHP'] < 1:
            kl = 0
            for i in [0,1,2,3,4]:
              if db['PokeTeam'][i][2] > 0:
                kl += 1
            if kl > 0:
              switch()
            else:
              bruh = 6
              Loss()
              return ''
        elif HP < 1:
            if len(PokemonTeam) == 0:
              bruh = 6
              Win(level)
              return ''
            else:
              x = PokemonTeam[0]
              PokemonTeam.remove(x)
              HP = level * 2
              print(f'{Trainer} sent out {x}! ')
              epoison = False
              eburn = False
              estun = False
              efreeze = False
              econfuse = False
  
              t = x
              MYNAME = t
              if MYNAME in [
            'Noivern', 'Umbreon', 'Jolteon', 'Espeon', 'Sylveon', 'Glaceon',
            'Flareon', 'Vaporeon', 'Leafeon', 'Gabite', 'Quagsire',
            'Charmeleon', 'Wartortle', 'Pikachu', 'Clefairy', 'Furret',
            'Weezing', 'Slowbro', 'Dewgong', 'Vibrava', 'Ninetails', 'Gyrados'
    ]:
                dmg = 5
                sdef = 5
              elif MYNAME in [
            'Blastoise',  'Charizard', 'Zygarde', 'Dragonite',
            'Raichu', 'Garchomp'
    ]:
                dmg = 10
                sdef = 10
              elif MYNAME in ['Lunala', 'Solgaleo', 'Zekrom', 'Arceus']:
                dmg = 13
                sdef = 13


              affirm()
              clear()
        ThemEffects()


def Win(Level):
    global epoison, eburn, estun, efreeze, econfuse, Trophy, Trainer
    epoison = False
    eburn = False
    estun = False
    efreeze = False
    econfuse = False

    print('You won! ')
    pause(1)
    if Trophy == True:
        db['Trophys'] += 1
    xp = Level * random.randint(13, 17)
    if Battle == True:
        xp = round(xp * 1.5)
    if Training == True:
        xp = round(xp * 2)
    if Trainer != '':
      xp = round(xp*4)
    db['Encounters'] += xp

    if x == 'Princess Flareon':
        db['Salve'] = 5
    if (db['EeveeLv'] * 100) + (db['EeveeLv'] * 5) > db['Encounters']:
        if 1 == 1:
            print(f'Your pokemon gained {xp} xp! ')
        totalxp = (db['EeveeLv'] * 100) + (db['EeveeLv'] * 5)
        totalxp = totalxp - db['Encounters']
        print(f'Get {totalxp} more xp to level up!')
        print("Check your profile to see your pokemon's total xp!")

        db['EeveeDmg'] = round(db['EeveeLv'] / 2)
    else:
        print(f"{db['PokemonName']} leveled up! ")
        pause(2)

        db['EeveeLv'] += 1
        db['EeveeHP'] = db['EeveeLv'] * 2
        db['EeveeDmg'] = round(db['EeveeLv'] / 2)
        db['Encounters'] = 0
        print(f"{db['PokemonName']} is now level {db['EeveeLv']}! ")
        affirm()
        clear()

    from Evolutions import Evolve
    Evolve()
    cv = 0
    for i in db['PokeTeam']:
      if i[0] != 'Empty':
        db['PokeTeam'][cv][7] = db['PokeTeam'][cv][7] + xp
        if db['PokeTeam'][cv][7] > (db['PokeTeam'][cv][1] * 105):
          db['PokeTeam'][cv][1] += 1
          name = db['PokeTeam'][cv][0]
          print(f'{name} leveled up! ')
          db['PokeTeam'][cv][7] = 0
      cv += 1
    item = random.randint(1, 30)
    if item > 25:
        print(f"The {x} dropped a Pokeball! You add it to your inventory ")
        db['PokeBalls'] += 1
    elif item < 3:
        print(f"The {x} dropped a Potion! You add it to your inventory ")
        db['Potions'] += 1
    elif item > 3 and item < 15:
        if not 'Berries' in db.keys():
                db['Berries'] = [['Cheri', 0],['Chesto', 0],['Pecha', 0],['Rawst', 0],['Aspear', 0],['Leppa', 0],['Oran', 0],['Persim', 0],['Lum', 0],['Sitrus', 0],['Figy', 0],['Wiki', 0],['Mago', 0],['Aguav', 0],['Lapapa', 0],['Tamato',0]]
        rndberrynum = random.randint(3,5)
        addedberries = random.sample(['Cheri','Chesto','Pecha','Rawst','Aspear','Leppa','Oran','Persim','Lum','Sitrus','Figy','Wiki','Mago','Aguav','Lapapa','Tamato','Cheri','Chesto','Pecha','Rawst','Aspear','Leppa','Oran','Persim','Lum','Sitrus','Figy','Wiki'], rndberrynum)
        print(f"The {x} dropped some Berries! You got:")
        v = 0
        for i in addedberries:
                pause(1)
                if berries[addedberries[v]][2] == 'Common':
                        print(f'{i} - {Style.DIM}Common{Style.RESET_ALL}{Fore.RESET}')
                elif berries[addedberries[v]][2] == 'Uncommon':
                        print(f'{i} - {Fore.LIGHTGREEN_EX}Uncommon{Fore.RESET}')
                elif berries[addedberries[v]][2] == 'Rare':
                        print(f'{i} - {Fore.BLUE}Rare{Fore.RESET}')
                elif berries[addedberries[v]][2] == 'legendary':
                        print(f'{i} - {Fore.LIGHTYELLOW_EX}legendary{Fore.RESET}')
                elif berries[addedberries[v]][2] == 'Mythical':
                        print(f'{i} - {Fore.RED}Mythical{Fore.RESET}')
                elif berries[addedberries[v]][2] == 'Ultra':
                        print(f'{i} - {Fore.LIGHTMAGENTA_EX}Ultra{Fore.RESET}')
                else:
                        pass
                v += 1
                if i == 'Cheri':
                        db['Berries'][0][1] += 1
                elif i == 'Chesto':
                        db['Berries'][1][1] += 1
                elif i == 'Pecha':
                        db['Berries'][2][1] += 1
                elif i == 'Rawst':
                        db['Berries'][3][1] += 1
                elif i == 'Aspear':
                        db['Berries'][4][1] += 1
                elif i == 'Leppa':
                        db['Berries'][5][1] += 1
                elif i == 'Oran':
                        db['Berries'][6][1] += 1
                elif i == 'Persim':
                        db['Berries'][7][1] += 1
                elif i == 'Lum':
                        db['Berries'][8][1] += 1
                elif i == 'Sitrus':
                        db['Berries'][9][1] += 1
                elif i == 'Figy':
                        db['Berries'][10][1] += 1
                elif i == 'Wiki':
                        db['Berries'][11][1] += 1
                elif i == 'Mago':
                        db['Berries'][12][1] += 1
                elif i == 'Aguav':
                        db['Berries'][13][1] += 1
                elif i == 'Lapapa':
                        db['Berries'][14][1] += 1
                elif i == 'Tamato':
                        db['Berries'][15][1] += 1
                else:
                        pass
    elif item > 15 and item < 23:
        if not 'Cook' in db.keys():
                db['Cook'] = [['Leek', 0],['Apple', 0],['Bread', 0],['Steak', 0],['Fries', 0],['Instant Noodles', 0],['Rice', 0],['Chicken Broth', 0],['Cake', 0],['Slowpoke Tail', 0],['Fried Chicken', 0],['Moomoo Milk', 0],['Beans', 0],['Pasta', 0],['Sausage', 0],['Lettuce',0]]
        addedberries = random.sample(['Leek','Apple','Bread','Steak','Fries','Instant Noodles','Rice','Chicken Broth','Cake','Slowpoke Tail','Fried Chicken','Moomoo Milk','Beans','Pasta','Sausage','Lettuce','Leek','Apple','Bread','Steak','Fries','Instant Noodles','Rice','Chicken Broth','Cake','Beans','Sausage','Lettuce'], 1)
        print(f"The {x} dropped an ingredient! You got:")
        v = 0
        for i in addedberries:
                time.sleep(0.5)
                if ingredients[addedberries[v]][2] == 'Common':
                        print(f'{i} - {Style.DIM}Common{Style.RESET_ALL}{Fore.RESET}')
                elif ingredients[addedberries[v]][2] == 'Uncommon':
                        print(f'{i} - {Fore.LIGHTGREEN_EX}Uncommon{Fore.RESET}')
                elif ingredients[addedberries[v]][2] == 'Rare':
                        print(f'{i} - {Fore.BLUE}Rare{Fore.RESET}')
                elif ingredients[addedberries[v]][2] == 'legendary':
                        print(f'{i} - {Fore.LIGHTYELLOW_EX}legendary{Fore.RESET}')
                elif ingredients[addedberries[v]][2] == 'Mythical':
                        print(f'{i} - {Fore.RED}Mythical{Fore.RESET}')
                elif ingredients[addedberries[v]][2] == 'Ultra':
                        print(f'{i} - {Fore.LIGHTMAGENTA_EX}Ultra{Fore.RESET}')
                else:
                        pass
                v += 1
                if i == 'Leek':
                        db['Cook'][0][1] += 1
                elif i == 'Apple':
                        db['Cook'][1][1] += 1
                elif i == 'Bread':
                        db['Cook'][2][1] += 1
                elif i == 'Steak':
                        db['Cook'][3][1] += 1
                elif i == 'Fries':
                        db['Cook'][4][1] += 1
                elif i == 'Instant Noodles':
                        db['Cook'][5][1] += 1
                elif i == 'Rice':
                        db['Cook'][6][1] += 1
                elif i == 'Chicken Broth':
                        db['Cook'][7][1] += 1
                elif i == 'Cake':
                        db['Cook'][8][1] += 1
                elif i == 'Slowpoke Tail':
                        db['Cook'][9][1] += 1
                elif i == 'Fried Chicken':
                        db['Cook'][10][1] += 1
                elif i == 'Moomoo Milk':
                        db['Cook'][11][1] += 1
                elif i == 'Beans':
                        db['Cook'][12][1] += 1
                elif i == 'Pasta':
                        db['Cook'][13][1] += 1
                elif i == 'Sausage':
                        db['Cook'][14][1] += 1
                elif i == 'Lettuce':
                        db['Cook'][15][1] += 1
                else:
                        pass
    elif item == 15:
        print(
            f"The {x} disapears in a mist... The Sheening Perfume effect has been applied for 250 steps.... "
        )
        db['Perfume'] += 250

    if 1 == 1:
        mon = random.randint((Level * 1), (Level * 3))
    if Battle == True:
        mon += 1000
    if Training == True:
        mon *= 2
    if db['Double'] == True:
        mon = mon * 2
    print(f"You gained {mon}$! ")
    db['Money'] += mon
    affirm()
    clear()
    return ''


def Loss():
    global epoison, eburn, estun, efreeze, econfuse
    epoison = False
    eburn = False
    estun = False
    efreeze = False
    econfuse = False
    print('You lost! You blacked out! ')
    affirm()
    clear()


def MyEffects():
    global level, HP, x, dmg, sdef, mdmg, mdef, mpoison, mburn, mstun, mfreeze, mconfuse, epoison, eburn, estun, efreeze, econfuse
    if mpoison == True:
        db['EeveeHP'] -= random.randint((db['EeveeLv'] - 3),
                                        (db['EeveeLv'] - 1))
        print(f"{db['PokemonName']} took damage from the poison! ")
        affirm()
        clear()
    if mburn == True:
        db['EeveeHP'] -= random.randint((db['EeveeLv'] - 3),
                                        (db['EeveeLv'] - 1))
        print(f"{db['PokemonName']} took damage from the burn! ")
        affirm()
        clear()
    if mconfuse == True:
        h = random.randint(1, 2)
        if h == 1:
            db['EeveeHP'] -= random.randint((db['EeveeLv'] - 3),
                                            (db['EeveeLv'] - 1))
            print(f"{db['PokemonName']} hit itself in confusion! ")
        g = random.randint(1, 4)
        if g == 4:
            mconfuse = False
            print(f"{db['PokemonName']} snapped out of its confusion! ")
        affirm()
        clear()


def ThemEffects():
    global level, HP, x, dmg, sdef, mdmg, mdef, mpoison, mburn, mstun, mfreeze, mconfuse, epoison, eburn, estun, efreeze, econfuse
    if epoison == True:
        HP -= random.randint((level - 3), (level - 1))
        print(f"{x} took damage from the poison! ")
        affirm()
        clear()
    if eburn == True:
        HP -= random.randint((level - 3), (level - 1))
        print(f"{x} took damage from the burn! ")
        affirm()
        clear()
    if econfuse == True:
        h = random.randint(1, 2)
        if h == 1:
            HP -= random.randint((level - 3), (level - 1))
            print(f"{x} hit itself in confusion! ")
        g = random.randint(1, 4)
        if g == 4:
            econfuse = False
            print(f'{x} snapped out of its confusion! ')
        affirm()
        clear()


def StopMe():
    global mstun, mfreeze, move
    if mstun == True:
        jo = random.randint(1, 2)
        if jo == 1:
            move = False
            print(f'{db["PokemonName"]} is paralyzed!')
            affirm()
            clear()
        jo = random.randint(1, 4)
        if jo == 1:
            mstun = False
            print(f"{db['PokemonName']} snapped out of the paralysis! ")
            affirm()
            clear()
    if mfreeze == True:
        jo = random.randint(1, 3)
        if jo == 1 or jo == 2:
            move = False
            print(f'{db["PokemonName"]} is frozen!')
            affirm()
            clear()
        jo = random.randint(1, 3)
        if jo == 1:
            mfreeze = False
            print(f"{db['PokemonName']} thawed out! ")
            affirm()
            clear()


def ESTOP():
    global estun, efreeze, emove, x
    if estun == True:
        jo = random.randint(1, 2)
        if jo == 1:
            emove = False
            print(f'{x} is paralyzed!')

            affirm()
            clear()
        jo = random.randint(1, 4)
        if jo == 1:
            estun = False
            print(f"{x} snapped out of the paralysis! ")
            affirm()
            clear()
    if efreeze == True:
        jo = random.randint(1, 3)
        if jo == 1 or jo == 2:
            emove = False
            print(f'{x} is frozen!')
            affirm()
            clear()
        jo = random.randint(1, 3)
        if jo == 1:
            efreeze = False
            print(f"{x} thawed out! ")
            affirm()
            clear()
