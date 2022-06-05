import random

attacks = { # meh dino's attacks
  "Strike":{"cooldown":0,"power":1,"special":None},
  "Impact":{"cooldown":1,"power":1.5,"special":"Stun"},
  "Rampage":{"cooldown":1,"power":2,"special":"Bypass Armor"},
  "Pounce":{"cooldown":1,"power":2,"special":"Reduce Damage"},
  "Stunning Strike":{"cooldown":1,"power":1,"special":"Stun"},
  "Decelerating Strike":{"cooldown":1,"power":1,"special":"Slow"},
  "Heal":{"cooldown":0,"power":0,"special":"Heal"},
  "Wound":{"cooldown":2,"power":1,"special":"Bleed"},
  "Flock":{"cooldown":3,"power":0,"special":None}, # Improve later! # pokemon attacks
  "Intimidate":{"cooldown":1,"power":0.5,"special":"Reduce Damage"},
  "Tackle":{"cooldown":0, "power": 1, "special":None},
  "Vine Whip":{"cooldown":0, "power": 1, "special":None},
  "Bubble Beam":{"cooldown":0, "power": 1, "special":None},
  "Flamethrower":{"cooldown":1, "power": 1, "special":"Bleed"},
  "Wing Slash":{"cooldown":1, "power": 1, "special":"Stun"},
  "Earthquake":{"cooldown":1, "power": 1.5, "special":None},
  "Dark Pulse":{"cooldown":1, "power": 1.5, "special":"Stun"},
  "Poison Sting":{"cooldown":1, "power": 1, "special":"Bleed"},
  "Thunder Shock":{"cooldown":1, "power":1.5, "special":"Stun"},
  "Blizzard":{"cooldown":1,"power":1.5,"special":"Stun"},
  "Dynamic Punch":{"cooldown":1,"power":1,"special":"Reduce Damage"},
  "Barrier":{"cooldown":1,"power":0.5,"special":"Reduce Damage"},
  "Bug Bite":{"cooldown":1,"power":1,"special":"Bleed"},
  "Rock Slide":{"cooldown":1,"power":1.5,"special":"Stun"},
  "Nightmare":{"cooldown":1,"power":1,"special":"Stun"},
  "Dragon Rage":{"cooldown":2,"power":2.5,"special":"Bypass Armor"},
  "Iron Tail":{"cooldown":1,"power":1.5,"special":"Reduce Damage"}
}

# a dict of default, everywhere dinos
dinos = {
  "Tyrannosaurus Rex":{"lvl":11,"rarity":"Epic","cdna":150,"hp":2164,"dmg":913,"speed":102,"armor":1,"crit":0.3,"attacks":["Strike","Impact","Rampage"]},
  "Velociraptor":{"lvl":1,"rarity":"Common","cdna":50,"hp":487,"dmg":457,"speed":132,"armor":1,"crit":0.05,"attacks":["Strike","Pounce"]},
  "Triceratops":{"lvl":6,"rarity":"Rare","cdna":100,"hp":1243,"dmg":376,"speed":111,"armor":0.8,"crit":0.05,"attacks":["Strike","Stunning Strike"]},
  "Dilophosaurus":{"lvl":6,"rarity":"Rare","cdna":100,"hp":1356,"dmg":489,"speed":124,"armor":1,"crit":0.05,"attacks":["Strike","Impact","Rampage"]},
  "Ankylosaurus":{"lvl":11,"rarity":"Epic","cdna":150,"hp":2236,"dmg":481,"speed":116,"armor":0.7,"crit":0.05,"attacks":["Impact","Heal"]},
  "Brachiosaurus":{"lvl":11,"rarity":"Epic","cdna":150,"hp":2886,"dmg":481,"speed":111,"armor":0.9,"crit":0.3,"attacks":["Strike","Rampage"]},
  "Spinosaurus":{"lvl":6,"rarity":"Rare","cdna":100,"hp":1356,"dmg":376,"speed":122,"armor":1,"crit":0.05,"attacks":["Strike","Impact","Wound"]},
"Stegosaurus":{"lvl":1,"rarity":"Common","cdna":50,"hp":1151,"dmg":295,"speed":116,"armor":0.8,"crit":0.05,"attacks":["Strike","Impact"]}
}

