#################################################################################################
## calculate pi
### Main File -> Main Executable File (Mother Script)
# Calls the other functions and classes
#################################################################################################

print('######## loading interval libraries ########')

# Data driven methodology to compute pi (3.14)
# MONTE CARLO SIMULATION: used to compute Pi (data driven method)

# including libraries of python

import numpy as np # importing numpy
import matplotlib.pyplot as plt # pyplot method of matplotlib module imported only
# from matplotlib import pyplot as plt

# from folder.scriptname import class
from Point.Point import Point # Importing class for point object
from Vis.Vis import Vis # Importing class for visualising data
from Calc.Calc import Calc # Importing the class object

print('\n### Starting Program ###')
num_samples = 1000
R = 1.0 # Radius over whoch the random points are distributed
point_list = [] # Empty list which will store all the random points 
# Reminder: A single list can store multiple types of objects (for eg, integer, floating point, string etc)

print('\n### Collecting Data ###')
for i in range(0,num_samples):
    pt = Point(i,R) # Creating as many point objects as many as samples/random points needed
    # For collecting all the points, we need to store each point object in a list (which can store
    # different types of objects)
    pt.sample() # Random Sampling
    point_list.append(pt) # Appending to the empty list
    
# print(point_list)

num = 5 # Sample random point

# Since each member of point_list is a point object, all members will possess the 
# fields/variables and the methods/functions defined for the point obj
print(point_list[num].number) # 38th element of the list-> 38th point object
# Expected Output: 37 
print('x:',point_list[num].x)    
print('y:',point_list[num].y)
point_list[num].print_me() # Information about the point

print('\n#### Plot Data ####')
Visual = Vis(point_list)
Visual.point_size = 5 # The point size field of the class can be varied globally too
Visual.col_circle = 'red' # The circle color field can be changed globally too
Visual.define_fig()
Visual.plot_samples()
Visual.plot_circle(R)

    
# pt = Point(1984,22.3) # pt is a new Point Object
# print('Number of the point: ', pt.number)
# print('Radius of the point: ',pt.radius)
# print('x.coord: ', pt.x)
# print('y.coord: ', pt.y)


# STARTING THE COMPUTATION OF PI

print('\n#### Process the data and calculate Pi #####')
MC_eval = Calc(point_list,R)
MC_eval.run()
print('cntr_in: ',str(MC_eval.cntr_in))
print('cntr_out: ',str(MC_eval.cntr_out))

# Evaluating probability

print('\n### This is Pi: ',str(4*MC_eval.eval_probabilty()))

# Since the points are generated randomly everytime, the Monte Carlo method gives
# out a significantly different value of Pi for less number of Random Points 
# (The standard deviation of the computed Pi values are usually pretty high)


## ADVANTAGE OF MC Mthod:
    # It can handle highly non-linear problems since it is just a random hit and 
    # trial method
    
## DISADVANTAGE OF MC Method:
    # It requires a lot of data for it to predict stuff accurately
    
# As the random number of points increase, the estimate of the Monte Carlo method
# comes closer and clsoer to the actual value of Pi

# Life lesson from Monte Carlo Simulation: Keep doing random shit and you'll eventually
# achieve what you want in life.

print('......Done......')
