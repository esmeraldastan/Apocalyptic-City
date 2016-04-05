# -*- coding: utf-8 -*-
import sys
import random
import time 

inventory = []
#Into to the game 
time.sleep(0.5)
print "Welcome to Apocalyptic City\n"
print "Your obective in this game will be to get out of\nthe building to saftey.\n"  

node = None 

#INVENTORY
def addToInventory(item):
    inventory.append(item)
    global invenotory

    
#player status 
class player(object):
    
    def __init__(self, name, health):
        self.name = name 
        self.health = health 
        
class single_player(player):
    def __init__(self, name, health = 49800):
        super(single_player, self).__init__(name, health = 49800)
        
me = single_player(player)        
        
#ITEMS     
class Item(object):
    def __init__(self, name):
        self.name = name
        
#CONSUMABLES   

#SUBCLASS
class Consumable(Item):
    
    def __init__(self, name, health):
        super(Consumable, self).__init__(name)
        self.health = health
        
class health_potion(Consumable):
    def __init__(self, name, health = 200):
        super(health_potion, self).__init__(name, health = 200)
        
health = health_potion(Consumable)    
    
class Building:#start of the map 

    def __init__(self, name, description, up, down, north, east, south, west, right, left, outside, inside):
        self.name = name
        self.description = description
        self.up = up
        self.down = down
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.right = right
        self.left = left
        self.outside = outside 
        self.inside = inside 
        
    def move(self, direction):
        global node 
        node = globals()[getattr(self, direction)]
        
print 'You have woken up from a long sleep. The last thing you remember was escaping\nthe white gas that was spreading throughout the city.' 
                   
#BUILDING

#THIRD FLOOR            
Office = Building("Office", 'Papers are shattered everywhere. The lights are\nflashing on and off. There next to you is a light blue paper. Type "pick up" to read what it says.', None, None, 'Conference', 'Secutary', None, None, None, None, None, None)
Conference = Building("Conference Room", 'You are now standing in the Conference Room. A couple of bodies are laying around. Rottening with a nasty smell. There\'s a flashlight on the table. Pick it up...you might need it later on.\n>yes\n>no\n\nHead "east"', None, None, None, 'Elevator', 'Office',None, None, None, None, None)
Elevator = Building("Elevator", 'In the Elevator head down to continue getting to your destination. Type "down".But wait before that you you need to restore to full health.There is a green cyrum laying on the grown. Type "restore" this will get you to full health. ', None, 'Elevator2', None, None, 'Secutary Desk',None, None, None, None, None)
Stairs = Building("Stairs", 'The walls are coverd with blood. You are not alone. Zombies and infecteds run the area now. You don\'t want to encounter with one ...it can be your end.To go down the stairs type down to go on to the next floor.There is blood covering the walls….Bodies laying down with body parts missing. Be careful.  ', None, 'Stairs1', None, None, None,None, None, None, None, None)
Secutary = Building("Secutary Desk",' You are standing next to your securary\'s desk. A flash light stands on top. Pick it up you might need it later on. Head "north" to the elevator or "east" to the stairs.', None, None, 'Elevator', None, None , None, None, None, None, None)

node = Office


    
#RUN THROUGH THE MAP 
while True:
    print "Room: " + node.name
    print 
    print "Description: " + node.description 
    
    #WORD DEFINE
    infected = "A person who had been contaminated by the gas"
    zombie = 'A dead person risen from the dead.The chemicals within the gass had an effect on the dead makeing them come back to life'
    restore = ['restore']
    response = ['up', 'down', 'north', 'east', 'south', 'west', 'right', 'left', 'outside', 'inside'] 
    pick = ['pick up']
    

    
    command = raw_input('>').strip().lower()

 

    
    #QUITE THE PROGRAM 
    if command in ['q', 'exit', 'quit']:
        sys.exit(0)
        
    #paper read out 
    if command in pick:
        print '*Escape to the labatory hidden under the an old facotry building.It should be located a couple\nof blockswest of where you are located.*'
        print 
        print 'Head "north" or "east"'
        
    #MOVE INTO DIFFERNT ROOMS 
    if command in response:
        try:
           node.move(command)
        except:
           print 'You can\'t do that way! '  
           
           
    if command in restore:
        status = me + health
    print  

        #INVENTORY FOR ITEMS/WEAPONS
        
       
    if command == "yes":
        addToInventory("flash light")
        print (inventory)
    print
    
   

'''# door 

print "Figure out the password in order to open the door."

password = "3546", "5515", "1651", "4539" #passwords to open up the doors 
wordIndex = random.randint(0,len(password)-1)
code_rip = password[wordIndex]
user_guesses = ''
turns = 10 #the player will have only 10 times to try to figure out the code


while turns > 0:
       left = 0
       for number in code_rip:
         if number in user_guesses:
            print number,
         else:
            print "#",
            left += 1
       if left == 0:
            print
            print
            print "Excellent, move on."# move into the next room 
                
            break
        
       print 
        
       guess = raw_input("Guess the four Numbers:")
       if guess in ['q','quit','exit']:
            sys.exit(0)
       user_guesses += guess 
       if guess not in code_rip:
            turns -=1
            print "Sorry number not in the secret code. \n\n Please try again"
            print "You have", +turns, 'left'
       if turns == 0:
            print "Sorry you lose"#change
       
'''

        