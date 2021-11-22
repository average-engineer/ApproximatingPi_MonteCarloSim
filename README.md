# ApproximatingPi_MonteCarloSim

***A data driven approach for estimating the value of Pi***.

This apporach was covered in my class of ***Computational Intelligence in Engineering*** which I am taking in the first semester of my master's degree at RWTH Aachen University. We make the use of the *Montel Carlo* simulation to estimate the value of pi. One of the most important features of this repository is that the the whole code is object oriented.

***Brief Description of the program files***
* `main.py`: Mother script which is executed and calls all classes and functions
* `point.py`: Class for a point object. Since we are using Monte Carlo Simulation, we generate a lot of random points and each of these points are a point object. 
* `vis.py`: Class for creating visual objects which help us in creating visualisations of the randomised points in 2D space
* `calc.py`: Class for creating the object which makes the final computation of pi.
