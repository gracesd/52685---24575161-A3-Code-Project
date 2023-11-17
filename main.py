# Hi there! This is the source code for my RPG game 'Fading Vale'. 

#MODULES#
import sys
import os
import time
import random

screen_width = 100

# Player Setup #
class player:
  def __init__(self, hp, location, name='', attack_power=0):
    self.name = ' '
    self.hp = hp
    self.attack_power = attack_power
    self.location = location
    self.game_over = False
myPlayer = player(hp=50, location='B2: Town Outskirts', name='', attack_power=20)



###############################################################################################

# Enemy Setup #
class Enemy:
  def __init__(self, name, hp, attack_power, defense, attack_damage=0):
    self.name = name
    self.hp = hp
    self.attack_power = attack_power
    self.defense = defense
    self.attack_damage = attack_damage
witch = Enemy('witch', 20, 5, 10)
wyvern = Enemy('wyvern', 50, 15, 20)
ogre = Enemy('ogre', 15, 5, 10)
spider = Enemy('spider', 15, 20, 15)
siren = Enemy('siren', 10, 10, 10)
angry_bandit = Enemy('angry_bandit', 10, 5, 5)

###########WITCH###########
def witch_battle(player, witch):
  print("You open the door to the hut cautiously.")
  time.sleep(2)
  print(f'You encountered a {witch.name}!')
  time.sleep(2)
  print(f'The {witch.name} turns to you, lifting her hands up and preparing for battle!')
  time.sleep(2)
  print("You get the first move, act quickly!"+ '\n')
  time.sleep(2)
  print(" ########################################")
  print(" #                                      #")
  print(" #               /\                     #")
  print(" #            __/__\__                  #")
  print(" #            ))|  |((                  #")
  print(" #           _-- \/ --_                 #")
  print(" #           |   |    |                 #")
  print(" #            \   /  /                  #")
  print(" #            |  /   /|                 #")
  print(" #      v=====w=O|    \========<<<<<<   #")
  print(" #      |       | |    |                #")
  print(" #     / \        \ \   \               #")
  print(" #     [_]         \ \  |               #")
  print(" #                 <___/                #")
  print(" #                                      #")
  print(" ########################################" + '\n')
  time.sleep(2)

  # Ask user if they want to fight or run #
  print('"Do you want to FIGHT or RUN?"')
  user_input = input("> ").upper()
  while user_input not in ['FIGHT', 'RUN']:
    print("Unable to find response. Please try again.")
    time.sleep(2)
    print('"Do you want to FIGHT or RUN?"')
    user_input = input("> ").upper()
  if user_input in ['FIGHT']:
    print('"Prepare for battle! Be careful!"' + '\n')
    time.sleep(2)
    print("You ready your sword.")

    while witch.hp > 0:

    # randomised attack system for PLAYER! #
      player.attack_damage = random.randint(1, player.attack_power)
      player.attack_text = ' '
      if player.attack_damage <= 5:
        player.attack_text = 'weak'
      elif player.attack_damage <= 10:
        player.attack_text = 'moderate'
      elif player.attack_damage <= 15:
        player.attack_text = 'strong'
      else:
        player.attack_text = 'very strong'

      print(f'You attack the Witch for {player.attack_damage} damage!')
      time.sleep(2)

      if player.attack_text == 'weak':
        print("The Witch cackles as she jumps out of the way.")
        time.sleep(2)
      elif player.attack_text  == 'moderate':
        print("The witch screeches as you stab at her ankles!")
        time.sleep(2)
      elif player.attack_text  == 'strong':
        print("Your sword slices a chunk out of her shoulder as she screams!")
        time.sleep(2)
      elif player.attack_text  == 'very strong':
        print("The Witch looks extremely weak!")
        time.sleep(2)

    # calculate witch current HP
      witch.hp -= player.attack_damage
      print(f'The {witch.name} has {witch.hp} health remaining!'+ '\n')
      time.sleep(2)

    # check witch HP!
      if witch.hp <= 0:
        print(f'You defeated the {witch.name}!'+'\n')
        time.sleep(2)
        break

    # randomised attack system for WITCH! #
      witch.attack_damage = random.randint(1,5)

      witch_attack_text = ''

      if witch.attack_damage == 1:
        witch_attack_text = 'negligible'
      elif witch.attack_damage == 2:
        witch_attack_text = 'weak'
      elif witch.attack_damage == 3:
        witch_attack_text = 'moderate'
      elif witch.attack_damage == 4:
        witch_attack_text = 'strong'
      else:
        witch_attack_text = 'very strong'

      print(f'The {witch.name} blasts magic at you for {witch.attack_damage} damage!')
      time.sleep(2)
      if witch_attack_text == 'negligible':
        print("You don't feel a thing.")
        time.sleep(2)
      elif witch_attack_text == 'weak':
        print("Ouch! You'll be okay.")
        time.sleep(2)
      elif witch_attack_text == 'moderate':
        print("That hurt! Keep your head up!")
        time.sleep(2)
      elif witch_attack_text == 'strong':
        print("That hurt a lot!")
        time.sleep(2)
      elif witch_attack_text== 'very strong':
        print("You groan in pure pain, bracing yourself.")
        time.sleep(2)

    # calculate remaining player HP:
      player.hp -= witch.attack_damage
      print('\n'+"#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#")
      print(f'# You have {player.hp} health remaining. #')
      print("#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#"+'\n')
      time.sleep(2)

      if player.hp <=0:
        print('"You have been defeated."')
        time.sleep(2)
        print('Thank you for playing my game!')
        time.sleep(2)
        print('"Better luck next time..."')
        time.sleep(2)
        sys.exit()

  #RUN option:
  elif user_input in ['RUN']:
    print("You flee from the battle." + '\n')
    time.sleep(2)

###########WYVERN###########
def wyvern_battle(player, wyvern):
  print("You walk into the cavern.")
  time.sleep(2)
  print(f'You encountered a {wyvern.name}!')
  time.sleep(2)
  print(f'The {wyvern.name} hisses at you as it steps off its treasure pile.')
  time.sleep(2)
  print("It glares down at you, it's sharp teeth flashing." + '\n')
  time.sleep(2)
  print(" ########################################")
  print(" #                                      #")
  print(" #           _/\ /\                     #")
  print(" #        __/  - /_  =>                 #")
  print(" #      [. .]     O  \        {_______- #")
  print(" #       -v-v-v\  \   |       /  \ __/v #")
  print(" #  >>>   M__M / /    \     / \__/ v    #")
  print(" #         \-----/       \__/  /v       #")
  print(" #               \  \\        /          #")
  print(" #                | //       \     |^   #")
  print(" #                { w  /     _  \  /\   #")
  print(" #                 \ |      /   \_/ |   #")
  print(" #                    \__  /__     /    #")
  print(" #                    __/  \  \___/     #")
  print(" #                 d_d___/\|            #")
  print(" ########################################" + '\n')
  time.sleep(2)

# Ask user if they want to fight or run #
  print('"Do you want to FIGHT or RUN?"')
  user_input = input("> ").upper()
  while user_input not in ['FIGHT', 'RUN']:
    print("Unable to find response. Please try again.")
    time.sleep(2)
    print('"Do you want to FIGHT or RUN?"')
    user_input = input("> ").upper()
  if user_input in ['FIGHT']:
    print('"Prepare for battle! Be careful!"' + '\n')
    time.sleep(2)
    print("You ready your sword.")

    while wyvern.hp > 0: 

  # randomised attack system for PLAYER! #
      player.attack_damage = random.randint(1,player.attack_power)
      attack_text = ' '
      if player.attack_damage <= 5:
        attack_text = 'weak'
      elif player.attack_damage <= 10:
        attack_text = 'moderate'
      elif player.attack_damage <= 15:
        attack_text = 'strong'
      else:
        attack_text = 'very strong'
      print(f'You attack the Wyvern for {player.attack_damage} damage!')
      time.sleep(2)

      if attack_text == 'weak':
        print("The Wyvern barely seems to notice your attack!")
        time.sleep(2)
      elif attack_text  == 'moderate':
        print("The great beast roars and stomps closer!")
        time.sleep(2)
      elif attack_text  == 'strong':
        print("Your sword cuts through the scales slightly, greatly injuring the Wyvern!")
        time.sleep(2)
      elif attack_text  == 'very strong':
        print("You slash a deep cut in the Wyvern's abdomen as it screeches in pain!")
        time.sleep(2)

  # calculate wyvern current HP
      wyvern.hp -= player.attack_damage
      print(f'The {wyvern.name} has {wyvern.hp} health remaining!'+ '\n')
      time.sleep(2)

  # check wyvern HP!
      if wyvern.hp <= 0:
        print(f'You defeated the {wyvern.name}!'+'\n')
        time.sleep(2)
        break

  # randomised attack system for WYVERN! #
      wyvern.attack_damage = random.randint(1,15)

      wyvern_attack_text = ''

      if wyvern.attack_damage <= 3:
        wyvern_attack_text = 'negligible'
      elif wyvern.attack_damage <=6:
        wyvern_attack_text = 'weak'
      elif wyvern.attack_damage <=9 :
        wyvern_attack_text = 'moderate'
      elif wyvern.attack_damage <= 12:
        wyvern_attack_text = 'strong'
      else:
        wyvern_attack_text = 'very strong'

      print(f'The {wyvern.name} breathes fire at you, dealing {wyvern.attack_damage} damage!')
      time.sleep(2)
      if wyvern_attack_text == 'negligible':
        print("You don't feel a thing.")
        time.sleep(2)
      elif wyvern_attack_text == 'weak':
        print("Ouch! You'll be okay.")
        time.sleep(2)
      elif wyvern_attack_text == 'moderate':
        print("That hurt! Keep your head up!")
        time.sleep(2)
      elif wyvern_attack_text == 'strong':
        print("That hurt a lot!")
        time.sleep(2)
      elif wyvern_attack_text== 'very strong':
        print("You groan in pure pain, bracing yourself.")
        time.sleep(2)

  # calculate remaining player HP:
      player.hp -= wyvern.attack_damage
      print(f'You have {player.hp} health remaining.'+ '\n')
      time.sleep(2)

      if player.hp <=0:
        print('"You have been defeated."')
        time.sleep(2)
        print('Thank you for playing my game!')
        time.sleep(2)
        print('"Better luck next time..."')
        time.sleep(2)
        sys.exit()

  #RUN option:
  elif user_input in ['RUN']:
    print("You flee from the battle."+'\n')
    time.sleep(2)

