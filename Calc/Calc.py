#################################################################################################
## Calculate Pi using Monte Carlo
### class: Calc
#################################################################################################

import numpy as np

class Calc:
    # Constructor
    def __init__(self,point_data,R):
        # Member Variables
        self.point_data = point_data
        self.R = R
        self.cntr_in = 0
        self.cntr_out = 0
        
        
        ## VV IMPORTANT
        # Python creats a pointer on the points list defined in the main file
        # If the points list is modified here, the original list is also modified
        # since lists are mutable objects
        # Since we can modify the points list from here only, it is not necessary to
        # return it to the main file
        # Using pointers help in storing memory since no new list needs to be created
        
    def run(self):
        
        # ALternate?: Vectorized Computation (faster and takes fewer lines)
        # For loop not used
        
        for i in range(0,len(self.point_data)):
            # Distance of the point from the origin
            dist = np.sqrt(self.point_data[i].x*self.point_data[i].x + self.point_data[i].y*self.point_data[i].y)
            
            # Comparing the distance with the radius
            if dist > self.R:
                self.cntr_out = self.cntr_out + 1
            else:
                self.cntr_in = self.cntr_in + 1
                
                
            
    # Evaluate Probabilty
    def eval_probabilty(self):
        return float(self.cntr_in)/float(self.cntr_in + self.cntr_out)