# a dict of japan specific dinos from local area 1
japan_dinos = {
  "Gallimimus":{"lvl":1,"rarity":"Common","cdna":50,"hp":797,"dmg":383,"speed":130,"armor":1,"crit":0.05,"attacks":["Strike","Impact"]},
  "Glyptodon":{"lvl":1,"rarity":"Common","cdna":50,"hp":1151,"dmg":295,"speed":103,"armor":0.6,"crit":0.05,"attacks":["Impact","Rampage"]},
  "Inostrancevia":{"lvl":1,"rarity":"Common","cdna":50,"hp":1151,"dmg":354,"speed":130,"armor":1,"crit":0.05,"attacks":["Strike","Impact"]},
  "Miragaia":{"lvl":1,"rarity":"Common","cdna":50,"hp":885,"dmg":295,"speed":109,"armor":1,"crit":0.05,"attacks":["Decelerating Strike","Heal"]},
  "Amargasaurus":{"lvl":6,"rarity":"Rare","cdna":100,"hp":1978,"dmg":376,"speed":103,"armor":1,"crit":0.05,"attacks":["Decelerating Strike","Impact"]},
  "Giraffatitan":{"lvl":6,"rarity":"Rare","cdna":100,"hp":2148,"dmg":376,"speed":107,"armor":0.9,"crit":0.2,"attacks":["Decelerating Strike","Rampage"]},
  "Megalonyx":{"lvl":6,"rarity":"Rare","cdna":100,"hp":1300,"dmg":452,"speed":103,"armor":1,"crit":0.1,"attacks":["Strike","Rampage"]},
  "Megalosaurus":{"lvl":6,"rarity":"Rare","cdna":100,"hp":1469,"dmg":376,"speed":105,"armor":1,"crit":0.05,"attacks":["Strike","Rampage"]},
  "Preondactylus":{"lvl":6,"rarity":"Rare","cdna":100,"hp":1469,"dmg":376,"speed":105,"armor":1,"crit":0.05,"attacks":["Strike","Rampage"]},
  "Baryonyx":{"lvl":11,"rarity":"Epic","cdna":150,"hp":2020,"dmg":673,"speed":126,"armor":1,"crit":0.3,"attacks":["Strike","Rampage"]},
  "Compsognathus":{"lvl":11,"rarity":"Epic","cdna":150,"hp":1731,"dmg":577,"speed":128,"armor":1,"crit":0.05,"attacks":["Strike","Heal","Pounce"]},
  "Concavenator":{"lvl":11,"rarity":"Epic","cdna":150,"hp":1803,"dmg":553,"speed":106,"armor":1,"crit":0.1,"attacks":["Strike","Impact"]},
  "Sinoceratops":{"lvl":11,"rarity":"Epic","cdna":150,"hp":1587,"dmg":481,"speed":107,"armor":0.75,"crit":0.05,"attacks":["Strike","Stunning Strike","Impact"]}
}