###########OGRE###########
def ogre_battle(player, ogre):
  print(f'Suddenly, the {ogre.name} turns to face you.')
  time.sleep(2)
  print("He yells, slobber exploding from his lips as he lobs his club above his head." + '\n')
  time.sleep(2)
  print(" ########################################")
  print(" #                                      #")
  print(" #                                      #")
  print(" #                                      #")
  print(" #                                      #")
  print(" #                                      #")
  print(" #          /|___|\                     #")
  print(" #         / _^ ^_  \                   #")
  print(" #      {// .@| |@. \\}                 #")
  print(" #       \   <._.>   /                  #")
  print(" #        \^^-v-v-^^/        _-_.       #")
  print(" #       _-[_______]-_     ./ . /       #")
  print(" #      /     \ /     \    /  ./.       #")
  print(" #     |  |        |   |  /. ./         #")
  print(" #     |  /         \  | /  ./          #")
  print(" ########################################" + '\n')
  time.sleep(2)

  # Ask user if they want to fight or run #
  print('"Do you want to FIGHT or RUN?"')
  user_input = input("> ").upper()
  while user_input not in ['FIGHT', 'RUN']:
    print("Unable to find response. Please try again.")
    time.sleep(2)
    print('"Do you want to FIGHT or RUN?"')
    user_input = input("> ").upper()
  if user_input in ['FIGHT']:
    print('"Prepare for battle! Be careful!"' + '\n')
    time.sleep(2)
    print("You ready your sword.")

    while ogre.hp > 0:

  # randomised attack system for PLAYER! #
      player.attack_damage = random.randint(1, player.attack_power)
      player.attack_text = ' '
      if player.attack_damage <= 5:
        player.attack_text = 'weak'
      elif player.attack_damage <= 10:
        player.attack_text = 'moderate'
      elif player.attack_damage <= 15:
        player.attack_text = 'strong'
      else:
        player.attack_text = 'very strong'
      print(f'You attack the Ogre for {player.attack_damage} damage!')
      time.sleep(2)

      if player.attack_text == 'weak':
        print("You barely manage to land a hit, as the Ogre groans quietly.")
        time.sleep(2)
      elif player.attack_text  == 'moderate':
        print("The Ogre roars!")
        time.sleep(2)
      elif player.attack_text  == 'strong':
        print("Your sword cuts clean through the Ogre's light armour and cuts his chest.")
        time.sleep(2)
      elif player.attack_text  == 'very strong':
        print("The Ogre looks extremely weak!")
        time.sleep(2)



  # calculate ogre current HP
      ogre.hp -= player.attack_damage
      print(f'The {ogre.name} has {ogre.hp} health remaining!'+ '\n')
      time.sleep(2)

  # check ogre HP!
      if ogre.hp <= 0:
        print(f'You defeated the {ogre.name}!'+'\n')
        time.sleep(2)
        break

  # randomised attack system for OGRE! #
      ogre.attack_damage = random.randint(1,5)

      ogre_attack_text = ''

      if ogre.attack_damage == 1:
        ogre_attack_text = 'negligible'
      elif ogre.attack_damage == 2:
        ogre_attack_text = 'weak'
      elif ogre.attack_damage == 3:
        ogre_attack_text = 'moderate'
      elif ogre.attack_damage == 4:
        ogre_attack_text = 'strong'
      else:
        ogre_attack_text = 'very strong'

      print(f'The {ogre.name} swings his club, hitting you for' + f' {ogre.attack_damage} damage!')
      time.sleep(2)

  # calculate remaining player HP:
      player.hp -= ogre.attack_damage
      print('\n'+"#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#")
      print(f'# You have {player.hp} health remaining. #')
      print("#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#"+'\n')
      time.sleep(2)
      if player.hp <=0:
        print('"You have been defeated."')
        time.sleep(2)
        print('Thank you for playing my game!')
        time.sleep(2)
        print('"Better luck next time..."')
        time.sleep(2)
        sys.exit()

  #RUN option:
  elif user_input in ['RUN']:
    print("You flee from the battle." + '\n')
    time.sleep(2)

###########SPIDER###########
def spider_battle(player, spider):
  print(f'Mist begins to surround you.')
  time.sleep(2)
  print("From somewhere within the fog, you here a scratching sound.")
  time.sleep(2)
  print("As chills run down your spine, the sillhouette of a large arachnid crawls closer.")
  time.sleep(2)
  print("The spider hisses, it's huge, hairy black legs towering above you!" + '\n')
  time.sleep(2)
  print(" ########################################")
  print(" #                                      #")
  print(" #                                      #")
  print(" #                                      #")
  print(" #                                      #")
  print(" #                                      #")
  print(" #                                      #")
  print(" #         _-\              /-_         #")
  print(" #        / ^\\ __------__ //^\          #")
  print(" #       / /\ \| O o  o O | /\ \        #")
  print(" #      / /^^\  \ Vv--vV / /^^\ \       #")
  print(" #     / //  \\ |-\/-\/-|//   \\ \       #")
  print(" #   <<_//    \\_\______///    \\_>>     #")
  print(" #   <<_v                       v_>>    #")
  print(" #                                      #")
  print(" ########################################" + '\n')
  time.sleep(2)

  # Ask user if they want to fight or run #
  print('"Do you want to FIGHT or RUN?"')
  user_input = input("> ").upper()
  while user_input not in ['FIGHT', 'RUN']:
    print("Unable to find response. Please try again.")
    time.sleep(2)
    print('"Do you want to FIGHT or RUN?"')
    user_input = input("> ").upper()
  if user_input in ['FIGHT']:
    print('"Prepare for battle! Be careful!"' + '\n')
    time.sleep(2)
    print("You ready your sword.")

    while spider.hp > 0:

  # randomised attack system for PLAYER! #
      player.attack_damage = random.randint(1, player.attack_power)
      player.attack_text = ' '
      if player.attack_damage <= 5:
        player.attack_text = 'weak'
      elif player.attack_damage <= 10:
        player.attack_text = 'moderate'
      elif player.attack_damage <= 15:
        player.attack_text = 'strong'
      else:
        player.attack_text = 'very strong'

      print(f'You attack the Spider for {player.attack_text} damage!')
      time.sleep(2)
      if player.attack_text == 'weak':
        print("You barely manage to land a hit, just scraping the spider's leg.")
        time.sleep(2)
      elif player.attack_text == 'moderate':
        print("The spider hisses as you land a decent hit on it's abdomen.")
        time.sleep(2)
      elif player.attack_text == 'moderate':
        print("Your sword finds a groove underneath the spider's tough shell, stabbing it hard!")
        time.sleep(2)
      elif player.attack_text == 'very strong':
        print("You cut the spider's leg off perfectly, slicing through the flesh.")
        time.sleep(2)

  # calculate spider current HP
      spider.hp -= player.attack_damage
      print(f'The {spider.name} has {spider.hp} health remaining!'+ '\n')
      time.sleep(2)

  # check spider HP!
      if spider.hp <= 0:
        print(f'You defeated the {spider.name}!'+'\n')
        time.sleep(2)
        break

  # randomised attack system for SPIDER! #
      spider.attack_damage = random.randint(1,20)

      spider_attack_text = ''

      if spider.attack_damage <= 4:
        spider_attack_text = 'negligible'
      elif spider.attack_damage <= 8:
        spider_attack_text = 'weak'
      elif spider.attack_damage <= 12:
        spider_attack_text = 'moderate'
      elif spider.attack_damage <= 16:
        spider_attack_text = 'strong'
      else:
        spider_attack_text = 'very strong'

      print(f'The {spider.name} hisses, spitting a chunk of acid at you. It burns! You take {spider.attack_damage} damage!')
      time.sleep(2)
      if spider_attack_text == 'negligible':
        print("You barely feel a thing.")
        time.sleep(2)
      elif spider_attack_text == 'weak':
        print("Ouch! You'll be okay.")
        time.sleep(2)
      elif spider_attack_text == 'moderate':
        print("That hurt! Keep your head up!")
        time.sleep(2)
      elif spider_attack_text == 'strong':
        print("That hurt a lot!")
        time.sleep(2)
      elif spider_attack_text== 'very strong':
        print("You groan in pure pain, bracing yourself.")
        time.sleep(2)

  # calculate remaining player HP:
      player.hp -= spider.attack_damage
      print('\n'+"#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#")
      print(f'# You have {player.hp} health remaining. #')
      print("#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#"+'\n')
      time.sleep(2)
      if player.hp <=0:
        print('"You have been defeated."')
        time.sleep(2)
        print('Thank you for playing my game!')
        time.sleep(2)
        print('Better luck next time...')
        time.sleep(2)
        sys.exit()

  #RUN option:
  elif user_input in ['RUN']:
    print("You flee from the battle." + '\n')
    time.sleep(2)

