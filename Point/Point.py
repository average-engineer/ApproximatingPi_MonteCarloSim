#################################################################################################
## calculate pi
### class: point
# Point Object: Concrete Instance of the Point Class Point.py
#################################################################################################

import random # Importing random module

class Point: # Nothing in parenthesis so there seems to be no base class/super class
    # Constructor: The first function which is (and must be) called in a class -> builds the object (instance of the object)
    # def-> defining a function in python. 
    def __init__(self,number,radius): # initialise(the object initialises itself,object number,the bounded radius)
        # __init__ is the class constructor
        # Member Variables (Instance Variables/Fields->States of the object)
        self.number = number # even if the function has finished running, this variable survives
        self.radius = radius # second member variable (instance variable)
        self.x = 0.0 # x coordinate of the point
        self.y = 0.0 # y coordinate of the point    
        # print('This is the class point')
        
    
    
    # Object Method/Instance Methods# New Member Function/object method
    # For random sampling 
    def sample(self): # The input is the point object itself
    # random.random() gives a random number between 0 and 1    
        self.x = random.random()*self.radius # this gives a random number between 0 and R
        self.y = random.random()*self.radius
        
        
    def print_me(self):
        print('## Point Info: ',self.number,self.radius)
        print('x: ',self.x)
        print('x: ',self.y)