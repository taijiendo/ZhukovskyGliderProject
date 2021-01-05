# About this project

This project is an attempt to determine various 
parameters of interest in paper glider flight using video-based data gathering
using the physics modeling tool 'Tracker' and using ODEs derived by Zhukovsky
and described in the book [Theory of Oscillators](http://pi.math.cornell.edu/~rand/randdocs/classics/zhukovski.pdf).


# Repo stucture

-Initial data visualisation is done in data_vis.py. 

-Numerical integration of these equations and their calibration to the data
are found in odes.py, solve_odes.py and calibrate_vis.py.

-.trk files can be viewed by downloading Tracker and opening these files in Tracker.

-.txt files contain csv data corresponding to speed and angle data gathered in Tracker.

-.mp4 files contain video of paper glider flights which have been loaded into Tracker
and data gathered. 

  