###########SIREN###########
def siren_battle(player, siren):
  print(f'As your ship moves closer to the wreckage, the figure becomes clearer and clearer.')
  time.sleep(2)
  print("You watch as she sobs, staring straight at you as the sound of anguished singing fills your ears")
  time.sleep(2)
  print("You are almost comforted by her voice, but snap back awake as you realise what's happening!")
  time.sleep(2)
  print("Your ship stops right next to the wreck, as you step across the gap and board the haunted ship."+ '\n')
  time.sleep(2)
  print(" ########################################")
  print(" #                                      #")
  print(" #                                      #")
  print(" #            /  .    .  \              #")
  print(" #           _|===^\/^===|_             #")
  print(" #          //=-__ == __-=\\            #")
  print(" #          ||{ [@\  /@] }||            #")
  print(" #          //{\. <..> ./}\\            #")
  print(" #          ||\ \ <ww> / /||            #")
  print(" #          ||/  \----/  \||            #")
  print(" #         _w_---______---_w_           #")
  print(" #        /   |__      __|   \          #")
  print(" #       |   \/  \\\///  \/   |         #")
  print(" #       |    \__/----\__/    |         #")
  print(" #       |    \||||||||||/    |         #")
  print(" ########################################" + '\n')
  time.sleep(2)

  # Ask user if they want to fight or run #
  print('"Do you want to FIGHT or RUN?"')
  user_input = input("> ").upper()
  while user_input not in ['FIGHT', 'RUN']:
    print("Unable to find response. Please try again.")
    time.sleep(2)
    print('"Do you want to FIGHT or RUN?"')
    user_input = input("> ").upper()
  if user_input in ['FIGHT']:
    print('"Prepare for battle! Be careful!"' + '\n')
    time.sleep(2)
    print("You ready your sword.")

    while siren.hp > 0:

  # randomised attack system for PLAYER! #
      player.attack_damage = random.randint(1, player.attack_power)
      player.attack_text = ' '
      if player.attack_damage <= 5:
        player.attack_text = 'weak'
      elif player.attack_damage <= 10:
        player.attack_text = 'moderate'
      elif player.attack_damage <= 15:
        player.attack_text = 'strong'
      else:
        player.attack_text = 'very strong'

      print(f'You attack the Siren for {player.attack_damage} damage!')
      time.sleep(2)
      if player.attack_text == 'weak':
        print("She slips out of the way, your sword scraping her scaly arm.")
        time.sleep(2)
      elif player.attack_text == 'moderate':
        print("You catch her off guard, slicing her shoulder.")
        time.sleep(2)
      elif player.attack_text == 'strong':
        print("You ram your blade into her ribs, piercing through the scales!")
        time.sleep(2)
      elif player.attack_text == 'very strong':
        print("Your blade glides through the air smoothly as you cut her deep, watching her screech.")
        time.sleep(2)

  # calculate siren current HP
      siren.hp -= player.attack_damage
      print(f'The {siren.name} has {siren.hp} health remaining!'+ '\n')
      time.sleep(2)

  # check siren HP!
      if siren.hp <= 0:
        print(f'You defeated the {siren.name}!'+'\n')
        time.sleep(2)
        break

  # randomised attack system for SPIDER! #
      siren.attack_damage = random.randint(1,10)

      siren_attack_text = ''

      if siren.attack_damage == 1:
        siren_attack_text = 'negligible'
      elif siren.attack_damage == 2:
        siren_attack_text = 'weak'
      elif siren.attack_damage == 3:
        siren_attack_text = 'moderate'
      elif siren.attack_damage == 4:
        siren_attack_text = 'strong'
      else:
        siren_attack_text = 'very strong'

      print(f'The Siren screams, blood curdling and ear splitting. Your head spins as you take {siren.attack_damage} damage!')
      time.sleep(2)
      if siren_attack_text == 'negligible':
        print("You barely feel a thing.")
        time.sleep(2)
      elif siren_attack_text == 'weak':
        print("Ouch! You'll be okay.")
        time.sleep(2)
      elif siren_attack_text == 'moderate':
        print("That hurt! Keep your head up!")
        time.sleep(2)
      elif siren_attack_text == 'strong':
        print("That hurt a lot!")
        time.sleep(2)
      elif siren_attack_text== 'very strong':
        print("You groan in pure pain, bracing yourself.")
        time.sleep(2)

  # calculate remaining player HP:
      player.hp -= siren.attack_damage
      print(f'You have {player.hp} health remaining.'+ '\n')
      time.sleep(2)
      if player.hp <=0:
        print('"You have been defeated."')
        time.sleep(2)
        print('Thank you for playing my game!')
        time.sleep(2)
        print('Better luck next time...')
        time.sleep(2)
        sys.exit()

  #RUN option:
  elif user_input in ['RUN']:
    print("You flee from the battle." + '\n')
    time.sleep(2)

###########SIREN###########
def siren_battle(player, siren):
  print(f'As your ship moves closer to the wreckage, the figure becomes clearer and clearer.')
  time.sleep(2)
  print("You watch as she sobs, staring straight at you as the sound of anguished singing fills your ears")
  time.sleep(2)
  print("You are almost comforted by her voice, but snap back awake as you realise what's happening!")
  time.sleep(2)
  print("Your ship stops right next to the wreck, as you step across the gap and board the haunted ship."+ '\n')
  time.sleep(2)
  print(" ########################################")
  print(" #                                      #")
  print(" #                                      #")
  print(" #            /  .    .  \              #")
  print(" #           _|===^\/^===|_             #")
  print(" #          //=-__ == __-=\\            #")
  print(" #          ||{ [@\  /@] }||            #")
  print(" #          //{\. <..> ./}\\            #")
  print(" #          ||\ \ <ww> / /||            #")
  print(" #          ||/  \----/  \||            #")
  print(" #         _w_---______---_w_           #")
  print(" #        /   |__      __|   \          #")
  print(" #       |   \/  \\\///  \/   |         #")
  print(" #       |    \__/----\__/    |         #")
  print(" #       |    \||||||||||/    |         #")
  print(" ########################################" + '\n')
  time.sleep(2)

  # Ask user if they want to fight or run #
  print('"Do you want to FIGHT or RUN?"')
  user_input = input("> ").upper()
  while user_input not in ['FIGHT', 'RUN']:
    print("Unable to find response. Please try again.")
    time.sleep(2)
    print('"Do you want to FIGHT or RUN?"')
    user_input = input("> ").upper()
  if user_input in ['FIGHT']:
    print('"Prepare for battle! Be careful!"' + '\n')
    time.sleep(2)
    print("You ready your sword.")

    while siren.hp > 0:

  # randomised attack system for PLAYER! #
      player.attack_damage = random.randint(1, player.attack_power)
      player.attack_text = ' '
      if player.attack_damage <= 5:
        player.attack_text = 'weak'
      elif player.attack_damage <= 10:
        player.attack_text = 'moderate'
      elif player.attack_damage <= 15:
        player.attack_text = 'strong'
      else:
        player.attack_text = 'very strong'

      print(f'You attack the Siren for {player.attack_damage} damage!')
      time.sleep(2)
      if player.attack_text == 'weak':
        print("She slips out of the way, your sword scraping her scaly arm.")
        time.sleep(2)
      elif player.attack_text == 'moderate':
        print("You catch her off guard, slicing her shoulder.")
        time.sleep(2)
      elif player.attack_text == 'strong':
        print("You ram your blade into her ribs, piercing through the scales!")
        time.sleep(2)
      elif player.attack_text == 'very strong':
        print("Your blade glides through the air smoothly as you cut her deep, watching her screech.")
        time.sleep(2)

  # calculate siren current HP
      siren.hp -= player.attack_damage
      print(f'The {siren.name} has {siren.hp} health remaining!'+ '\n')
      time.sleep(2)

  # check siren HP!
      if siren.hp <= 0:
        print(f'You defeated the {siren.name}!'+'\n')
        time.sleep(2)
        break

  # randomised attack system for SPIDER! #
      siren.attack_damage = random.randint(1,10)

      siren_attack_text = ''

      if siren.attack_damage == 1:
        siren_attack_text = 'negligible'
      elif siren.attack_damage == 2:
        siren_attack_text = 'weak'
      elif siren.attack_damage == 3:
        siren_attack_text = 'moderate'
      elif siren.attack_damage == 4:
        siren_attack_text = 'strong'
      else:
        siren_attack_text = 'very strong'

      print(f'The Siren screams, blood curdling and ear splitting. Your head spins as you take {siren.attack_damage} damage!')
      time.sleep(2)
      if siren_attack_text == 'negligible':
        print("You barely feel a thing.")
        time.sleep(2)
      elif siren_attack_text == 'weak':
        print("Ouch! You'll be okay.")
        time.sleep(2)
      elif siren_attack_text == 'moderate':
        print("That hurt! Keep your head up!")
        time.sleep(2)
      elif siren_attack_text == 'strong':
        print("That hurt a lot!")
        time.sleep(2)
      elif siren_attack_text== 'very strong':
        print("You groan in pure pain, bracing yourself.")
        time.sleep(2)

  # calculate remaining player HP:
      player.hp -= siren.attack_damage
      print('\n'+"#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#")
      print(f'# You have {player.hp} health remaining. #')
      print("#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#"+'\n')
      time.sleep(2)
      if player.hp <=0:
        print('"You have been defeated."')
        time.sleep(2)
        print('Thank you for playing my game!')
        time.sleep(2)
        print('Better luck next time...')
        time.sleep(2)
        sys.exit()

  #RUN option:
  elif user_input in ['RUN']:
    print("You flee from the battle." + '\n')
    time.sleep(2)

