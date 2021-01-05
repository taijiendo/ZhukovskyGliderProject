# functions for data visualisation

import matplotlib.pyplot as plt
import os
import numpy as np
import pandas as pd

def load_data():
    ''' Returns time and conc measurements from conc csv file.

        Parameters:
        -----------
        none

        Returns:
        --------
        t : array-like
            Vector of times (s) at which measurements were taken.
        v : array-like
            Vector of speed measurements.
        theta : array-like
            Vector of angle to velocity vector wrt x-axis.    

        Notes:
        ------
        The file name of file containing the data is hard coded inside this function.
    '''
    #read data in from csv
    data=np.genfromtxt("VID_20210104_175453_2.txt", delimiter=',', skip_header=True)
    #data = pd.read_csv("data.csv")
    
    t=data[:,0]
    v=data[:,1]
    theta=data[:,2]
    theta = 180 + theta

    return t,v, -theta

def plot_data(save):
    ''' Generate a plots comparing speed & time, angle to horiz & time
        
        Parameters:
        -----------
        save : Bool
            If set to true, save BOTH figures generated to working directory

        Returns:
        --------
        None

        Notes:
        ------
    '''
    t,v,theta = load_data()

    #extraction vs conc
    fig, axv = plt.subplots()

    axv.plot(t, v, 'k')
    axv.set_ylabel('speed [m/s]')

    axtheta = axv.twinx()
    axtheta.plot(t, theta, 'b')
    axtheta.set_ylabel('$\\theta$ [degrees]')
    fig.legend(labels = ('Speed', 'Angle to horizontal $\\theta$'), loc=4,bbox_to_anchor=(1,0.45),bbox_transform=axv.transAxes)
    plt.title('Comparison of speed and angle to horizontal')

    #show the plot to the screen OR save the plot in the directory
    save_figure = save
    if not save_figure:
        #Open a new window and display the plot
        plt.show()
    else:
        #Save that plot to a png file
        plt.savefig('v_vs_theta.png',dpi=300)

if __name__ == "__main__":
    plot_data(save=False)
