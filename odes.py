import numpy as np
from data_vis import load_data
from scipy.interpolate import interp1d

def v_ode(v, t, F, Cx, m, rho):
    ''' Return the derivative dv/dt at time, t, for given parameters.

        Parameters:
        -----------
        v : float
            speed(dependent variable).
        t : float
            time(independent variable).
        theta : float
            angle to horiz.
        F : float
            wing area parameter.
        Cx : float
            drag coeff. parameter.      

        Returns:
        --------
        dvdt : float
            Derivative of velocity with respect to time.

        Notes:
        ------
        Based on N.I. Zhukovskii's glider ODE's.
        theta must be in units degrees, t in units seconds
    '''
    # since glider made out of one sheet of A4 paper it will weigh 5g
    #m = 0.005 # SI units
    #rho = 1.2 # air density

    # interpolate on theta if data point not available
    tv, vdat, thetav = load_data()
    theta = np.interp(t, tv, thetav)

    #theta_splines=interp1d(tv,thetav,kind='cubic')
    #interp1d creates a function which can be fed interpolation points stored in t
    #theta = theta_splines(t)


    dvdt = -9.81*np.sin(theta*np.pi/180) - (0.5*rho*F*Cx*(v**2))/m

    return dvdt

def theta_ode(theta, t, F, Cy, m, rho):
    ''' Return the derivative dtheta/dt at time, t, for given parameters.

        Parameters:
        -----------
        theta : float
            angle to horiz(dependent variable).
        t : float
            time(independent variable).
        v : float
            speed.
        F : float
            wing area parameter.
        Cx : float
            lift coeff. parameter.      

        Returns:
        --------
        dthetadt : float
            Derivative of angle wrt horiz with respect to time.

        Notes:
        ------
        Based on N.I. Zhukovskii's glider ODE's.
        theta must be in units degrees, t in units seconds
    '''
    # since glider made out of one sheet of A4 paper it will weigh 5g
    #m = 0.005 # SI units
    #rho = 1.2 # air density

    # interpolate on theta if data point not available
    tv, vdat, thetav = load_data()
    v = np.interp(t, tv, vdat)

    #v_splines=interp1d(tv,vdat,kind='cubic')
    #interp1d creates a function which can be fed interpolation points stored in t
    #v = v_splines(t)

    dthetadt = -(9.81*np.cos(theta*np.pi/180))/(v)+(0.5*rho*F*Cy*v)/m

    return dthetadt
