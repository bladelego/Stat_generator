
#this is an importation of the random number generator
import random

#getting important stuff from the player
player_class = input('what class shall you play: ')
race = input('what race shall you play: ')

#switch name to drow
if race == 'dark elf':
    race = 'drow'


#a simple comment


#creating an empty stat list
stats = []

while len(stats) < 6:
#rolling 4 dice
    rolls = []
    roll1 = random.randint(1,6)
    rolls.append(roll1)
    roll2 = random.randint(1,6)
    rolls.append(roll2)
    roll3 = random.randint(1,6)
    rolls.append(roll3)
    roll4 = random.randint(1,6)
    rolls.append(roll4)
    
    #get rid of the smallest result
    rolls.sort()
    rolls.pop(0)


    stat = sum(rolls)
    stats.append(stat)


#sorting the stats
stats.sort()
print (stats)

if player_class == 'fighter':
#assign base stats
    strength = stats[5]
    constitution = stats[4]
    dexterity = stats[3]
    charisma = stats[2]
    wisdom = stats[1]
    intelligence = stats[0]

if player_class == 'wizard':
#assign base stats
    intelligence = stats[5]
    dexterity = stats[4]
    charisma = stats[3]
    constitution = stats[2]
    wisdom = stats[1]
    strength = stats[0]
    


#modify the stats based on race
    
if race == 'human':
    strength = strength + 1
    dexterity = dexterity + 1
    constitution = constitution + 1
    intelligence = intelligence + 1
    wisdom = wisdom + 1
    charisma = charisma + 1

if race == 'mountain dwarf':
    strength = strength + 2
    constitution = constitution + 2

if race == 'hill dwarf':
    constitution = constitution + 2
    wisdom = wisdom + 1

if race == 'high elf':
    dexterity = dexterity + 2
    intelligence = intelligence + 1

if race == 'wood elf':
    dexterity = dexterity + 2
    wisdom = wisdom + 1

if race == 'drow':
    dexterity = dexterity + 2
    charisma = charisma + 1

if race == 'lightfoot halfling':
    dexterity = dexterity + 2
    charisma = charisma + 1

if race == 'stout halfling':
    dexterity = dexterity + 2
    constitution = constitution + 1

if race == 'dragonborn':
    strength = strength + 2
    charisma = charisma + 1

if race == 'forest gnome':
    dexterity = dexterity + 1
    intelligence = intelligence + 2

if race == 'rock gnome':
    constitution = constitution + 1
    intelligence = intelligence + 2

if race == 'half-elf':
    charisma = charisma + 2
    if player_class == 'fighter':
        strength = strength + 1
        constitution = constitution + 1
        #add the rest of the classes here when ready

if race == 'half-orc':
    strength = strength + 2
    constitution = constitution + 1

if race == 'teifling':
    intelligence = intelligence + 1
    charisma = charisma + 2

    


#show the player the numbers
print ('your strength is:')
print (strength)
print ('your dexterity is:')
print (dexterity)
print ('your constitution is:')
print (constitution)
print ('your intelligence is:')
print (intelligence)
print ('your wisdom is:')
print (wisdom)
print ('your charisma is:')
print (charisma)