###########ANGRY_BANDIT###########
def angry_bandit_battle(player, angry_bandit):
  print("The biggest of the bandits hears you move closer, turning to face you.")
  time.sleep(2)
  print(f'"Hey!", he yells. "Intruder alert!"')
  time.sleep(2)
  print(f'The Bandit stands up, pulling out a dull blade and pointing it at you.')
  time.sleep(2)
  print("The other bandits don't even move. It seems like he is merely annoying them." + '\n')
  time.sleep(2)
  print(" ########################################")
  print(" #                                      #")
  print(" #                ....______.m_m        #")
  print(" #                \________|/|||==]     #")
  print(" #          ___----___     \W_W         #")
  print(" #         / >>\  /<< \     ===         #")
  print(" #        [| .[]--[]. |]   |  |         #")
  print(" #          \\  ..  //    /  /           #")
  print(" #     __--__\///\\\/__--/  /            #")
  print(" #    / .    ||| |||       /            #")
  print(" #   /  /      w-w       _-             #")
  print(" #  |   |              /                #")
  print(" #  |   |              |                #")
  print(" #  |   |              |                #")
  print(" # /   |              |                 #")
  print(" ########################################" + '\n')
  time.sleep(2)

  # Ask user if they want to fight or run #
  print('"Do you want to FIGHT or RUN?"')
  user_input = input("> ").upper()
  while user_input not in ['FIGHT', 'RUN']:
    print("Unable to find response. Please try again.")
    time.sleep(2)
    print('"Do you want to FIGHT or RUN?"')
    user_input = input("> ").upper()
  if user_input in ['FIGHT']:
    print('"Prepare for battle! Be careful!"' + '\n')
    time.sleep(2)
    print("You ready your sword.")

    while angry_bandit.hp > 0:

    # randomised attack system for PLAYER! #
      player.attack_damage = random.randint(1, player.attack_power)
      player.attack_text = ' '
      if player.attack_damage  <= 5:
        player.attack_text = 'weak'
      elif player.attack_damage  <= 10:
        player.attack_text = 'moderate'
      elif player.attack_damage  <= 15:
        player.attack_text = 'strong'
      else:
        player.attack_text = 'very strong'


      print(f'You attack the Bandit for {player.attack_text} damage!')
      time.sleep(2)
      if player.attack_text == 'weak':
        print("The man grumbles as you slice at him!")
        time.sleep(2)
      elif player.attack_text == 'moderate':
        print("He grunts, your sword stabbing into his leg!")
        time.sleep(2)
      elif player.attack_text == 'moderate':
        print("He cries, asking you to stop!")
        time.sleep(2)
      elif player.attack_text == 'very strong':
        print("He falls.")
        time.sleep(2)

    # calculate angry bandit current HP
      angry_bandit.hp -= player.attack_damage
      print(f'The {angry_bandit.name} has {angry_bandit.hp} health remaining!'+ '\n')
      time.sleep(2)

    # check angry bandit HP!
      if angry_bandit.hp <= 0:
        print(f'You defeated the {angry_bandit.name}!')
        time.sleep(2)
        print('The other bandits run away in fear!'+'\n')
        time.sleep(2)
        break

    # randomised attack system for BANDIT! #
      angry_bandit.attack_damage = random.randint(1,5)

      angry_bandit_attack_text = ''

      if angry_bandit.attack_damage == 1:
        angry_bandit_attack_text = 'negligible'
      elif angry_bandit.attack_damage == 2:
        angry_bandit_attack_text = 'weak'
      elif angry_bandit.attack_damage == 3:
        angry_bandit_attack_text = 'moderate'
      elif angry_bandit.attack_damage == 4:
        angry_bandit_attack_text = 'strong'
      else:
        angry_bandit_attack_text = 'very strong'

      print(f'The {angry_bandit.name} swings the dagger at you for {angry_bandit.attack_damage} damage!')
      time.sleep(2)
      if angry_bandit_attack_text == 'negligible':
        print("You don't feel a thing.")
        time.sleep(2)
      elif angry_bandit_attack_text == 'weak':
        print("Ouch! You'll be okay.")
        time.sleep(2)
      elif angry_bandit_attack_text == 'moderate':
        print("That hurt! Keep your head up!")
        time.sleep(2)
      elif angry_bandit_attack_text == 'strong':
        print("That hurt a lot!")
        time.sleep(2)
      elif angry_bandit_attack_text== 'very strong':
        print("You groan in pure pain, bracing yourself.")
        time.sleep(2)

    # calculate remaining player HP:
      player.hp -= angry_bandit.attack_damage
      print('\n'+"#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#")
      print(f'# You have {player.hp} health remaining. #')
      print("#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#"+'\n')
      time.sleep(2)
      if player.hp <=0:
        print('"You have been defeated."')
        time.sleep(2)
        print('Thank you for playing my game!')
        time.sleep(2)
        print('"Better luck next time..."')
        time.sleep(2)
        sys.exit()

  #RUN option:
  elif user_input in ['RUN']:
    print("You flee from the battle." + '\n')
    time.sleep(2)


###############################################################################################

# Item Setup #
class Item:
  def __init__(self, name, description, hp_gain, attack_gain):
    self.name = name
    self.description = description
    self.hp_gain = hp_gain
    self.attack_gain = attack_gain
crystal = Item('Crystal', 'A shiny crystal that emits a strange aura.', 25, 5) #Crytsal Falls
bandage = Item('Bandage', 'A small bandage you can apply anywhere you wish.', 5, 0) #Home
sword = Item('Sword', 'A long, sharp sword with a dragon carved into the hilt.', 0, 0) #Home
book = Item('Book', 'A thick, loosely bound book that is filled with mysterious text.', 3, 10) #Book
idol = Item('Idol', 'A small wooden figure of an unkown creature. It looks scary.', 0, 5) #Small Island
cloak = Item('Cloak', 'A large fur coat. This could keep you really warm!', 10, 0) #Cabin
elixr = Item('Elixr', 'A small bottle of golden liquid.', 20, 0) #Temple
wand = Item('Wand','A short wooden stick that emits a strange power.', 5, 5) #Elf Village
dirty_carrot = Item('Dirty Carrot', 'A long, orange carrot covered in dirt.', 5, 0) #Farmlands
bread = Item('Bread', 'A long, crusty loaf of bread. It looks slightly burnt.', 10, 0)

###########CRYSTAL###########
def use_crystal(player, crystal):
  print('As you step into the water, you notice something sparkling underwater a few steps ahead of you.'+'\n')
  time.sleep(2)
  print('Curious, you step forward to look closer.')
  time.sleep(2)
  print('As you get closer, you can see a small blue crystal glowing between some river stones.')
  time.sleep(2)

  print("Do you want to take it?" + '\n')
  user_input = input("> ").upper()
  if user_input in ['YES', 'Yes', 'yes']:
    print("You plunge your hand into the water, picking the crystal up and placing it in your pocket.")
    time.sleep(2)
    print("You feel a tingling sensation in your hands."+ '\n')
    time.sleep(2)
    print("#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#")
    print("# You regain 25 HP and 5 AP.  #")
    print("#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#"+ '\n')
    time.sleep(2)
    player.hp = player.hp + crystal.hp_gain #calculate HP bonus
    player.attack_power = player.attack_power + crystal.attack_gain #calculate attack bonus
    print(f'You now have {player.hp} HP'+ f' and {player.attack_power} AP'+'\n')
    time.sleep(2)
  elif user_input in ['NO', 'no', 'No']:
    print("You decide not to take the crystal."+ '\n')
    time.sleep(2)
  else:
    while user_input not in ['YES', 'yes', 'Yes', 'No,', 'no', 'NO']:
      print("Could not find response. Please try again.")
      time.sleep(2)
      print("Do you want to take the crystal?")
      user_input = input("> ").upper()
      if user_input in ['YES', 'Yes', 'yes']:
        print("You plunge your hand into the water, picking the crystal up and placing it in your pocket.")
        time.sleep(2)
        print("You feel a tingling sensation in your hands."+ '\n')
        time.sleep(2)
        print("#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#")
        print("# You regain 25 HP and 5 AP.  #")
        print("#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#"+ '\n')
        time.sleep(2)
        player.hp = player.hp + crystal.hp_gain #calculate HP bonus
        player.attack_power = player.attack_power + crystal.attack_gain #calculate attack bonus
        print(f'You now have {player.hp} HP,'+ f'and {player.attack_power}.'+'\n')
        time.sleep(2)
      elif user_input in ['NO', 'no', 'No']:
        print("You decide not to take the crystal."+ '\n')
        time.sleep(2)

###########BANDAGE###########
def use_bandage(player, bandage):
  print('You look closer around the room and notice a small pile of bandages.')
  time.sleep(2)

  print("Do you want to take them?" + '\n')
  user_input = input("> ").upper()
  if user_input in ['YES', 'Yes', 'yes']:
    print("You take the bandages and wrap them around your knuckles.")
    time.sleep(2)
    print("You gain 5 HP.")
    time.sleep(2)
    player.hp = player.hp + bandage.hp_gain
    print(f'You now have {player.hp} HP.'+'\n')
    time.sleep(2)
  elif user_input in ['NO', 'no', 'No']:
    print("You decide not to take them.")
    time.sleep(2)
  else:
    while user_input not in ['YES', 'yes', 'Yes', 'No,', 'no', 'NO']:
      print("Could not find response. Please try again.")
      time.sleep(2)
      print("Do you want to take the bandages?")
      user_input = input("> ").upper()
      if user_input in ['YES', 'Yes', 'yes']:
        print("You take the bandages and wrap them around your knuckles.")
        time.sleep(2)
        print("You regain 5 HP.")
        time.sleep(2)
        player.hp = player.hp + bandage.hp_gain
        print(f'You now have {player.hp} HP.'+'\n')
        time.sleep(2)
      elif user_input in ['NO', 'no', 'No']:
        print("You decide not to take them.")
        time.sleep(2)

###########SWORD###########
def use_sword(player, sword):
  print('At the edge of your bed sits a long, silver sword with a dragon carved into the hilt.')
  time.sleep(2)

  print("Do you want to take it?" + '\n')
  user_input = input("> ").upper()
  if user_input in ['YES', 'Yes', 'yes']:
    print("You pick up the sword and sheath it at your side." + '\n')
    time.sleep(2)
  elif user_input in ['NO', 'no', 'No']:
    print("You decide not to take it.")
    time.sleep(2)
  else:
    while user_input not in ['YES', 'yes', 'Yes', 'No,', 'no', 'NO']:
      print("Could not find response. Please try again.")
      time.sleep(2)
      print("Do you want to take the sword?")
      user_input = input("> ").upper()
      if user_input in ['YES', 'Yes', 'yes']:
        print("You pick up the sword and sheath it at your side.")
        time.sleep(2)
      elif user_input in ['NO', 'no', 'No']:
        print("You decide not to take it.")
        time.sleep(2)

