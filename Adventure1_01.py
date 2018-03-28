# text adventure using a dictionary

import time

# set up data

rooms = {'stonechamber': {'name': 'a stone chamber', 'north': 'laboratory', 'east': 'guardroom',
    'contents': ['sword', 'torch'], 'monster': [], 'text': 'The walls are made of rock, a torch flickers on the wall. \nThere is a door to the North and a passage to the East.'},
    'guardroom': {'name': 'a guardroom', 'west': 'stonechamber', 'north': 'smallcavern', 'east': 'library', 'contents': [], 'monster': [],
    'text': 'A few broken chairs and tables are strewn about the room. There are passages to the North, West and East.'},
    'library': {'name': 'an ornate library', 'west': 'guardroom', 'north': 'refrectory', 'east': 'chapel', 'contents': ['spellbook'], 'monster': [],
    'text': 'Dusty volumes fill the shelves. There is an ornate table with some volumes lying there. \nYou can see passages to the North, West and East.'},
    'chapel': {'name': 'a dismal chapel', 'north': 'largehall', 'west': 'library',
    'contents': ['holywater', 'crucifix'], 'monster': [], 'text': 'Tattered drapes hang from the walls and there is a small, stone alter. \nThere are passages to the North and West.'},
    'laboratory': {'name': 'a disused laboratory', 'north': 'dungeon', 'south': 'stonechamber', 'contents': ['potion'], 'monster': [],
    'text': 'Glass ampules and test-tubes lie broken on the floor. There is the strange smell of old \nchemycals hanging in the air. An exit leads North and a passage goes to the South.'},
    'smallcavern': {'name': 'a small cavern', 'south': 'guardroom', 'east': 'refrectory', 'contents': [], 'monster': ['Goblin'], 'text': 'It is dark and musty, water drips from the ceiling. \nYou can make out exits to the South and East'},
    'refrectory': {'name': 'a refrectory', 'north': 'amphitheatre', 'west': 'smallcavern', 'south': 'library', 'contents': ['bread'], 'monster': [],
    'text': 'Mouldy food lies festering on large tables, long abandoned. \nWine stains cover the floor like old, congealed blood. Exits are to the North, West and South.'},
    'largehall': {'name': 'a large hall', 'north': 'conservatory', 'south': 'chapel', 'contents': [], 'monster': ['Necromancer'],
    'text': 'Ornate stone columns, richly carved march down the length of this vast room. \nThere is a huge, dusty fireplace to the right, full of the ash of burned bones. \nThere is a passage to the North and a stone doorway to the South.'},
    'dungeon': {'name': 'a dank dungeon', 'north': 'graveyard', 'south': 'laboratory', 'east': 'armoury', 'contents': ['skull'], 'monster': [],
    'text': 'The sound of dripping echoes off the walls and there is the constant odour \nof ancient death. There is nothing of interest here, except fear. There are \ndark passages leading out to the North, South and East.'},
    'armoury': {'name': 'an armoury', 'north': 'glitteringcave', 'west': 'dungeon', 'east': 'amphitheatre', 'contents': ['axe'], 'monster': [],
    'text': 'The broken remains of ancient suits of armour hang from the solid walls. Old weapons \nlie about discarded. In the gloom you can make out passages to the North, West and East.'},
    'amphitheatre': {'name': 'a vast amphitheatre', 'north': 'tavern', 'west': 'armoury', 'south': 'refrectory', 'east': 'conservatory',
    'contents': [], 'monster': ['Vampire'], 'text': 'Stone seats encirle a wide space where players once performed for crowds long gone, or perhaps gruesome executions \nwere enacted here. There are exits on all four sides.'},
    'conservatory': {'name': 'an ornate glass conservatory', 'north': 'hugecavern', 'west': 'amphitheatre', 'south': 'largehall',
    'contents': ['herbs'], 'monster': [], 'text': 'Many panes of glass lie shattered on the floor, and the cold air makes you shiver. However you cannot \nsee outside. The exits are to the North, West and South.'},
    'graveyard': {'name': 'an eldritch graveyard', 'south': 'dungeon', 'east': 'glitteringcave', 'contents': [], 'monster': ['Ghoul'],
    'text': 'Moss covered stones stand in uneven rows with barely readable inscriptions, \nsome have been wrenched over and are cracked apart. A peculiar mist writhes between the stones \nand you can just about see the way East and to the South.'},
    'glitteringcave': {'name': 'a glittering cave', 'west': 'graveyard', 'south': 'armoury', 'east': 'tavern', 'contents': ['gem'], 'monster': [],
    'text': 'Gem encrusted stalagtites and stalagmites fill this mighty cave, the site takes \nyour breath away. Cave tunnels lead out to the West, East and South.'},
    'tavern': {'name': 'a dusty tavern', 'west': 'glitteringcave', 'south': 'amphitheatre', 'east': 'hugecavern', 'contents': ['ale'], 'monster': [],
    'text': 'A musty smell of old spirits pervades the air. Cracked glasses and tarnished goblets still stand on the bar top. \nThe could be something tasty tucked away behind the bar!'},
    'hugecavern': {'name': 'a huge cavern', 'west': 'tavern', 'south': 'conservatory', 'contents': ['gold'], 'monster': ['Dragon'],
    'text': 'This is a mighty cavern indeed. The walls rise sheer to an unknown height \nand your gasp echoes back fearfully.'}}

