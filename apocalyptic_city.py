import sys

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

        