###########BOOK###########
def use_book(player, book):
  print('Between two dusty stones, an object sticks out.')
  time.sleep(2)
  print('As you move closer, you can see it is a large, leather-bound book, loose pages spilling out the side.')
  time.sleep(2)

  print("Do you want to take it?" + '\n')
  user_input = input("> ").upper()
  if user_input in ['YES', 'Yes', 'yes']:
    print("Carefully, you pull a stone aside and lift the book off the ground.")
    time.sleep(2)
    print("Curiously, you open the pages, only to not be able to read what is within.")
    time.sleep(2)
    print("You place it in your bag."+ '\n')
    time.sleep(2)
    print("#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#")
    print("#  You gain 3 HP and 10 AP.   #")
    print("#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#"+ '\n')
    time.sleep(2)
    player.hp = player.hp + book.hp_gain #calculate HP bonus
    player.attack_power = player.attack_power + book.attack_gain #calculate attack bonus
    print(f'You now have {player.hp} HP,'+ f'and {player.attack_power} AP.' + '\n')
    time.sleep(2)
  elif user_input in ['NO', 'no', 'No']:
    print("You decide not to take it."+ '\n')
    time.sleep(2)
  else:
    while user_input not in ['YES', 'yes', 'Yes', 'No,', 'no', 'NO']:
      print("Could not find response. Please try again.")
      time.sleep(2)
      print("Do you want to take the book?")
      user_input = input("> ").upper()
      if user_input in ['YES', 'Yes', 'yes']:
        print("Carefully, you pull a stone aside and lift the book off the ground.")
        time.sleep(2)
        print("Curiously, you open the pages, only to not be able to read what is within.")
        time.sleep(2)
        print("You place it in your bag."+ '\n')
        time.sleep(2)
        print("#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#")
        print("#  You gain 3 HP and 10 AP.   #")
        print("#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#"+ '\n')
        time.sleep(2)
        player.hp = player.hp + book.hp_gain #calculate HP bonus
        player.attack_power = player.attack_power + book.attack_gain #calculate attack bonus
        print(f'You now have {player.hp} HP,'+ f'and {player.attack_power} AP.' + '\n')
        time.sleep(2)
      elif user_input in ['NO', 'no', 'No']:
        print("You decide not to take it."+ '\n')
        time.sleep(2)

###########IDOL###########
def use_idol (player, idol):
  print("You reach the outcrop, with a small object sitting atop it now becoming visible.")
  time.sleep(2)
  print("You hear whispering, but you can't tell where it's coming from.")
  time.sleep(2)
  print("Will you take the idol?" + '\n')
  user_input = input("> ").upper()
  if user_input in ['YES', 'Yes', 'yes']:
    print("You pick it up caustiously, and the whispering stops abruptly.")
    time.sleep(2)
    print("You place it in your bag.")
    time.sleep(2)
    print("You gain 5 AP.")
    time.sleep(2)
    player.attack_power = player.attack_power + idol.attack_gain #calculate attack bonus
    print(f'You now have {player.attack_power}.''\n')
    time.sleep(2)
  elif user_input in ['NO', 'no', 'No']:
    print("You decide not to take it.")
    time.sleep(2)
  else:
    while user_input not in ['YES', 'yes', 'Yes', 'No,', 'no', 'NO']:
      print("Could not find response. Please try again.")
      time.sleep(2)
      print("Do you want to take the idol?")
      user_input = input("> ").upper()
      if user_input in ['YES', 'Yes', 'yes']:
        print("You pick it up caustiously, and the whispering stops abruptly.")
        time.sleep(2)
        print("You place it in your bag.")
        time.sleep(2)
        print("You gain 5 AP.")
        time.sleep(2)
        player.attack_power = player.attack_power + idol.attack_gain #calculate attack bonus
        print(f'You now have {player.attack_power} AP.''\n')
        time.sleep(2)
      elif user_input in ['NO', 'no', 'No']:
        print("You decide not to take it.")
        time.sleep(2)

###########CLOAK###########
def use_cloak (player, cloak):
  print("Hidden in the back of a small wooden cabinet, you spot a thick, fur coat.")
  time.sleep(2)
  print("You pull it out and immediately feel warm as it touches your skin.")
  time.sleep(2)
  print("Will you take the cloak?" + '\n')
  user_input = input("> ").upper()
  if user_input in ['YES', 'Yes', 'yes']:
    print("You pull the cloak comfortably over your shoulders.")
    time.sleep(2)
    print("It seems to fit perfectly."+ '\n')
    time.sleep(2)
    print("#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#")
    print("#       You gain 10 HP.       #")
    print("#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#"+ '\n')
    time.sleep(2)
    player.hp = player.hp + cloak.hp_gain #calculate hp bonus
    print(f'You now have {player.hp} HP.'+'\n')
    time.sleep(2)
  elif user_input in ['NO', 'no', 'No']:
    print("You decide not to take it."+ '\n')
    time.sleep(2)
  else:
    while user_input not in ['YES', 'yes', 'Yes', 'No,', 'no', 'NO']:
      print("Could not find response. Please try again.")
      time.sleep(2)
      print("Do you want to take the cloak?")
      user_input = input("> ").upper()
      if user_input in ['YES', 'Yes', 'yes']:
        print("You pull the cloak comfortably over your shoulders.")
        time.sleep(2)
        print("It seems to fit perfectly."+ '\n')
        time.sleep(2)
        print("#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#")
        print("#       You gain 10 HP.       #")
        print("#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#"+ '\n')
        time.sleep(2)
        player.hp = player.hp + cloak.hp_gain #calculate hp bonus
        print(f'You now have {player.hp} HP.'+'\n')
        time.sleep(2)
      elif user_input in ['NO', 'no', 'No']:
        print("You decide not to take it."+ '\n')
        time.sleep(2)

###########ELIXR###########
def use_elixr (player, elixr):
  print("You wander through the grand halls of the temple.")
  time.sleep(2)
  print("It is deserted, but a small glass bottle atop an ionic pillar catches your eye.")
  time.sleep(2)
  print("Upon further observation, you can see some sort of golden liquid inside it.")
  time.sleep(2)
  print("Will you drink the elixr?" + '\n')
  time.sleep(2)
  user_input = input("> ").upper()
  if user_input in ['YES', 'Yes', 'yes']:
    print("You flip the metal cap off the bottle, cautiously placing the glass to your lips.")
    time.sleep(2)
    print("You swallow it down, feeling the warmth flow through your body.")
    time.sleep(2)
    print("You gain 20 HP.")
    time.sleep(2)
    player.hp = player.hp + elixr.hp_gain #calculate hp bonus
    print(f'You now have {player.hp} HP.'+'\n')
    time.sleep(2)
  elif user_input in ['NO', 'no', 'No']:
    print("You decide not to take it.")
    time.sleep(2)
  else:
    while user_input not in ['YES', 'yes', 'Yes', 'No,', 'no', 'NO']:
      print("Could not find response. Please try again.")
      time.sleep(2)
      print("Do you want to drink the elixr?")
      user_input = input("> ").upper()
      if user_input in ['YES', 'Yes', 'yes']:
        print("You flip the metal cap off the bottle, cautiously placing the glass to your lips.")
        time.sleep(2)
        print("You swallow it down, feeling the warmth flow through your body.")
        time.sleep(2)
        print("You gain 20 HP.")
        time.sleep(2)
        player.hp = player.hp + elixr.hp_gain #calculate hp bonus
        print(f'You now have {player.hp} HP.''\n')
        time.sleep(2)
      elif user_input in ['NO', 'no', 'No']:
        print("You decide not to take it.")
        time.sleep(2)

###########WAND###########
def use_wand (player, wand):
  print("You step through the village gates, greeted by a short elf with wispy grey hair and age in his eyes.")
  time.sleep(2)
  print("He appears to have a small pedler's cart of various miscellaneous magic items.")
  time.sleep(2)
  print('"Hello, traveller. May I interest you in some of my wares?"' + '\n')
  time.sleep(2)
  user_input = input("> ").upper()
  if user_input in ['YES', 'Yes', 'yes']:
    print('"Hmmm...", he says.')
    time.sleep(2)
    print('"Something tells me you need this more than me. Here,", he reaches out and hands you a small wand. "a magic wand for you. Take care, traveller."')
    time.sleep(2)
    print("Before you even have time to pay him, he waddles away.")
    time.sleep(2)
    print("The wand feels right. That's the only word for it.")
    time.sleep(2)
    print("You place it in your bag and move on."+ '\n')
    time.sleep(2)
    print("#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#")
    print("#   You gain 5 HP and 5 AP.   #")
    print("#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#"+ '\n')
    time.sleep(2)
    player.hp = player.hp + wand.hp_gain #calculate hp bonus
    player.attack_power = player.attack_power + wand.attack_gain #calculate AP bonus
    print(f'You now have {player.hp} HP and {player.attack_power} AP.'+ '\n')
    time.sleep(2)
  elif user_input in ['NO', 'no', 'No']:
    print("You shake your head, walking away from the elf."+ '\n')
    time.sleep(2)
  else:
    while user_input not in ['YES', 'yes', 'Yes', 'No,', 'no', 'NO']:
      print("Could not find response. Please try again.")
      time.sleep(2)
      print('"Hello, traveller. May I interest you in some of my wares?"' + '\n')
      user_input = input("> ").upper()
      if user_input in ['YES', 'Yes', 'yes']:
        print('"Hmmm...", he says.')
        time.sleep(2)
        print('"Something tells me you need this more than me. Here,", he reaches out and hands you a small wand. "a magic wand for you. Take care, traveller."')
        time.sleep(2)
        print("Before you even have time to pay him, he waddles away.")
        time.sleep(2)
        print("The wand feels right. That's the only word for it.")
        time.sleep(2)
        print("You place it in your bag and move on."+ '\n')
        time.sleep(2)
        print("#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#")
        print("#   You gain 5 HP and 5 AP.   #")
        print("#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#"+ '\n')
        time.sleep(2)
        player.hp = player.hp + wand.hp_gain #calculate hp bonus
        player.attack_power = player.attack_power + wand.attack_gain #calculate AP bonus
        print(f'You now have {player.hp} HP and {player.attack_power} AP.'+ '\n')
        time.sleep(2)
      elif user_input in ['NO', 'no', 'No']:
        print("You shake your head, walking away from the elf."+ '\n')
        time.sleep(2)

