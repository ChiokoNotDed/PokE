from functions import affirm, clear, pause
from replit import db
import pokemon
from pokemon import berries, ingredients
from getkey import getkey, keys
import random

cookinglist = []
yi = []
ingredient = 0
swflavor = 0
soflavor = 0
biflavor = 0
spflavor = 0
drflavor = 0
berryadd = []
cookinglist = []

def campsite():
        clear()
        print(f'''Your at the camp!
(1) Check Pokemon
(2) Play
(3) Cook
(4) Train
(5) Leave Camp''')
        campS = input('What would you like to do: ')
        clear()
        if campS == '1':
                print(db['PokeTeam'])
                affirm()
                campsite()
        elif campS == '2':
                print('Play Wip')
                affirm()
                campsite()
        elif campS == '3':
                cookinglist = []
                cook()
        elif campS == '4':
                print('Train Wip')
                affirm()
                campsite()
        elif campS == '5':
                clear()
        else:
                campsite()
def cook():
        global yi, ingredient, cookinglist, berryadd, cookinglist
        no = 0
        for i in db['Cook']:
                if i[1] < 1:
                        no += 1
        if no == 16:
                print('You have no ingredients to cook with.')
                affirm()
                clear()
                campsite()
        no = 0
        for i in db['Berries']:
                if i[1] < 1:
                        no += 1
        if no == 16:
                print('You have no berries to cook with.')
                affirm()
                clear()
                campsite()
        clear()
        v = 1
        yi = []
        for i in db['Cook']:
                if i[1] > 0:
                        yi.append(i)
                        print(f'({v}) {i[0]}: {i[1]}')
                        v += 1
        ingredient = input('Pick a main ingredient: ')
        try:
                ingredient = int(ingredient)
                ingredient -= 1
        except:
                cook()
        if ingredient > -1 and ingredient < v:
                pass
        else:
                cook()
        finish = False
        while len(cookinglist) < 10:
                clear()
                v = 1
                yb = []
                for i in db['Berries']:
                        if i[1] > 0:
                                yb.append(i)
                                print(f'({v}) {i[0]}: {i[1]}')
                                v += 1
                berry = input('Pick a berry: ')
                try:
                        berry = int(berry)
                        berry -= 1
                except:
                        cook()
                if berry > -1 and berry < v:
                                cookinglist.append(yb[berry][0])
                                clear()
                                v = 0
                                print('Cooking List:')
                                for i in cookinglist:
                                        print(f'{cookinglist[v]}')
                                        v += 1
                                print('')
                                print('(1) Start Cooking')
                                print('(2) Add More Berries')
                                print('(3) Stop Cooking')
                                choice = input('What would you like to do: ')
                                if choice == '1':
                                        cookfood()
                                if choice == '2':
                                        Berrynum = ['Cheri', 'Chesto', 'Pecha', 'Rawst', 'Aspear', 'Leppa', 'Oran', 'Persim', 'Lum', 'Sitrus', 'Figy', 'Wiki', 'Mago', 'Aguav', 'Tamato', 'Lapapa']
                                        berryindex = Berrynum.index(yb[berry][0])
                                        berryadd.append([yb[berry][0]])
                                        db['Berries'][berryindex][1] -= 1
                                        pass
                                if choice == '3':       
                                        campsite()
                                else:
                                        pass 
                else:
                        cook()
        clear()
        print('Max berry limit reached!')
        affirm()
        clear()
        cookfood()
def cookfood():
        global yi, ingredient, cookinglist, swflavor, soflavor, biflavor, spflavor, drflavor, cookinglist
        Cooknum = ['Leek', 'Apple', 'Bread', 'Steak', 'Fries', 'Instant Noodles', 'Rice', 'Chicken Broth', 'Cake', 'Slowpoke Tail', 'Fried Chicken', 'Moomoo Milk', 'Beans', 'Pasta', 'Sausage', 'Lettuce']
        Berrynum = ['Cheri', 'Chesto', 'Pecha', 'Rawst', 'Aspear', 'Leppa', 'Oran', 'Persim', 'Lum', 'Sitrus', 'Figy', 'Wiki', 'Mago', 'Aguav', 'Tamato', 'Lapapa']
        clear()
        ingfood = yi[ingredient][0]
        cookindex = Cooknum.index(ingfood)
        db['Cook'][cookindex][1] -= 1
        pop = 0
        for i in cookinglist:
                berryindex = Berrynum.index(i)
                db['Berries'][berryindex][1] -= 1
                if berries[i[0]][1] == 1:
                        swflavor += 1
                elif berries[i[0]][1] == 2:
                        soflavor += 1
                elif berries[i[0]][1] == 3:
                        biflavor += 1
                elif berries[i[0]][1] == 4:
                        spflavor += 1
                elif berries[i[0]][1] == 5:
                        drflavor += 1
                if berries[i[0]][0] == 5:
                        pop += 1
                elif berries[i[0]][0] == 10:
                        pop += 2
                elif berries[i[0]][0] == 15:
                        pop += 3
                elif berries[i[0]][0] == 20:
                        pop += 4
                elif berries[i[0]][0] == 25:
                        pop += 5
                elif berries[i[0]][0] == 30:
                        pop += 6
        compare = [swflavor, soflavor, biflavor, spflavor, drflavor]
        flav = max(compare)
        if flav == swflavor:
                flavor = 'Sweet'
        elif flav == soflavor:
                flavor = 'Sour'
        elif flav == biflavor:
                flavor = 'Bitter'
        elif flav == spflavor:
                flavor = 'Spicy'
        elif flav == drflavor:
                flavor = 'Dry'
        heat = 0
        while heat <= 100:
                clear()
                if heat != 0:
                        rndheat = random.randint(1,3)
                        if rndheat == 1:
                                rndheat = random.randint(1,3)
                                heat -= rndheat
                print('Spam [SPACE] to cook the food!')
                print(f'Heat: {heat}/100')
                key = getkey()
                if key == keys.SPACE:
                        rndheat = random.randint(1,3)
                        heat += rndheat
        clear()
        print('Your food is ready!')
        affirm()
        clear()
        print(f'You made a {flavor} {ingredients[yi[ingredient][0]][1]}!')
        xp = 0
        if pop < 11 and pop > 0:
                cookmsg = 'Your pokemon HATED that! It was a total disaster.'
                xp = 0
        elif pop < 21 and pop > 10:
                cookmsg = "Your pokemon don't want to eat it anymore. They didn't even finish their plates!"
                xp = random.randint(1,10)
        elif pop < 31 and pop > 20:
                cookmsg = 'Your pokemon were satisfied with the meal.'
                xp = random.randint(10,100)
        elif pop < 41 and pop > 30:
                cookmsg = 'Your pokemon liked it! They came back for seconds.'
                xp = random.randint(100,1000)
        elif pop < 51 and pop > 40:
                cookmsg = 'Your pokemon loved it! They want to eat it every night!'
                xp = random.randint(1000,10000)
        elif pop < 61 and pop > 50:
                cookmsg = "Your pokemon are in heaven with how perfectly balanced this dish it. Not only is it's exsquite flavor delectable, its bountiful too! Your pokemon are full with food and happy dreams."
                xp = random.randint(10000,100000)
        print(cookmsg)
        affirm()
        clear()
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
        affirm()
        clear()
        campsite()
'''
0-10 = EWWWW
11-20 = yuck
21-30 = ok
31-40 = good
41-50 = great
51-60 = yummy!
'''