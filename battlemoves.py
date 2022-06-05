
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
#[Accuracy, Base Power, Attack Boost, Defense Increase, Percent Healed, Type, PP]
moves = {
  'Absorb': [100, 20, 0, 0, 50, 2, 25], #Grass 0 done
  'Acid': [100, 40, 10, 0, 0, 8,  30], #Poison 1 done
  'Aurora Beam': [100, 65, 0, 10, 0, 10, 20], #Ice 2 done
  'Barrier': [0, 5, 0, 100, 0, 12, 10], #Psychic 3 done
  'Bite': [100, 60, 0, 0, 0, 7, 15], #Dark 4 done
  'Blizzard': [70, 110, 0, 0, 0, 10, 10], #Ice 5 done
  'Body Slam': [100, 85, 0, 0, 0, 1, 10], #Normal 6 done
  'Bone Club': [85, 65, 0, 0, 0, 6, 20], #Ground 7 done
  'Bonemerang': [90, 50, 0, 0, 0, 6, 20], #Ground 8 done
  'Bubble': [100, 40, 0, 0, 0, 3, 30], #Water 9 done
  'Bubble Beam': [100, 65, 0, 0, 0, 3, 20], #Water 10 done
  'Comet Punch': [100, 18, 0, 0, 0, 1, 15], #Normal 11 done
  'Confuse Ray': [100, 0, 0, 0, 0, 15, 10], #Ghost 12
  'Confusion': [100, 50, 0, 0, 0, 12, 20], #Psychic 13
  'Double Kick': [100, 30, 0, 0, 0, 11, 30], #Fighting 14 done
  'Dragon Rage': [100, 75, 0, 0, 0, 16, 15], #Dragon 15 done
  'Drill Peck': [100, 80, 0, 0, 0, 5, 20], #Flying 16 done
  'Earthquake': [100, 80, 0, 0, 0, 6, 10], #Ground 17 done
  'Ember': [100, 40, 0, 0, 0, 4, 25], #Fire 18 done
  'Fire Blast': [85, 110, 0, 0, 0, 4, 10], #Fire 19 done
  'Fire Spin': [85, 35, 0, 0, 0, 4, 15], #Fire 20 done
  'Fissure': [30, 5, 0, 0, 0, 5, 5], #Ground 21 done
  'Flamethrower': [100, 90, 0, 0, 0, 4, 10], #Fire 22 done
  'Air Slash': [95, 90, 0, 0, 0, 5, 15], #Flying 23 done
  'Gust': [100, 40, 0, 0, 0, 5, 25], #Flying 24 done
  'Hydro Pump': [80, 110, 0, 0, 0, 3, 10], #Water 25 done
  'Leech Life': [100, 80, 0, 0, 50, 13, 20], #Bug 26 done
  'Lick': [100, 30, 0, 0, 0, 15, 10], #Ghost 27 done
  'Mega Drain': [100, 40, 0, 0, 50, 2, 15], #Grass 28 done
  'Draco Meteor': [100, 75, 0, 0, 0, 16, 20], #Dragon 29 done
  'Dragon Breath': [75, 100, 0, 0, 0, 16, 15], #Dragon 30 done
  'Draining Kiss': [85, 80, 0, 0, 50, 18, 10], #Fairy 31 done
  'Moon Blast': [100, 110, 0, 0, 0, 18, 10], #Fairy 32 done
  'Bug Bite': [100, 60, 0, 0, 0, 13,15], #Bug 33 done
  'Rock Tomb': [95, 100, 0, 0, 0, 14, 15], #Rock 34 done
  'Thunder Shock': [95, 55, 0, 0, 0, 9, 20], #Electric 35 done
  'Nuzzle': [85, 100, 0, 0, 0, 9, 10], #Electric 36 done
  'Hone Claws': [100, 5, 100, 0, 0, 17, 10], #Steel 37 done
  'Diamond Storm': [95, 65, 0, 100, 0, 14, 10], #Rock 38
  'Iron Head': [100, 65, 0, 0, 0, 17, 10], #Steel 39 done
  'Shadow Claw': [90, 100, 0, 0, 0, 7, 10], #Dark 40 done
  'Close Combat': [100, 100, 0, 0, 0, 11, 15], #Fighting 41 done
  'Bug Buzz': [100, 80, 0, 0, 0, 13, 20], #Bug 42 done
  'Poison Fang': [90, 95, 0, 0, 0, 8, 20], #Poison 43 done
  'Thunder Punch': [100, 75, 0, 0, 0, 9, 20], #Electric 44 done
  'Egg Bomb': [75, 100, 0, 0, 0, 1, 15], #Normal 45 done
  'Ice Beam': [100, 95, 0, 0 ,0, 10, 10], #Ice 46 done
  'Mega Kick': [75, 120, 0, 0, 0, 1, 5], #Normal 47 done
  'Poison Powder': [75, 5, 0, 0, 0, 8, 10], #Poison 48 done
  'Ice Punch': [100, 75, 0, 0, 0, 10, 15], #Ice 49 done
  'Leaf Blade': [100, 90, 0, 0, 0, 2, 15], #Grass 50 done
  'Fusion Flare': [100, 120, 0, 0, 0, 4, 5], #Fire 51 done
  'Bolt Strike': [85, 130, 0, 0, 0, 9, 5], #Electric 52 done
  'Moongeist Beam': [100, 120, 0, 0, 0, 18, 5], #Fairy 53 done
  'Sunsteel Strike': [100, 120, 0, 0, 0, 17, 5], #Steel 54
  'Hyper Beam': [90, 150, 0, 0, 0, 1, 10], #Normal 55
  'Rainbow Rage': [90, 200, 25, 10, 15, 18, 5], #Fairy 56 (Unique)
  'Boomburst': [100, 150, 0, 0, 0, 1, 10], #Normal 57
  'Intelligence Drop': [100, 0, 25, -25, 0, 1, 5], #Normal 58 (Unique)
  'Dunce Dance': [50, 50, 0, 0, -20, 11, 10], #Fighting 59 (Unique)
  "Developer's Fury": [100, 100, 10, 0, 0, 18, 5], #Fairy 60 (Unique)
  'Bug Fix': [100, 10, 10, 10, 0, 1, 10], #Normal 61 (Unique)
  'Flame Strike': [100, 100, 5, -5, 0, 4, 10], #Fire 62 (Unique)
  'Fire Hazard': [75, 50, 10, -10, 0, 4, 5], #Fire 63 (Unique)
  'Cake Crush': [95, 75, 0, 0, 0, 1, 10], #Normal 64 
  'Sweet Nectar': [100, 0, -10, 10, 0, 2, 5], #Grass 65
  'Choco Chomp': [85, 60, 10, 0, 0, 4, 10], #Fire 66
  'Blend Through': [100, 50, -10, 20, 0, 1, 15], #Normal 67 
  'Fizzle': [75, 10, 10, 0, 15, 1, 10], #Normal 68 
  'Soda Pop': [100, 100, 0, 0, 0, 3, 5], #Water 69 
  'Grass Frosting': [100, 10, 0, 0, 20, 2, 5], #Grass 70
  'Foilage': [75, 20, -10, 20, 20, 18, 20], #Fairy 71
  'Spicy Cocoa Crunch': [100, 100, 10, 10, -10, 4, 15], #Fire 72
  'Co-op Blend': [100, 10, 10, 10, 10, 1, 10], #Normal 73
  'Caffine Craze': [75, 125, -25, -25, -25, 8, 5], #Poison 74
  'Fizz Bliss': [100, 15, 15, 15, 15, 3, 10], #Water 75
  'Cake Blitz': [80, 100, 5, 5, 5, 18, 5], #Fairy 76
  'Grass Bomb': [70, 125, -5, -5, -5, 2, 10], #Grass 77
  'Choco Flare': [100, 50, 10, 0, 0, 4, 5], #Fire 78
  'Dark Chocolate Blare': [90, 100, 0, 30, 0, 7, 15], #Dark 79
  'Sugar Rush': [75, 150, -25, -25, -25, 8, 10], #Poison 80 
  'Refesh': [75, -10, 25, 25, 25, 3, 5], #Water 81
  'Chloroblast': [90, 120, 0, 0, 0, 2, 5], #Grass 82
  'Light of Ruin': [75, 140, 0, 0, 0, 18, 10], #Fairy 83
  "Let's Snuggle Forever": [90, 190, 0, 0, 0, 18, 5], #Fairy 84
  'Power Whip': [100, 140, 0, 0, 0, 2, 10], #Grass 85
  'Prismatic Lazer': [100, 110, 0, 0, 0, 12, 15], #Psychic 86
}
movesid = ['Absorb', 'Acid', 'Aurora Beam', 'Barrier', 'Bite', 'Blizzard', 'Body Slam', 'Bone Club', 'Bonemerang', 'Bubble', 'Bubble Beam', 'Comet Punch', 'Confuse Ray', 'Confusion', 'Double Kick', 'Dragon Rage', "Drill Peck", 'Earthquake', 'Ember', 'Fire Blast', 'Fire Spin', 'Fissure', 'Flamethrower', 'Air Slash', 'Gust', 'Hydro Pump', 'Leech Life', 'Lick', 'Mega Drain', 'Draco Meteor', 'Dragon Breath', 'Draining Kiss', 'Moon Blast', 'Bug Bite', 'Rock Tomb', 'Thunder Shock', 'Nuzzle', 'Hone Claws', 'Diamond Storm', 'Iron Head', "Shadow Claw", 'Close Combat', 'Bug Buzz', 'Poison Fang', 'Thunder Punch', 'Egg Bomb', 'Ice Beam', 'Mega Kick', 'Poison Powder', 'Ice Punch', 'Leaf Blade', 'Fusion Flare', 'Bolt Strike', 'Moongeist Beam', 'Sunsteel Strike', 'Hyper Beam', 'Rainbow Rage', 'Boomburst', 'Intelligence Drop', 'Dunce Dance', "Developer's Fury", 'Bug Fix', 'Flame Strike', 'Fire Hazard', 'Cake Crush', 'Sweet Nectar', 'Choco Chomp', 'Blend Through', 'Fizzle', 'Soda Pop', 'Grass Frosting', 'Foilage', 'Spicy Cocoa Crunch', 'Co-op Blend', 'Caffine Craze', 'Fizz Bliss', 'Cake Blitz', 'Grass Bomb', 'Choco Flare', 'Dark Chocolate Blare', 'Sugar Rush', 'Refresh', 'Chloroblast', 'Light of Ruin', "Let's Snuggle Forever", 'Power Whip', 'Prismatic Lazer']

'''


Normal: 2
Grass: 2
Water: 3
Fire: 4
Flight: 3
Ground: 3
Dark: 2
Poison: 2
Electric: 2
Ice: 2
Fighting: 2
Psychic: 2
Bug: 3
Rock: 2
Ghost: 2
Dragon: 3
Steel: 2
Fairy: 2
-------------
'''