###########DIRTY_CARROT###########
def use_dirty_carrot (player, dirty_carrot):
  print("As you walk through the cropfields, you notice a large, dirt-coated carrot.")
  time.sleep(2)
  print("Your stomach rumbles.")
  time.sleep(2)
  print("Do you want to eat the carrot? Nobody's watching." + '\n')
  user_input = input("> ").upper()
  if user_input in ['YES', 'Yes', 'yes']:
    print("Hungrily, you pick the carrot up, dusting some dirt off before taking a huge bite..")
    time.sleep(2)
    print("Surprisingly, it doesn't taste too bad!"+ '\n')
    time.sleep(2)
    print("#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#")
    print("#        You gain 5 HP.       #")
    print("#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#"+ '\n')
    time.sleep(2)
    player.hp = player.hp + dirty_carrot.hp_gain #calculate hp bonus
    print(f'You now have {player.hp} HP.'+'\n')
    time.sleep(2)
  elif user_input in ['NO', 'no', 'No']:
    print("You leave the carrot alone, ignoring your rumbling belly.")
    time.sleep(2)
  else:
    while user_input not in ['YES', 'yes', 'Yes', 'No,', 'no', 'NO']:
      print("Could not find response. Please try again.")
      time.sleep(2)
      print("Do you want to eat the carrot? Nobody's watching." + '\n')
      user_input = input("> ").upper()
      if user_input in ['YES', 'Yes', 'yes']:
        print("Hungrily, you pick the carrot up, dusting some dirt off before taking a huge bite..")
        time.sleep(2)
        print("Surprisingly, it doesn't taste too bad!"+ '\n')
        time.sleep(2)
        print("#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#")
        print("#        You gain 5 HP.       #")
        print("#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#"+ '\n')
        time.sleep(2)
        player.hp = player.hp + dirty_carrot.hp_gain #calculate hp bonus
        print(f'You now have {player.hp} HP.'+'\n')
        time.sleep(2)
      elif user_input in ['NO', 'no', 'No']:
        print("You leave the carrot alone, ignoring your rumbling belly.")
        time.sleep(2)

###########BREAD###########
def use_bread(player, bread):
  print("The marketplace is bustling with people crowding around all kinds of stands.")
  time.sleep(2)
  print("Your stomach rumbles.")
  time.sleep(2)
  print("The smell of fresh bread guides you to a bakery, a line of several people waiting out the door.")
  time.sleep(2)
  print("Wandering around the back, you spot a pile of discarded loaves.")
  time.sleep(2)
  print("They don't look too bad! Will you take one to eat?"+ '\n')
  user_input = input("> ").upper()
  if user_input in ['YES', 'Yes', 'yes']:
    print("You quietly sneak over, snagging the biggest loaf you can.")
    time.sleep(2)
    print("You eat it as you walk away from the scene.")
    time.sleep(2)
    print("You gain 10 HP.")
    time.sleep(2)
    player.hp = player.hp + bread.hp_gain #calculate hp bonus
    print(f'You now have {player.hp} HP.'+'\n')
    time.sleep(2)
  elif user_input in ['NO', 'no', 'No']:
    print("You spot a patch of mould on one of the loaves anyway. Ew.")
    time.sleep(2)
  else:
    while user_input not in ['YES', 'yes', 'Yes', 'No,', 'no', 'NO']:
      print("Could not find response. Please try again.")
      time.sleep(2)
      print("They don't look too bad! Will you take one to eat?"+ '\n')
      user_input = input("> ").upper()
      if user_input in ['YES', 'Yes', 'yes']:
        print("You quietly sneak over, snagging the biggest loaf you can.")
        time.sleep(2)
        print("You eat it as you walk away from the scene.")
        time.sleep(2)
        print("You gain 10 HP.")
        time.sleep(2)
        player.hp = player.hp + bread.hp_gain #calculate hp bonus
        print(f'You now have {player.hp} HP.'+'\n')
        time.sleep(2)
      elif user_input in ['NO', 'no', 'No']:
        print("You spot a patch of mould on one of the loaves anyway. Ew.")
        time.sleep(2)

###########BREAD###########
def use_bread(player, bread):
  print("The marketplace is bustling with people crowding around all kinds of stands.")
  time.sleep(2)
  print("Your stomach rumbles.")
  time.sleep(2)
  print("The smell of fresh bread guides you to a bakery, a line of several people waiting out the door.")
  time.sleep(2)
  print("Wandering around the back, you spot a pile of discarded loaves.")
  time.sleep(2)
  print("They don't look too bad! Will you take one to eat?"+ '\n')
  user_input = input("> ").upper()
  if user_input in ['YES', 'Yes', 'yes']:
    print("You quietly sneak over, snagging the biggest loaf you can.")
    time.sleep(2)
    print("You eat it as you walk away from the scene."+'\n')
    time.sleep(2)
    print("#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#")
    print("#       You gain 10 HP.       #")
    print("#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#"+'\n')
    time.sleep(2)
    player.hp = player.hp + bread.hp_gain #calculate hp bonus
    print(f'You now have {player.hp} HP.'+'\n')
    time.sleep(2)
  elif user_input in ['NO', 'no', 'No']:
    print("You spot a patch of mould on one of the loaves anyway. Ew."+ '\n')
    time.sleep(2)
  else:
    while user_input not in ['YES', 'yes', 'Yes', 'No,', 'no', 'NO']:
      print("Could not find response. Please try again.")
      time.sleep(2)
      print("They don't look too bad! Will you take one to eat?"+ '\n')
      user_input = input("> ").upper()
      if user_input in ['YES', 'Yes', 'yes']:
        print("You quietly sneak over, snagging the biggest loaf you can.")
        time.sleep(2)
        print("You eat it as you walk away from the scene."+'\n')
        time.sleep(2)
        print("#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#")
        print("#       You gain 10 HP.       #")
        print("#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#"+'\n')
        time.sleep(2)
        player.hp = player.hp + bread.hp_gain #calculate hp bonus
        print(f'You now have {player.hp} HP.'+'\n')
        time.sleep(2)
      elif user_input in ['NO', 'no', 'No']:
        print("You spot a patch of mould on one of the loaves anyway. Ew." + '\n')
        time.sleep(2)



###############################################################################################

# Title screen #
def title_screen_selections():
  option = input("> ")
  if option.lower() == ("play"):
    setup_game() 
  elif option.lower() == ("help"):
    help_menu()
  elif option.lower() == ("quit"):
    sys.exit()
  while option.lower() not in ['play' , 'help', 'quit']:
    print("Please enter a valid command.")
    option = input("> ")
    if option.lower == ("play"):
     setup_game() 
    elif option.lower() == ("help"):
       help_menu()
    elif option.lower() == ("quit"):
      sys.exit()

def title_screen():
  os.system('clear')
  print('#~~~~~~~~~~~~~~~~~~~~~~~~~~~~#')
  print('#                            #')
  print('#   F A D I N G   V A L E    #')
  print('#                            #')
  print('#~~~~~~~~~~~~~~~~~~~~~~~~~~~~#')
  print('#                            #')
  print('#          - PLAY -          #')  
  print('#                            #')
  print('#          - HELP -          #')
  print('#                            #')
  print('#          - QUIT -          #')
  print('#                            #')
  print('#~~~~~~~~~~~~~~~~~~~~~~~~~~~~#')
  print('#         [24575161]         #')
  print('#~~~~~~~~~~~~~~~~~~~~~~~~~~~~#')
  title_screen_selections()

def help_menu():
  print('#~~~~~~~~~~~~~~~~~~~~~~~~~~~~#')
  print('#           H E L P          #') 
  print('#~~~~~~~~~~~~~~~~~~~~~~~~~~~~#')
  print('#          To move:          #') 
  print("#type UP, DOWN, LEFT or RIGHT#")
  print('#   To examine: type LOOK    #')
  print('#  To fight: follow prompts  #')
  print('#~~~~~~~~~~~~~~~~~~~~~~~~~~~~#')
  title_screen_selections()


# MAP - player starts in b2

#--------------------------
#| a1 | a2 | a3 | a4 | a5 |
#--------------------------
#| b1 | b2 | b3 | b4 | b5 |
#--------------------------
#| c1 | c2 | c3 | c4 | c5 |
#--------------------------
#| d1 | d2 | d3 | d4 | d5 |
#--------------------------
#| e1 | e2 | e3 | e4 | e5 |
#--------------------------

#MAP DICTIONARY#
{
'ZONENAME': 'zonename',
'DESCRIPTION': 'description',
'EXAMINATION': 'examine',
'ENEMIES' : 'enemies',
'ITEMS' : 'items',
'SOLVED': False,
'UP': ['up', 'north'],
'DOWN': ['down', 'south'],
'LEFT': ['left', 'west'],
'RIGHT': ['right', 'east']
}

solved_places = {'A1: Ancient Ruins': False, 'A2: Bandits Hideout': False, 'A3: Crystal Falls': False, 'A4: Northern Bay': False, 'A5: Calm Ocean': False,
                'B1: Farmlands': False, 'B2: Town Outskirts': False, 'B3: Town Centre': False, 'B4: Docks': False, 'B5: Small Island': False,
                'C1: Acropolis': False, 'C2: Grass Plains': False, 'C3: Castle': False, 'C4: Rugged Cliffs': False, 'C5: Shipwrecks': False,
                'D1: Mushroom Hut': False, 'D2: Highlands': False, 'D3: Mountain Cabin': False, 'D4: Cave': False, 'D5: Temple': False,
                'E1: Swamplands': False, 'E2: Elf Village': False, 'E3: Stronghold': False, 'E4: Forest': False, 'E5: Orc Camp': False,}

