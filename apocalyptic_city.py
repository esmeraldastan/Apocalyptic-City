import sys
import random

#Into to the game 
print "Welcome to Apocalyptic City\n"
print "Your obective in this game will be to get out of\nthe building to saftey outside the city.\n"  

node = None 

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
        
print 'You have woken up form a long sleep. The last thing you remember was escaping the white gass that was spreading throughout the city.' 


        
# door 

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
       


        