from colorama import *
#'Pokemon': [type1, type2, move1, move 2, move3, move4]
# Normal: 1
# Grass: 2
# Water: 3
# Fire: 4
# Flight: 5
# Ground: 6
# Dark: 7
# Poison: 8
# Electric: 9
# Ice: 10
# Fighting: 11
# Psychic: 12
# Bug: 13
# Rock: 14
# Ghost: 15
# Dragon: 16
# Steel: 17
# Fairy: 18

# Polarized List:
# Normal: Dark
# Grass: Rock
# Water: Poison
# Fire: Ice
# Flight: Ground
# Ground: Flight
# Dark: Normal
# Poison: Water
# Electric: Fairy
# Ice: Fire
# Fighting: Bug
# Psychic: Steel
# Bug: FIghting
# Rock: Grass
# Ghost: Dragon
# Dragon: Ghost
# Steel: Psychic
# Fairy: Electric
pokemonn = {
  'Noivern': [5, 16, 57, 15, 23, 29],
  # 'Polarized-Noivern': [6, 15, 12, 17], # Done
  'Umbreon': [7, 7, 37, 4, 11, 12],
  # 'Polarized-Umbreon': [1, 1, 6, 11], # Done
  'Eevee': [1, 1, 6, 14, 45, 47],
  # 'Polarized-Eevee': [7, 7, 4, 40], # Done
  'Gible': [16, 6, 7, 15, 23, 29],
  # 'Polarized-Gible': [15, 5, 6, 14],
  'Gabite': [16, 6, 7, 15, 23, 29],
  # 'Polarized-Gabite': [15, 5, 6, 14],
  'Garchomp': [16, 6, 15, 17, 30, 24],
  # 'Polarized-Garchomp': [15, 5, 6, 14],
  'Cubchoo': [10, 10, 46, 2, 39, 49],
  # 'Polarized-Cubchoo': [4, 4, 46, 2],
  'Beartic': [10, 10, 46, 5, 39, 49],
  # 'Polarized-Beartic': [4, 4, 46, 5],
  'Yamask': [15, 15, 27, 12, 13, 10],
  # 'Polarized-Yamask': [16, 16, 27, 12],
  'Wooper': [3, 6, 7, 10, 13, 10],
  # 'Polarized-Wooper': [8, 5, 7, 10],
  'Quagsire': [3, 6, 25, 17, 13, 10], #Infmy's favorite pokemon
  # 'Polarized-Quagsire': [8, 5, 25, 17], 
  'Remoraid': [3, 3, 10, 2, 25, 32],
  # 'Polarized-Remoraid': [8, 8, 10, 2],
  'Octillery': [3, 3, 2, 25, 32, 42],
  # 'Polarized-Octillery': [8, 8, 2, 25],
  'Rattata': [1, 1, 7, 12, 47, 48],
  # 'Polarized-Rattata': [7, 7, 7, 12],
  'Bulbasaur': [2, 8, 0, 1, 47, 48],
  # 'Polarized-Bulbasaur': [14, 3, 0, 1],
  'Ivysaur': [2, 8, 48, 50],
  'Venusaur': [2, 8, 50, 43],
  'Squirtle': [3, 3, 9, 2, 41, 39],
  # 'Polarized-Squirtle': [8, 8, 9, 2],
  'Charmander': [4, 4, 18, 4, 37, 34],
  # 'Polarized-Charmander': [10, 10, 18, 4],
  'Charmeleon': [4, 4, 18, 4, 37, 34],
  # 'Polarized-Charmeleon': [10, 10, 18, 4],
  'Pidgey': [1, 5, 16, 24, 15, 25],
  # 'Polarized-Pidgey': [7, 6, 16, 24],
  'Sandile': [6, 7, 7, 4, 15, 21],
  # 'Polarized-Sandile': [5, 1, 7, 4],
  'Sandshrew': [6, 6, 8, 21, 15, 7],
  # 'Polarized-Sandshrew': [5, 5, 8, 21],
  'Skorupi': [13, 8, 1, 26, 48, 33],
  # 'Polarized-Skorupi': [11, 3, 1, 26],
  'Machop': [11, 11, 14, 6 ],
  # 'Polarized-Machop': [13, 13, 14, 6],
  'Abra': [12, 12, 3, 13],
  # 'Polarized-Abra': [17, 17, 3, 13],
  'Zygarde': [6, 16, 14, 6],
  # 'Polarized-Zygarde': [5, 15, 14, 6],
  'Caterpie': [13, 13, 33, 0],
  'Metapod': [13, 13, 28, 42],
  # 'Polarized-Caterpie': [11, 11, 33, 0],
  'Rolycoly': [14, 14, 34, 38],
  # 'Polarized-Rolycoly': [2, 2, 34, 38],
  'Pikachu': [9, 9, 35, 36],
  # 'Polarized-Pikachu': [9, 9, 35, 36],
  'Litwick': [15, 4, 22, 27],
  # 'Polarized-Litwick': [15, 4, 22, 27],
  'Dreepy': [16, 15, 30, 27],
  # 'Polarized-Dreepy': [16, 15, 30, 27],
  'Aron': [17, 14, 37, 34],
  # 'Polarized-Aron': [17, 14, 37, 34],
  'Clefairy': [18, 18, 31, 32],
  # 'Polarized-Clefairy': [18, 18, 31, 32],
  'Spheal': [10, 3, 49, 9],
  # 'Polarized-Spheal': [10, 3, 49, 9],
  'Raichu': [9, 9, 35, 36],
  # 'Polarized-Raichu': [9, 9, 35, 36],
  'Slowbro': [12, 3, 10, 13],
  # 'Polarized-Slowbro': [12, 3, 10, 13],
  'Weezing': [8, 8, 1, 43],
  'Furret': [1, 1, 6, 45],
  'Leafeon': [2, 2, 28, 50],
  'Gyarados': [5, 3, 10, 24],
  'Jigglypuff': [18, 1, 31, 45],
  'Sandslash': [6, 6, 21, 17],
  'Poliwhirl': [3, 3, 9, 10],
  'Magnemite': [9, 17, 36, 39],
  "Farfetch'd": [5, 1, 45, 24],
  'Serperior': [2, 2, 28, 0],
  'Polywrath': [11, 3, 9, 41],
  'Ultra-Kyogre': [3, 3, 6, 10],
  'Ninetails': [4, 4, 19, 20],
  'Vaporeon': [3, 3, 9, 10],
  'Dragonite': [5, 16, 23, 29],
  'Blastoise': [3, 3, 6, 10],
  'Porygon2': [1, 1, 47, 11],
  'Gloom': [2, 8, 28, 48],
  'Kricketune': [13, 13, 33, 42],
  'Arbok': [8, 8, 43, 48],
  'Dewgong': [10, 3, 46, 9],
  'Kadabra': [12, 12, 3, 13],
  'Golduck': [3, 3, 9, 25],
  'Kingler': [3, 3, 9, 10],
  'Wartortle': [3, 3, 9, 25],
  'Oddish': [1, 2, 0, 45],
  'Voltorb': [9, 9, 44, 35],
  'Lickitung': [1, 1, 47, 27],
  'Poliwag': [3, 3, 9, 10],
  'Bellsprout': [2, 8, 28, 48],
  'Tentacool': [3, 8, 10, 43],
  'Seel': [3, 3, 9, 10],
  'Horsea': [3, 3, 9, 10],
  'Rhyhorn': [6, 14, 21, 34],
  'Magikarp': [3, 3, 9, 10],
  'Dratini': [16, 16, 30, 15],
  'Gastly': [15, 8, 12, 43],
  'Doduo': [1, 5, 16, 45],
  'Psyduck': [3, 3, 9, 10],
  'Onix': [6, 14, 17, 38],
  'Grimer': [8, 8, 43, 6],
  'Shellder': [3, 3, 9, 10],
  'Azurill': [1, 18, 6, 31],
  'Charizard': [4, 5, 19, 30],
  'Flareon': [4, 4, 19, 20],
  'Vibrava': [6, 16, 8, 15],
  'Sylveon': [18, 18, 31, 32],
  'Glaceon': [10, 10, 2, 5],
  'Jolteon': [9, 9, 35, 36],
  'Espeon': [12, 12, 3, 13], 
  'Zekrom': [9, 16, 30, 36, 52, 23],
  'Ratatta': [1, 1, 11, 14, 33, 18],
  'Princess Flareon': [4, 4, 19, 20, 43, 27],
  'Reshiram': [4, 16, 51, 30, 23, 34],
  'Lunala': [15, 12, 53, 46],
  'Solgaleo': [12, 17, 54, 22],
  'Arceus': [1, 1, 55, 40],
  'Rowlet': [2, 5, 0, 4],
  'Inteleon': [3, 3, 25, 47],
  'Steelix': [17, 17, 39, 38 ],
  'Piplup': [3, 3, 9, 14],
  'Quaxly': [3, 5, 9, 24],
  'Pidgeotto': [1, 5, 11, 16],
  'Butterfree': [13, 5, 42, 24],
  'Arcanine': [4, 4, 20, 18],
  'Electivire': [9, 9, 44, 52], 
  'Tyranitar': [14, 7, 34, 40],
  'Krabby': [3, 3, 9, 10],
  'Pawniard': [3, 3, 10, 10],
  'Bisharp': [5, 5, 20, 22],
# New Pokemon
  'Piethon': [17, 12, 52, 37], # Pie
  'Jaavaa': [17, 12, 39, 12], # Coffee
  'Cei++': [17, 18, 60, 61], # Cookie
  'Caikit': [2, 1, 64, 65],  # Grass Cake Cat Starter
  'Chocleon': [4, 1, 66, 67], # Fire Chocolate Chameleon Starter
  'Soadapup': [3, 1, 68, 69], # Water Soda Dog Starter
  'Caikatt': [2, 18, 70, 71], 
  'Cocoaleon': [4, 7, 72, 73], 
  'Softipop': [3, 8, 74, 75], 
  'Caikatat': [2, 18, 76, 77],
  'Choclameleon': [4, 7, 78, 79],
  'Poplipup': [3, 8, 80, 81],
  'Jazzal': [6, 16, 21, 30], # Jazzal evo 1
  'Rockinstone': [14, 16, 34, 15], # Jazzal evo 2
  'Fancidove': [12, 11, 3, 14], # Fancidove evo 1
# Evolve a Fancidove with a fighting type move
  'Classiquail': [11, 11, 47, 41], # Fancidove evo 2
# Evolve a Fancidove with a psychic type move
  'Aristoquack': [12, 12, 13, 86], # Fancidove evo 2
  'Rick Astley': [1, 1, 1, 1], # Best poekemon

# Special / Legendary Pokemon
  'Rainbow-Leafeon GX': [2, 18, 84, 85],
  'Super-Dunce': [1, 11, 58, 59], # Striker's Special Pokemon ;)
  f"Striker's-Charizard": [18, 4, 62, 63],
f'{Fore.RED}Col{Fore.LIGHTYELLOW_EX}ore{Fore.LIGHTGREEN_EX}d-N{Fore.BLUE}oiv{Fore.MAGENTA}ern{Fore.RESET}': [18, 16, 9, 10],
  f'{Style.DIM}Silvered-Leafeon{Style.RESET_ALL}': [18, 2, 60, 61],
  'Articuno': [5, 10, 23, 46],
  'Zapdos': [5, 9],
  'Moltres': [5, 4],
  'Mewtwo': [],
  'Mew': [],
  'Raikou': [9],
  'Entei': [4],
  'Suicune': [],
  'Ho-oh': [5, 4],
  'Lugia': [5],
  'Regirock': [],
  'Regice': [],
  'Registeel': [],
  'Latios': [5],
  'Latias': [5],
  'Kyogre': [],
  'Groudon': [],
  'Rayquaza': [],
  'Uxie': [],
  'Mesprit': [],
  'Azelf': [],
  'Dialga': [],
  'Palkia': [],
  'Heatran': [4],
  'Regigigas': [],
  'Giratina': [],
  'Cresselia': [],
  
  
  

  
}