#FULL ZONEMAP#
zonemap = {
    'A1: Ancient Ruins': {
      'ZONENAME': "Ancient Ruins",
      'DESCRIPTION': 'Before you lies a series of superimposed stone structures arranged in a circle.',
      'EXAMINATION': 'You look closer and notice a trapdoor in the centre of the ruins.',
      'ENEMIES': [],
      'ITEMS': [book],
      'SOLVED': False,
      'UP': '',
      'DOWN': 'B1: Farmlands',
      'LEFT': '',
      'RIGHT': 'A2: Bandits Hideout',
  }, 
  'A2: Bandits Hideout': {
    'ZONENAME': "Bandits Hideout",
    'DESCRIPTION': 'Nestled within the forest, the bandits have gathered and set up camp on the riverside.',
    'EXAMINATION': 'The bandits are talking, their weapons laid to rest as they feast on the spoils of their latest raid.',
    'ENEMIES': [angry_bandit],
    'ITEMS': [],
    'SOLVED': False,
    'UP': '',
    'DOWN': 'B2: Town Outskirts',
    'LEFT': 'A1: Ancient Ruins',
    'RIGHT': 'A3: Crystal Falls',
  },
  'A3: Crystal Falls': {
    'ZONENAME': "Crystal Falls",
    'DESCRIPTION': 'The river spills over the cliffs, the crystals in the pool beneath glimmering brightly.',
    'EXAMINATION': 'Some crystals have been pushed by currents to the shorelines.',
    'ENEMIES': [],
    'ITEMS': [crystal],
    'SOLVED': False,
    'UP': '',
    'DOWN': 'B3: Town Centre',
    'LEFT': 'A2: Bandits Hideout',
    'RIGHT': 'A4: Northern Bay',
  },
  'A4: Northern Bay': {
    'ZONENAME': "Northern Bay",
    'DESCRIPTION': 'The river opens up and the ocean lies ahead. The waves gently caress the sand in front of you.',
    'EXAMINATION': 'Nothing has changed.',
    'ENEMIES': [],
    'ITEMS': [],
    'SOLVED': False,
    'UP': '',
    'DOWN': 'B4: Docks',
    'LEFT': 'a3',
    'RIGHT': 'A5: Calm Ocean',
  },
  'A5: Calm Ocean': {
    'ZONENAME': "Calm Ocean",
    'DESCRIPTION': 'The waves are gentle, and the deep blue water glistens.',
    'EXAMINATION': 'Nothing has changed.',
    'ENEMIES': [],
    'ITEMS': [],
    'SOLVED': False,
    'UP': '',
    'DOWN': 'B5: Small Island',
    'LEFT': 'A4: Northern Bay',
    'RIGHT': '',
  },
  'B1: Farmlands': {
    'ZONENAME': "Farmlands",
    'DESCRIPTION': "Quiet farmer's huts dot the horizon, long stretches of cropfields and cattle as far as your eyes can see.",
    'EXAMINATION': 'If you were quiet enough you could probably snatch some food.',
    'ENEMIES': [],
    'ITEMS': [dirty_carrot],
    'SOLVED': False,
    'UP': 'A1: Ancient Ruins',
    'DOWN': 'C1: Acropolis',
    'LEFT': '',
    'RIGHT': 'B2: Town Outskirts',
  },
  'B2: Town Outskirts': {
    'ZONENAME': "Town Outskirts",
    'DESCRIPTION': 'You live here, in the outskirts of a bustling town.',
    'EXAMINATION': 'Nothing has changed.',
    'ENEMIES': [],
    'ITEMS': [],
    'SOLVED': False,
    'UP': 'A2: Bandits Hideout',
    'DOWN': 'C2: Grass Plains',
    'LEFT': 'B1: Farmlands',
    'RIGHT': 'B3: Town Centre',
  },
  'B3: Town Centre': {
    'ZONENAME': "Town Centre",
    'DESCRIPTION': 'This is the centre of town. Busy markets surround you.',
    'EXAMINATION': 'You can find food or other materials here.',
    'ENEMIES': [],
    'ITEMS': [bread],
    'SOLVED': False,
    'UP': 'A3: Crystal Falls',
    'DOWN': 'C3: Castle',
    'LEFT': 'B2: Town Outskirts',
    'RIGHT': 'B4: Docks',
  },
  'B4: Docks': {
    'ZONENAME': "Docks",
    'DESCRIPTION': 'On the edge of the town, hundreds of boats are parked at the docks.',
    'EXAMINATION': 'A bearded man sleeps next to a small boat just in front of you.',
    'ENEMIES': [],
    'ITEMS': [],
    'SOLVED': False,
    'UP': 'A4: Northern Bay',
    'DOWN': 'C4: Rugged Cliffs',
    'LEFT': 'B3: Town Centre',
    'RIGHT': 'B5: Small Island',
  },
  'B5: Small Island': {
    'ZONENAME': "Small Island",
    'DESCRIPTION': 'Not too far out from the docks, a small island stands in the ocean.',
    'EXAMINATION': 'The island looks deserted. You can see a small stone outcrop on the shoreline.',
    'ENEMIES': [],
    'ITEMS': [idol],
    'SOLVED': False,
    'UP': 'A5: Calm Ocean',
    'DOWN': 'C5: Shipwrecks',
    'LEFT': 'B4: Docks',
    'RIGHT': '',
  },
  'C1: Acropolis': {
    'ZONENAME': "Acropolis",
    'DESCRIPTION': 'A mass gravesite shrouded in a dark cloud.',
    'EXAMINATION': 'You sense the impending doom of death.',
    'ENEMIES': [spider],
    'ITEMS': [],
    'SOLVED': False,
    'UP': 'B1: Farmlands',
    'DOWN': 'D1: Mushroom Hut',
    'LEFT': '',
    'RIGHT': 'C2: Grass Plains',
  },
  'C2: Grass Plains': {
    'ZONENAME': "Grass Plains",
    'DESCRIPTION': 'A large expanse of grass. The only thing in sight are distant highlands.',
    'EXAMINATION': 'Nothing has changed.',
    'ENEMIES': [],
    'ITEMS': [],
    'SOLVED': False,
    'UP': 'B2: Town Outskirts',
    'DOWN': 'D2: Highlands',
    'LEFT': 'C1: Acropolis',
    'RIGHT': 'C3: Castle',
  },
  'C3: Castle': {
    'ZONENAME': "Castle",
    'DESCRIPTION': 'A massive building surrounded by walls. It is heavily guarded.',
    'EXAMINATION': "The royal guard's barracks are located just outside the walls.",
    'ENEMIES': [],
    'ITEMS': [],
    'SOLVED': False,
    'UP': 'B3: Town Centre',
    'DOWN': 'D3: Mountain Cabin',
    'LEFT': 'C2: Grass Plains',
    'RIGHT': 'C4: Rugged Cliffs',
  },
  'C4: Rugged Cliffs': {
    'ZONENAME': "Rugged Cliffs",
    'DESCRIPTION': 'You feel the ocean breeze beckon you to the edge of some tall cliffs. Bellow, sharp rocks beckon an uneasy death.',
    'EXAMINATION': 'Better stay away from the edge!',
    'ENEMIES': [],
    'ITEMS': [],
    'SOLVED': False,
    'UP': 'B4: Docks',
    'DOWN': 'D4: Cave',
    'LEFT': 'C3: Castle',
    'RIGHT': 'C5: Shipwrecks',
  },
  'C5: Shipwrecks': {
    'ZONENAME': "Shipwrecks",
    'DESCRIPTION': 'Nestled in the jagged rocks lies a graveyard of ships.',
    'EXAMINATION': 'You spot a small ghostly figure floating amongst the wrecks.',
    'ENEMIES': [siren],
    'ITEMS': [],
    'SOLVED': False,
    'UP': 'B5: Small Island',
    'DOWN': 'D5: Temple',
    'LEFT': 'C4: Rugged Cliffs',
    'RIGHT': '',
  },
  'D1: Mushroom Hut': {
    'ZONENAME': "Mushroom Hut",
    'DESCRIPTION': 'A small hut covered in mushrooms and toadstools of all shapes and sizes.',
    'EXAMINATION': 'You listen closely and hear maniacal laughter and the sound of something smashing.',
    'ENEMIES': [witch],
    'ITEMS': [],
    'SOLVED': False,
    'UP': 'C1: Acropolis',
    'DOWN': 'E1: Swamplands',
    'LEFT': '',
    'RIGHT': 'D2: Highlands',
  },
  'D2: Highlands': {
    'ZONENAME': "Highlands",
    'DESCRIPTION': 'A road winds up through steep, rocky territory.',
    'EXAMINATION': 'Nothing has changed.',
    'ENEMIES': [],
    'ITEMS': [],
    'SOLVED': False,
    'UP': 'C2: Grass Plains',
    'DOWN': 'E2: Elf Village',
    'LEFT': 'D1: Mushroom Hut',
    'RIGHT': 'D3: Mountain Cabin',
  },
  'D3: Mountain Cabin': {
    'ZONENAME': "Mountain Cabin",
    'DESCRIPTION': "A small log cabin close to the mountain's summit.",
    'EXAMINATION': 'The cabin looks uninhabited.',
    'ENEMIES': [],
    'ITEMS': [cloak],
    'SOLVED': False,
    'UP': 'C3: Castle',
    'DOWN': 'E3: Stronghold',
    'LEFT': 'D2: Highlands',
    'RIGHT': 'D4: Cave',
  },
  'D4: Cave': {
    'ZONENAME': "Cave",
    'DESCRIPTION': 'A gaping hole in the side of the mountain.',
    'EXAMINATION': 'A wyvern can be seen curled up on a mound of various golden objects.',
    'ENEMIES': [wyvern],
    'ITEMS': [],
    'SOLVED': False,
    'UP': 'C4: Rugged Cliffs',
    'DOWN': 'E4: Forest',
    'LEFT': 'D3: Mountain Cabin',
    'RIGHT': 'D5: Temple',
  },
  'D5: Temple': {
    'ZONENAME': "Temple",
    'DESCRIPTION': 'A small temple made from golden bricks stands alone.',
    'EXAMINATION': "Nothing has changed.",
    'ENEMIES': [],
    'ITEMS': [elixr],
    'SOLVED': False,
    'UP': 'C5: Shipwrecks',
    'DOWN': 'E5: Orc Camp',
    'LEFT': 'D4: Cave',
    'RIGHT': '',
  },
  'E1: Swamplands': {
    'ZONENAME': "Swamplands",
    'DESCRIPTION': 'A dark, damp forest. Murky water flows in between the tall trees.',
    'EXAMINATION': 'An ogre stomps past, carrying a thick claymore as he grumbles.',
    'ENEMIES': [ogre],
    'ITEMS': [],
    'SOLVED': False,
    'UP': 'D1: Mushroom Hut',
    'DOWN': '',
    'LEFT': '',
    'RIGHT': 'e2',
  },
  'E2: Elf Village': {
    'ZONENAME': "Elf Village",
    'DESCRIPTION': 'A valley unfolds. Elves can be seen going about their days in the village below.',
    'EXAMINATION': 'Nothing has changed.',
    'ENEMIES': [],
    'ITEMS': [wand],
    'SOLVED': False,
    'UP': 'D2: Highlands',
    'DOWN': '',
    'LEFT': 'E1: Swamplands',
    'RIGHT': 'E3: Stronghold',
  },
  'E3: Stronghold': {
    'ZONENAME': "Stronghold",
    'DESCRIPTION': 'A dark tower looms above. A faint roaring sound can be heard behind its walls.',
    'EXAMINATION': 'A small wooden door is built into the side of the tower. It stands ajar.',
    'ENEMIES': [],
    'ITEMS': [],
    'SOLVED': False,
    'UP': 'D3: Mountain Cabin',
    'DOWN': '',
    'LEFT': 'E2: Elf Village',
    'RIGHT': 'E4: Forest',
  },
  'E4: Forest': {
    'ZONENAME': "Forest",
    'DESCRIPTION': 'A forest of pine trees.',
    'EXAMINATION': 'Nothing has changed.',
    'ENEMIES': [],
    'ITEMS': [], 
    'SOLVED': False,
    'UP': 'D4: Cave',
    'DOWN': '',
    'LEFT': 'E3: Stronghold',
    'RIGHT': 'E5: Orc Camp',
  },
  'E5: Orc Camp': {
    'ZONENAME': "Orc Camp",
    'DESCRIPTION': "A small convoluted pile of tents and lean-to's house a small band of orcs.",
    'EXAMINATION': 'Nothing has changed.',
    'ENEMIES': [],
    'SOLVED': False,
    'UP': 'D5: Temple',
    'DOWN': '',
    'LEFT': 'E4: Forest',
    'RIGHT': '',
  },
}

