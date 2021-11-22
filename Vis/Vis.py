#################################################################################################
## Visualise Data
### class: Vis
#################################################################################################

import matplotlib.pyplot as plt
import numpy as np

class Vis:
    def __init__(self,point_data):
        self.point_data = point_data
        self.point_size = 3
        self.point_color = 'blue'
        self.numplotcircle = 100 # Number of steps required for plotting the circle
        self.linewidth = 2
        self.col_circle = 'black'
        
     # Method for developing a figure window
    def define_fig(self):
        fig = plt.figure(figsize = (10,10))
            
    def plot_samples(self):
        for i in range(0,len(self.point_data)):
            plt.plot(self.point_data[i].x,self.point_data[i].y,'o',markersize =self.point_size,color = self.point_color)
            plt.axis('equal') # Equally Sized Axes (the same tick sizes)
            plt.draw() # Equivalent to hold on in MATLAB
            
    def plot_circle(self,R):
        x_vec = np.linspace(0.0,R,self.numplotcircle)
        R_vec = np.ones(self.numplotcircle)*R # R repeated as many times as the number of steps
        y_vec = np.sqrt(np.power(R_vec,2) - np.power(x_vec,2)) # Circle Locus
        
        # Plotting circle
        plt.plot(x_vec,y_vec,linewidth = self.linewidth,color = self.col_circle)
        plt.axis('equal') # Equally Sized Axes (the same tick sizes)
        plt.draw()