us_dinos = {
  "Euoplocephalus":{"lvl":1,"rarity":"Common","cdna":50,"hp":1063,"dmg":265,"speed":112,"armor":0.6,"crit":0.05,"attacks":["Strike","Rampage"]},
  "Majungasaurus":{"lvl":1,"rarity":"Common","cdna":50,"hp":1018,"dmg":295,"speed":105,"armor":1,"crit":0.05,"attacks":["Strike","Impact"]},
  "Purussaurus Gen 2":{"lvl":1,"rarity":"Common","cdna":50,"hp":1240,"dmg":369,"speed":111,"armor":0.9,"crit":0.2,"attacks":["Strike","Impact"]},
  "Andrewsarchus":{"lvl":6,"rarity":"Rare","cdna":100,"hp":1243,"dmg":527,"speed":125,"armor":1,"crit":0.4,"attacks":["Strike","Impact","Rampage"]},
  "Bajadasaurus":{"lvl":6,"rarity":"Rare","cdna":100,"hp":1639,"dmg":339,"speed":108,"armor":1,"crit":0.05,"attacks":["Strike","Heal","Rampage"]},
  "Baryonyx Gen 2":{"lvl":6,"rarity":"Rare","cdna":100,"hp":1639,"dmg":376,"speed":123,"armor":1,"crit":0.2,"attacks":["Strike","Rampage"]},
  "Nasutoceratops":{"lvl":6,"rarity":"Rare","cdna":100,"hp":1809,"dmg":376,"speed":109,"armor":0.8,"crit":0.05,"attacks":["Decelerating Strike","Stunning Strike"]},
  "Nodosaurus":{"lvl":6,"rarity":"Rare","cdna":100,"hp":1639,"dmg":358,"speed":115,"armor":0.7,"crit":0.05,"attacks":["Decelerating Strike","Impact"]},
  "Wuerhosaurus":{"lvl":6,"rarity":"Rare","cdna":100,"hp":1696,"dmg":376,"speed":115,"armor":0.75,"crit":0.05,"attacks":["Strike","Decelerating Strike"]},
  "Alanqa":{"lvl":11,"rarity":"Epic","cdna":150,"hp":1948,"dmg":577,"speed":125,"armor":1,"crit":0.05,"attacks":["Strike","Rampage"]},
  "Dakotaraptor":{"lvl":11,"rarity":"Epic","cdna":150,"hp":1515,"dmg":577,"speed":129,"armor":1,"crit":0.05,"attacks":["Pounce","Rampage","Wound"]},
  "Pyroraptor":{"lvl":11,"rarity":"Epic","cdna":150,"hp":1515,"dmg":721,"speed":129,"armor":1,"crit":0.05,"attacks":["Strike","Pounce"]},
  "Rajasaurus":{"lvl":11,"rarity":"Epic","cdna":150,"hp":2020,"dmg":481,"speed":104,"armor":1,"crit":0.3,"attacks":["Strike","Rampage","Impact"]},
  "Woolly Mammoth":{"lvl":11,"rarity":"Epic","cdna":150,"hp":2020,"dmg":481,"speed":115,"armor":0.9,"crit":0.3,"attacks":["Strike","Decelerating Strike","Heal"]}
}

india_dinos = {
  "Eremotherium":{"lvl":1,"rarity":"Common","cdna":50,"hp":930,"dmg":310,"speed":102,"armor":1,"crit":0.05,"attacks":["Heal","Rampage"]},
  "Lythronax":{"lvl":1,"rarity":"Common","cdna":50,"hp":1240,"dmg":295,"speed":104,"armor":1,"crit":0.05,"attacks":["Strike","Rampage"]},
  "Phorusrhacos":{"lvl":1,"rarity":"Common","cdna":50,"hp":885,"dmg":442,"speed":130,"armor":1,"crit":0.05,"attacks":["Strike","Wound"]},
  "Sinosauropteryx":{"lvl":1,"rarity":"Common","cdna":50,"hp":797,"dmg":295,"speed":128,"armor":1,"crit":0.1,"attacks":["Strike","Pounce","Flock"]},
  "Archaeopteryx":{"lvl":6,"rarity":"Rare","cdna":100,"hp":1243,"dmg":471,"speed":127,"armor":1,"crit":0.1,"attacks":["Strike","Impact","Rampage","Flock"]},
  "Delta":{"lvl":6,"rarity":"Rare","cdna":100,"hp":904,"dmg":489,"speed":131,"armor":1,"crit":0.05,"attacks":["Strike","Pounce","Impact"]},
  "Edmontosaurus":{"lvl":6,"rarity":"Rare","cdna":100,"hp":1809,"dmg":376,"speed":113,"armor":1,"crit":0.05,"attacks":["Strike","Heal","Impact"]},
  "Fukuisaurus":{"lvl":6,"rarity":"Rare","cdna":100,"hp":1752,"dmg":395,"speed":115,"armor":1,"crit":0.05,"attacks":["Strike","Heal","Impact"]},
  "Moschops":{"lvl":6,"rarity":"Rare","cdna":100,"hp":1696,"dmg":376,"speed":113,"armor":0.75,"crit":0.05,"attacks":["Strike","Decelerating Strike","Impact","Rampage"]},
  "Arcocanthosaurus":{"lvl":11,"rarity":"Epic","cdna":150,"hp":2308,"dmg":817,"speed":103,"armor":1,"crit":0.3,"attacks":["Strike","Impact","Rampage"]},
  "Monolophosaurus":{"lvl":11,"rarity":"Epic","cdna":150,"hp":1443,"dmg":625,"speed":127,"armor":1,"crit":0.05,"attacks":["Strike","Impact","Rampage"]},
  "Pteranodon":{"lvl":11,"rarity":"Epic","cdna":150,"hp":1587,"dmg":432,"speed":127,"armor":1,"crit":0.05,"attacks":["Strike","Impact","Rampage"]},
  "Secodontosaurus":{"lvl":11,"rarity":"Epic","cdna":150,"hp":1875,"dmg":721,"speed":114,"armor":1,"crit":0.05,"attacks":["Strike","Impact","Rampage"]}
}