# GAME INTERACTIVITY
def print_location():
    print('\n' + ('#' * (4 + len(myPlayer.location))))
    print('# ' + myPlayer.location.upper() + ' #')
    print('# ' + zonemap[myPlayer.location] ['DESCRIPTION'] + ' #' + '\n')
    time.sleep(2)
    print('\n' + ('#' * (4 + len(myPlayer.location))))
    print('You are in the ' + myPlayer.location + '.\n')
    time.sleep(2)

    if zonemap[myPlayer.location]['ENEMIES']:
      print("#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#")
      print("# There are enemies present...#")
      print("#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#"+'\n')
      time.sleep(2)
    if zonemap[myPlayer.location]['ITEMS']:
      print("#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#")
      print("#  There are items present... #")
      print("#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#"+'\n')
      time.sleep(2)

        
def player_move(myAction):
  ask = "Where would you like to move to?\n"
  dest = input(ask)
  if dest.lower() in ['up', 'north'] and zonemap[myPlayer.location]['UP']:
    destination = zonemap[myPlayer.location]['UP']
    movement_handler(destination)
  elif dest.lower() in ['down', 'south'] and zonemap[myPlayer.location]['DOWN']:
    destination = zonemap[myPlayer.location]['DOWN']
    movement_handler(destination)
  elif dest.lower() in ['left', 'west'] and zonemap[myPlayer.location]['LEFT']:
    destination = zonemap[myPlayer.location]['LEFT']
    movement_handler(destination)
  elif dest.lower() in ['right', 'east'] and zonemap[myPlayer.location]['RIGHT']:
    destination = zonemap[myPlayer.location]['RIGHT']
    movement_handler(destination)
  else:
    print("You cannot move in this direction. Try again."+'\n')

def movement_handler(destination):
    print('\n' + 'You have moved to the ' + zonemap[destination]['ZONENAME'] + '.')
    myPlayer.location = destination
    print_location()

def player_examine(action):
  current_zone = zonemap[myPlayer.location]
  if zonemap[myPlayer.location]['SOLVED']:
    print("You have already solved this zone."+'\n')
  else:
    print("There is nothing to do here."+'\n')

    

def prompt():
    print('\n' + '#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#')
    print('       What will you do?      ')
    print('You can move, examine or quit.')
    print('#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#'+ '\n')
    action = input("> ")
    acceptable_actions = ['move','quit', 'examine'] 
 
    while action.lower() not in acceptable_actions:
      print('Unknown action. Please try again.'+'\n')
      action = input('> ')
    if action.lower() == 'quit':
      sys.exit()
    elif action.lower() in ['move', 'travel', 'go', 'walk', 'run']:
      player_move(action.lower())
    elif action.lower() in ['examine', 'inspect', 'interact', 'look']:
      player_examine(action.lower())


def main_game_loop():
  while myPlayer.game_over is False: 
    prompt()

    # trigger combat/items #
    if myPlayer.location == 'A1: Ancient Ruins' and not zonemap['A1: Ancient Ruins']['SOLVED']:
      use_book(myPlayer, book)
      zonemap['A1: Ancient Ruins']['SOLVED']= True
      
    if myPlayer.location == 'A2: Bandits Hideout' and not zonemap['A2: Bandits Hideout']['SOLVED']:
      angry_bandit_battle(myPlayer, angry_bandit)
      zonemap['A2: Bandits Hideout']['SOLVED']= True
      
    if myPlayer.location == 'A3: Crystal Falls' and not zonemap['A3: Crystal Falls']['SOLVED']:
      use_crystal(myPlayer, crystal)
      zonemap['A3: Crystal Falls']['SOLVED']= True
      
    #nothing in zone 'a4'
    #nothing in zone 'a5'
    
    if myPlayer.location == 'B1: Farmlands' and not zonemap['B1: Farmlands']['SOLVED']:
      use_dirty_carrot(myPlayer, dirty_carrot)
      zonemap ['B1: Farmlands']['SOLVED']= True
      
    if myPlayer.location == 'B2: Town Outskirts' and not zonemap['B2: Town Outskirts']['SOLVED']:
      use_sword(myPlayer, sword)
      use_bandage(myPlayer, bandage)
      zonemap['B2: Town Outskirts']['SOLVED']= True
      
    if myPlayer.location == 'B3: Town Centre' and not zonemap['B3: Town Centre']['SOLVED']:
      use_bread(myPlayer, bread)
      zonemap['B3: Town Centre']['SOLVED']= True
      
    #nothing in zone 'b4'
    
    if myPlayer.location == 'B5: Small Island' and not zonemap['B5: Small Island']['SOLVED']:
      use_idol(myPlayer, idol)
      zonemap['B5: Small Island']['SOLVED']= True
      
    if myPlayer.location == 'C1: Acropolis' and not zonemap['C1: Acropolis']['SOLVED']:
      spider_battle(myPlayer, spider)
      zonemap['C1: Acropolis']['SOLVED']= True
      
    #nothing in zone 'c2'
    #nothing in zone 'c3'
    #nothing in zone 'c4'
    
    if myPlayer.location == 'C5: Shipwrecks' and not zonemap['C5: Shipwrecks']['SOLVED']:
      siren_battle(myPlayer, siren)
      zonemap['C5: Shipwrecks']['SOLVED']= True
      
    if myPlayer.location == 'D1: Mushroom Hut' and not zonemap['D1: Mushroom Hut']['SOLVED']:
      witch_battle(myPlayer, witch)
      zonemap['D1: Mushroom Hut']['SOLVED']= True
      
    #nothing in zone 'd2'
    
    if myPlayer.location == 'D3: Mountain Cabin' and not zonemap['D3: Mountain Cabin']['SOLVED']:
      use_cloak(myPlayer, cloak)
      zonemap['D3: Mountain Cabin']['SOLVED']= True
      
    if myPlayer.location == 'D4: Cave' and not zonemap['D4: Cave']['SOLVED']:
      wyvern_battle(myPlayer, wyvern)
      zonemap['D4: Cave']['SOLVED']= True
      
    if myPlayer.location == 'D5: Temple' and not zonemap['D5: Temple']['SOLVED']:
      use_elixr(myPlayer, elixr)
      zonemap['D5: Temple']['SOLVED']= True
      
    if myPlayer.location == 'E1: Swamplands' and not zonemap['E1: Swamplands']['SOLVED']:
      ogre_battle(myPlayer, ogre)
      zonemap['E1: Swamplands']['SOLVED']= True
      
    if myPlayer.location == 'E2: Elf Village' and not zonemap['E2: Elf Village']['SOLVED']:
      use_wand(myPlayer, wand)
      zonemap['E2: Elf Village']['SOLVED']= True
      
    #nothing in zone 'e3'
    #nothing in zone 'e4'
    #nothing in zone 'e5'

# GAME FUNCTIONALITY
def setup_game():
  os.system('clear')
  intro1 = "You awaken in a cold sweat." + '\n'
  for character in intro1:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)
    
  intro2 = "As you sit up, kicking your blankets off, you come to your senses." + '\n'
  for character in intro2:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)

  intro3 = "A voice booms around you." + '\n'
  for character in intro3:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)

  intro4 = "WHAT IS YOUR NAME, YOUNG ONE?" + '\n'
  for character in intro4:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.1)
  player_name = input("> ")
  myPlayer.name = player_name

  intro5 = player_name + "? INTERESTING NAME." + '\n'
  for character in intro5:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.1)

  intro6 = "THIS WORLD IS DANGEROUS." + '\n'
  for character in intro6:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.1)

  intro7 = "ARE YOU SURE YOU WANT TO CONTINUE?" + '\n'
  for character in intro7:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.1)
  user_input= input("> ")
  if user_input in ['yes', 'Yes', 'YES', 'y']:
    print('GOOD.')
    time.sleep(2)
    print('WELCOME TO FADING VALE.' + '\n')
    time.sleep(5)
    print('You look around and can see you are in your room.')
    time.sleep(2)
  elif user_input in ['no', 'NO', 'n', 'No']:
    print('Goodbye.')
    sys.exit()
  else: 
    print("I don't understand. Please try again." + '\n')
    time.sleep(2)
    user_input= input("> ")
    if user_input in ['yes', 'Yes', 'YES', 'y']:
      print('GOOD.')
      time.sleep(2)
      print('WELCOME TO FADING VALE.' + '\n')
      time.sleep(4)
      os.system('clear')
      print('You look around and can see you are in your room.')
      time.sleep(2)
    elif user_input in ['no', 'NO', 'n', 'No']:
      print('Goodbye.')
      sys.exit()

os.system('clear')

#execute the game!#
title_screen()
main_game_loop()


