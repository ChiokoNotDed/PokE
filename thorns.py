from functions import affirm, clear, pause
from replit import db
def ThornPalace():
  global Escape
  clear()
  print(f"You walk up to Thorn Palace, your {db['PokemonName']} by your side. ")
  pause(1.5)
  if db['Thorns'] == True:
          print('You enter the palace and walk to the throne room.')
          pause(1.5)
          print("Leafeon jump's down from it's throne and confronts you.")
          pause(1.5)
          clear()
          Tips()
  else:
          print('There is a massive grand door in front of you, covered in vines and thorns. ')
          pause(1.5)
          print(f"Your {db['PokemonName']} sniffs at the door and doesn't seem to sense anything awry" )
          pause(1.5)
          print('To enter the palace, you must answer a riddle....')
          pause(1.5)
          affirm()
          clear()
          guess = ''
          while (guess.strip()).lower() != "plant" and  (guess.strip()).lower() != "plants" and (guess.strip()).lower() != "flower" and (guess.strip()).lower() != "flowers":
            print("You bury me when i'm alive, and dig me up when I die. What am I?  ")
            guess = input()
            clear()
          print('You are granted access into Thorn Palace. ')
          affirm()
          clear()
          print('The thorns unravel from the door and the gates swing open. ')
          pause(1)
          print('You are greeted by a group of Snivy. They say you must prove your Pokemon Knowledge before you can advance. ')
          affirm()
          answer = ''
          while (answer.strip()).lower() != 'leafeon':
            print('What is the grass type evolution of Eevee?')
            answer = input()
            clear()
          print(f"The Snivys are satisfied and make way for you and {db['PokemonName']}")
          pause(1)
          print('A Serperior pops out and challenges you!')
          from encounter import BPencounter
          affirm()
          clear()
          BPencounter()
          clear()
          if db['EeveeHP'] < 1:
                Escape()
          if db['EeveeHP'] > 1:
                  print(f"All the pokemon surrounding you shrink away from you, scared after that display of {db['PokemonName']}'s power.")
                  pause(2)
                  print("However, one timid Treeko crawls to you and heals your Eevee for you.")
                  db['EeveeHP'] = db['EeveeLv'] * 2
                  affirm()
                  clear()
                  print("You see 2 doors. You walk up and start thinking. Which door do you want to go through?\n",
                "(1) Right door\n",
                "(2) Left door\n")
                  Door1 = input("Choose a door: ")
                  if Door1=="1":
                    print("You went through the right door...") 
                    pause(1)
                    print("You see Leafeon standing on a vine entangled thrown.")
                    pause(1)
                    print("It jumps down, it wants to prove your skill in battle")
                    from encounter import BPencounter2
                    affirm()
                    clear()
                    BPencounter2()
                    clear()
                    if db['EeveeHP'] < 1:
                            Escape()
                    if db['EeveeHP'] > 0:
                            db['Tip'] = 1
                            db['Thorns'] = True
                            db['Area'].append('Big Blue')
                            print("Leafeon looks at you with hope in it's eyes.")
                            pause(1.5)
                            print("It takes you to a room full of treasure and picks up a lemon shaped staff.")
                            pause(1.5)
                            print("It hands you the staff...")
                            pause(1.5)
                            clear()
                            print("[Leafeon] Hello? Can you hear me?")
                            affirm()
                            clear()
                            print("[Leafeon] Yes? That's good, the staff has strange ability's such as understanding pokemon.")
                            affirm()
                            clear()
                            print("[Leafeon] It will be very usefull for your journey.")
                            affirm()
                            clear()
                            print("[Leafeon] Oh! I forgot to tell you about your journey!")
                            affirm()
                            clear()
                            print("[Leafeon] I'm sending you on a journey. You see, there has been a disturbance, my friend Espeon hasn't contacted me for weeks. I fear that something bad has happened.")
                            affirm()
                            clear()
                            print("[Leafeon] Espeon was contacting me via telekinesis about the 19 Ultimate pokemon. The Ultimate pokemon seem to be causing mass distruction everywhere they go.")
                            affirm()
                            clear()
                            print(f"[Leafeon] Now, your pretty strong with that {db['PokemonName']} of your's.")
                            affirm()
                            clear()
                            print("[Leafeon] I believe you have the strength to take down these Ultimate pokemon, thats why i'm sending you on this journey.")
                            affirm()
                            clear()
                            print("[Leafeon] You have no say in the matter, if you don't go, these pokemon will destroy the Ultrae Region!")
                            affirm()
                            clear()
                            print("[Leafeon] Now, the first place you should go is Big Blue, a city engulfed in water, find Vaporeon and ask him for access to his travel charm. Your going to need it to get to Vaporion will tell you where to go then.")
                            affirm()
                            clear()
                            print("[Leafeon] I'll open up the path to Big Blue, it shouldn't take long for you to get there.")
                            affirm()
                            clear()
                            print("[Leafeon] Now go! The future of Ultrae is counting on you!")
                            Lemon=True
                            affirm()
                            clear()
                            Escape()
                  else:
                    print("You found a secret treasure room...")
                    pause(1.5)
                    print("Snivys and bulbasaurs start surrounding you.")
                    pause(1.5)
                    print("They kicked you out.")
                    pause(1)
                    affirm()
                    clear()
                    Escape()

def Tips(): # This is for tip's, Like when your stuck and need help
        print('[Leafeon] Do you need anything?')
        print('')
        print('(1) Help\n(2) Back')
        print('')
        Tip = input("")
        if Tip == "2":
                clear()
                print('[Leafeon] Ok then.')
                affirm()
                clear()
                Escape()
        elif Tip == "1":
                clear()
                if db['Tip'] == 1:
                        clear()
                        print("[Leafeon] You should go to Big Blue, the water city, it's not very far from here.")
                        affirm()
                        clear()
                        Escape()
                elif db['Salve'] == 6:
                  print('[Leafeon] Ah Yes. You are now ready to go to your first challenging area. I am opening up Unstable Labratory. Good Luck. ')
                  db['Tip'] = False
                  affirm()
                  clear()
                elif db['Tip'] == 2:
                        print("[Leafeon] Oh no! Vaporeon is sick? Well, it seems he should need a Revival Herb. Here, give this to him. ")
                        db['Salve'] = True
                        db['Tip'] = False
                        affirm()
                        clear()
                
                else:
                        print("[Leafeon] Uh, I don't think I can help you here.")
                        affirm()
                        clear()
                        Escape()
        else:
                clear()
                Tips()
def Escape():
  clear()
  
    
  
  
  
        
  