directions = ['north', 'south', 'east', 'west']
current_room = rooms['stonechamber']
carrying = []
slain = []
currentmonster = ""
hp = 30

def briefpause(t):
    print()
    time.sleep(t)


print("*** WELCOME TO THE ADVENTURE! ***")
briefpause(1)
print('You start with ' + str(hp) + ' hp.')

# start of the game loop

while True:
    # display the current location
    briefpause(1)
    print('You are in {}.'.format(current_room['name']))
    briefpause(1)
    print(current_room['text'])
    # display moveable contents
    if current_room['contents']:
        briefpause(1)
        print('You find: {}'.format(', '.join(current_room['contents'])))
    # display monsters
    if current_room['monster']:
        currentmonster = ' '.join(current_room['monster'])
        briefpause(1)
        print('There is a {} here!! You lose 5 hp'.format(' '.join(current_room['monster'])))
        hp = hp -5
        if hp == 0:
            briefpause(1)
            print("You are DEAD!! Game Over.")
            break

    # get the users input
    briefpause(1)
    command = input('\nMake your choice! ').strip()

    # how to move
    if command in directions:
        if command in current_room:
            current_room = rooms[current_room[command]]
        else:
            # can't move
            briefpause(1)
            print("You can't go in that direction.")

    # exit the game
    elif command.lower() in ('q', 'quit'):
        briefpause(1)
        print("Thanks for playing!")
        break

    # pick up objects
    elif command.lower().split()[0] == 'get':
        if len(command) <= 3:
            briefpause(1)
            print("That's not a valid command.")
        else:
            item = command.lower().split()[1]
            if item in current_room['contents']:
                if item == "gold":
                    if current_room == rooms['hugecavern']:
                        slainmonster = ' '.join(slain)
                        if "Dragon" in slainmonster:
                            briefpause(1)
                            print("You take the gold from slain dragon! You have WON!!")
                            break
                        else:
                            briefpause(1)
                            print("You can't take the gold while the dragon is alive!")
                else:                                      
                    current_room['contents'].remove(item)
                    carrying.append(item)
                    briefpause(1)
                    print("You pick up the " + (item))
            else:
                briefpause(1)
                print("That item is not here.")

    # drop objects
    elif command.lower().split()[0] == 'drop':
        if len(command) <= 4:
            briefpause(1)
            print("That's not a valid command.")
        else:
            item = command.lower().split()[1]
            if item in carrying:
                current_room['contents'].append(item)
                carrying.remove(item)
                briefpause(1)
                print("You drop the " + (item))
            else:
                briefpause(1)
                print("You aren't carrying that.")

    # eat item
    elif command.lower().split()[0] == 'eat':
        if len(command) <= 3:
            briefpause(1)
            print("That's not a valid command.")
        else:
            fooditem = command.lower().split()[1]
            if fooditem in carrying:
                carry = ' '.join(carrying)
                if "bread" in carry:
                    briefpause(1)
                    print ("You eat the " + (fooditem) + " and restore 5 hp.")
                    hp = hp + 5
                    carrying.remove(fooditem)
                else:
                    briefpause(1)
                    print("You can't eat that item.")
            else:
                briefpause(1)
                print("You can't eat that as you aren't carrying it.")


    # drink item
    elif command.lower().split()[0] == 'drink':
        if len(command) <= 5:
            briefpause(1)
            print("That's not a valid command.")
        else:
            drinkitem = command.lower().split()[1]
            if drinkitem in carrying:
                carry = ' '.join(carrying)
                if "ale" in carry:
                    briefpause(1)
                    print ("You drink the " + (drinkitem) + " and restore 10 hp.")
                    hp = hp + 10
                    carrying.remove(drinkitem)
                else:
                    if "holywater" in carry:
                        briefpause(1)
                        print ("You drink the " + (drinkitem) + " and restore 15 hp.")
                        hp = hp + 15
                        carrying.remove(drinkitem)
                    else:
                        briefpause(1)
                        print("You can't drink that item.")
            else:
                briefpause(1)
                print("You can't drink that as you aren't carrying it.")

    # use item
    elif command.lower().split()[0] == 'use':
        if len(command) <= 3:
            briefpause(1)
            print("That's not a valid command.")
        else:
            useitem = command.lower().split()[1]
            if useitem in carrying:
                use = ' '.join(carrying)
                if useitem == "sword":
                    if currentmonster == "Goblin":
                        briefpause(1)
                        print("You slay the goblin with the sword!")
                        current_room['monster'].remove("Goblin")
                        slain.append("Goblin")
                elif useitem == "potion":
                    if currentmonster == "Ghoul":
                        briefpause(1)
                        print("You throw the potion at the ghoul and it dies, screaming!")
                        current_room['monster'].remove("Ghoul")
                        slain.append("Ghoul")
                elif useitem == "spellbook":
                    if currentmonster == "Necromancer":
                        briefpause(1)
                        print("You cast a spell at the necromancer and he evaporates!")
                        current_room['monster'].remove("Necromancer")
                        slain.append("Necromancer")
                elif useitem == "crucifix":
                    if currentmonster == "Vampire":
                        briefpause(1)
                        print("You show the crucifix to the vampire and he melts!")
                        current_room['monster'].remove("Vampire")
                        slain.append("Vampire")
                elif useitem == "axe":
                    if currentmonster == "Dragon":
                        briefpause(1)
                        print("You swing the axe with all your might at the dragon and it dies!")
                        current_room['monster'].remove("Dragon")
                        slain.append("Dragon")                      
            else:
                briefpause(1)
                print("You cannot do that here.")


    # show inventory
    elif command.lower() == 'inv':
        carry = ' '.join(carrying)
        briefpause(1)
        print ("You are carrying: " + (carry))

    # show kills
    elif command.lower() == 'kills':
        kills = ' '.join(slain)
        briefpause(1)
        print ("You have slain: " + (kills))

    # show help
    elif command.lower() == 'help':
        briefpause(1)
        print ("To move, type the direction for example \"south\". To pick up an object type \"get\" and to drop the object type \"drop\".")
        print ("To list the items you are carrying type \"inv\". To show your hit points, type \"hp\". To quit type \"quit\" or \"q\".")
        print ("To eat an item type \"eat\". To drink an item type \"drink\". To see monsters killed type \"kills\".")

    # show hp
    elif command.lower() == 'hp':
        briefpause(1)
        print('You have ' + str(hp) + ' hp left.')

    # unknown command
    else:
        briefpause(1)
        print("That's not a valid command.")

