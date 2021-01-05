from solve_odes import *
import matplotlib.pyplot as plt
def speed_ode_model(save):
    ''' Solves the speed ODE and displays calibrated solution

        Parameters
        ----------
		save : Bool
			If set to true, save both figures generated to working directory

        Returns
        -------
    '''
    # load speed data - to calibrate parameters
    t, v, theta = load_data()
        
    # use CURVE_FIT to find "best" model
    from scipy.optimize import curve_fit
    pars = curve_fit(v_ode_solve, t, v, [0.0241,0.15, 0.005, 1.2], bounds=([0, 0, 0, 0],[np.inf, np.inf, np.inf, np.inf]))[0]

    # plot the best solution
    vm = v_ode_solve(t,*pars)
    f,ax = plt.subplots(1,1, constrained_layout=True)
    ax.plot(t, v, 'ro', label = 'observations')
    ax.plot(t, vm, 'b-', label='model')
    ax.set_ylabel("Speed [m/s]",size=14); ax.set_xlabel("time[s]",size=14)
    ax.legend(prop={'size':14})
    ax.set_title('$F$={:2.2e},   $C_x$={:2.2e},   $m$={:2.2e},  $\\rho$={:2.2e}'.format(pars[0],pars[1],pars[2],pars[3]),size=14)
    f.suptitle("Best-fit speed ODE",size=15)

    save_figure = save
    if not save_figure:
        #Open a new window and display the plot
        plt.show()
    else:
        #Save that plot to a png file
        plt.savefig('speed_calibrate.png',dpi=300)


def angle_ode_model(save):
    ''' Solves the angle ODE and displays calibrated solution

        Parameters
        ----------
		save : Bool
			If set to true, save both figures generated to working directory

        Returns
        -------
    '''
    # load speed data - to calibrate parameters
    t, v, theta = load_data()

    e=np.finfo(float).eps    
    # use CURVE_FIT to find "best" model
    from scipy.optimize import curve_fit
    pars = curve_fit(theta_ode_solve, t, theta, [0.01,0.15, 0.005, 1.2], bounds=([0, 0, 0, 0],[np.inf, np.inf, np.inf, np.inf]))[0]

    # plot the best solution
    thetam = theta_ode_solve(t, *pars)
    f,ax = plt.subplots(1,1, constrained_layout=True)
    ax.plot(t, theta, 'ro', label = 'observations')
    ax.plot(t, thetam, 'b-', label='model')
    ax.set_ylabel("Angle [degrees]",size=14); ax.set_xlabel("time[s]",size=14)
    ax.legend(prop={'size':14})
    ax.set_title('$F$={:2.2e},   $C_x$={:2.2e},   $m$={:2.2e},  $\\rho$={:2.2e}'.format(pars[0],pars[1],pars[2],pars[3]),size=14)
    f.suptitle("Best-fit angle ODE",size=15)

    save_figure = save
    if not save_figure:
        #Open a new window and display the plot
        plt.show()
    else:
        #Save that plot to a png file
        plt.savefig('angle_calibrate.png',dpi=300)

if __name__ == "__main__":
    speed_ode_model(save=False)
    angle_ode_model(save=False)