china_dinos = {
  "Dimorphodon":{"lvl":1,"rarity":"Common","cdna":50,"hp":797,"dmg":147,"speed":128,"armor":1,"crit":0.05,"attacks":["Strike","Wound"]},
  "Monolophosaurus Gen 2":{"lvl":1,"rarity":"Common","cdna":50,"hp":797,"dmg":398,"speed":126,"armor":1,"crit":0.05,"attacks":["Strike","Impact"]},
  "Parasaurolophus":{"lvl":1,"rarity":"Common","cdna":50,"hp":1328,"dmg":354,"speed":106,"armor":1,"crit":0.05,"attacks":["Strike","Heal"]},
  "Scolosaurus":{"lvl":1,"rarity":"Common","cdna":50,"hp":1195,"dmg":295,"speed":107,"armor":0.7,"crit":0.05,"attacks":["Strike","Rampage"]},
  "Compsognathus Gen 2":{"lvl":6,"rarity":"Rare","cdna":100,"hp":1413,"dmg":414,"speed":127,"armor":1,"crit":0.1,"attacks":["Strike","Pounce","Impact","Flock"]},
  "Diplocaulus Gen 2":{"lvl":6,"rarity":"Rare","cdna":100,"hp":1526,"dmg":376,"speed":125,"armor":1,"crit":0.05,"attacks":["Strike","Impact"]},
  "Elasmotherium":{"lvl":6,"rarity":"Rare","cdna":100,"hp":1696,"dmg":471,"speed":108,"armor":0.7,"crit":0.05,"attacks":["Strike","Impact","Rampage"]},
  "Postosuchus":{"lvl":6,"rarity":"Rare","cdna":100,"hp":1130,"dmg":452,"speed":126,"armor":1,"crit":0.2,"attacks":["Strike","Heal"]},
  "Ouranosaurus":{"lvl":11,"rarity":"Epic","cdna":150,"hp":1731,"dmg":721,"speed":104,"armor":1,"crit":0.05,"attacks":["Strike","Heal"]},
  "Pachycephalosaurus":{"lvl":11,"rarity":"Epic","cdna":150,"hp":1875,"dmg":577,"speed":121,"armor":1,"crit":0.05,"attacks":["Strike","Decelerating Strike","Impact","Rampage"]},
  "Stygimoloch":{"lvl":11,"rarity":"Epic","cdna":150,"hp":1515,"dmg":721,"speed":129,"armor":1,"crit":0.05,"attacks":["Strike","Impact"]},
  "Troodon":{"lvl":11,"rarity":"Epic","cdna":150,"hp":1443,"dmg":577,"speed":130,"armor":1,"crit":0.05,"attacks":["Strike","Pounce","Rampage"]}
}

# all the dinos
all_dinos = {**dinos, **japan_dinos, **us_dinos, **india_dinos, **china_dinos}


def info(dino_name):
  return all_dinos[dino_name]

def get_dino(rarity):
  while True:
    name = random.choice(list(dinos))
    dino = dinos[name]
    if dino["rarity"] == rarity:
      return name,dino

def battle_info(move):
  return attacks[move]