'''
Cheri Chesto Pecha Rawst Aspear Leppa Oran Persim Lum Sitrus Figy Wiki Mago Aguav Lapapa Tamato
'''


# 'Berry': [Heal, Type, Rarity]

# Berry Types:
# N/A:0
# Sweet:1
# Sour:2
# Biter:3
# Spicy:4
# Dry:5

# Rarity's:
# 5 - Common
# 10 - Uncommon
# 15 - Rare
# 20 - Legendary
# 25 - Mythical
# 30 - Ultra

# Amounts
# Common - 5
# Uncommon - 4
# Rare - 3
# Legendary - 2
# Mythical - 1
# Ultra - 1

berries = {
        'Cheri': [10, 4, 'Uncommon'],
        'Chesto': [5, 5, 'Common'],
        'Pecha': [5, 1, 'Common'],
        'Rawst': [15, 3, 'Rare'],
        'Aspear': [5, 2, 'Common'],
        'Leppa': [15, 4, 'Rare'],
        'Oran': [5, 1, 'Common'],
        'Persim': [10, 1, 'Uncommon'],
        'Lum': [5, 3, 'Common'],
        'Sitrus': [10, 2, 'Uncommon'],
        'Figy': [10, 4, 'Uncommon'],
        'Wiki': [5, 5, 'Common'],
        'Mago': [20, 1, 'Legendary'],
        'Aguav': [20, 3, 'Legendary'],
        'Tamato': [25, 4, 'Mythical'],
        'Lapapa': [30, 2, 'Ultra'],
}

ingredients = {
        'Leek': [10, 'Leek', 'Uncommon'],
        'Apple': [5, 'Apple', 'Common'],
        'Bread': [5, 'Toast', 'Common'],
        'Steak': [15, 'Steak', 'Rare'],
        'Fries': [10, 'Fries', 'Uncommon'],
        'Instant Noodles': [15, 'Noodles', 'Rare'],
        'Rice': [5, 'Curry', 'Common'],
        'Chicken Broth': [10, 'Stew', 'Uncommon'],
        'Cake': [15, 'Cake', 'Rare'],
        'Slowpoke Tail': [20, 'Slowpoke Tail', 'Legendary'],
        'Fried Chicken': [30, 'Fried Chicken', 'Ultra'],
        'Lettuce': [5, 'Salad', 'Common'],
        'Moomoo Milk': [20, 'Smoothie', 'Legendary'],
        'Beans': [5, 'Beans', 'Common'],
        'Pasta': [25, 'Pasta', 'Mythical'],
        'Sausages': [10, 'Sausages', 'Uncommon'],
}