from data_vis import load_data
from odes import *
from scipy.interpolate import interp1d

# implement an improved Euler step to solve the ODE
def v_ode_solve(t, F, Cx, m, rho):
    ''' Solve an ODE numerically for the glider system

        Parameters:
        -----------
        t : float
            times for which solution is needed.
        F : float
            wing area parameter.
        Cx : float
            drag coeff. parameter. 

        Returns:
        --------
        v_soln : array-like
            Dependent variable solution vector corresponding to times in t.

        Notes:
        ------
        ODE is solved using the Improved Euler Method.
        A data txt file called data.txt MUST be present in
        the working directory for this function to run. 


        Assume that ODE function f takes the following inputs, in order:
            1. dependent variable
            2. independent variable
            3. other parameters
    '''

    # load pressure data - to get the initial value
    tv,v, theta = load_data()

    # initial value
    vm = [v[0],]                            
        # solve at pressure steps
    for t0,t1 in zip(tv[:-1],tv[1:]):          
        # predictor gradient
        dvdt1 = v_ode(vm[-1], t0, F, Cx, m, rho)
        # predictor step
        vp = vm[-1] + dvdt1*(t1-t0)
        # corrector gradient
        dvdt2 = v_ode(vp, t1, F, Cx, m, rho)
        # corrector step
        vm.append(vm[-1] + 0.5*(t1-t0)*(dvdt2+dvdt1))
    
    # interp onto requested times

    vsoln_splines=interp1d(tv,v,kind='cubic')
    #interp1d creates a function which can be fed interpolation points stored in t
    v_soln = vsoln_splines(t)

    return np.interp(t, tv, vm)

# implement an improved Euler step to solve the ODE
def theta_ode_solve(t, F, Cy, m, rho):
    ''' Solve an ODE numerically for the glider system

        Parameters:
        -----------
        t : float
            times for which solution is needed.
        F : float
            wing area parameter.
        Cy : float
            lift coeff. parameter. 

        Returns:
        --------
        v_soln : array-like
            Dependent variable solution vector corresponding to times in t.

        Notes:
        ------
        ODE is solved using the Improved Euler Method.
        A data txt file called data.txt MUST be present in
        the working directory for this function to run. 


        Assume that ODE function f takes the following inputs, in order:
            1. dependent variable
            2. independent variable
            3. other parameters
    '''

    # load pressure data - to get the initial value
    ttheta,v, theta = load_data()

    # initial value
    thetam = [theta[0],]                            
        # solve at pressure steps
    for t0,t1 in zip(ttheta[:-1],ttheta[1:]):          
        # predictor gradient
        dthetadt1 = theta_ode(thetam[-1], t0, F, Cy, m, rho)
        # predictor step
        thetap = thetam[-1] + dthetadt1*(t1-t0)
        # corrector gradient
        dthetadt2 = theta_ode(thetap, t1, F, Cy, m, rho)
        # corrector step
        thetam.append(thetam[-1] + 0.5*(t1-t0)*(dthetadt2+dthetadt1))
    
    # interp onto requested times  
    return np.interp(t, ttheta, thetam)