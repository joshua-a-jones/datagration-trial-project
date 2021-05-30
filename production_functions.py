#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 30 2021

@author: joshuajones
"""

def exponential_equation(t, qi, di):
    """
    Parameters
    ----------
    t : Time since initial (can be numpy array)
    qi : Initial production rate. Float
    di : Nominal decline rate. Float

    Returns
    -------
    returns Q, the ecummulative production at time t

    """
    import numpy as np
    q = qi*np.exp(-di*t)
    
    return (qi - q)/di

def hyperbolic_equation(t, qi, b, di):
    """
    Parameters
    ----------
    t : time since initial (can be numpy array)
    qi : Initial production rate. Float
    b : hyperbolic decline constant. Float
    di : Nominal decline rate at t = 0.

    Returns
    -------
    returns Q, the ecummulative production at time t

    """
    q = qi / ((1.0 + b*di*t)**(1.0/b))
    
    return ((qi**b)/(di*(1-b)))*(qi**(1-b)-q**(1-b))



def harmonic_equation(t, qi, di):
    """
    Parameters
    ----------
    t : Time since initial (can be numpy array)
    qi : Initial production rate. Float
    di : Nominal decline rate. Float

    Returns
    -------
    returns Q, the ecummulative production at time t

    """
    import numpy as np
    q = qi/(1.0 + di*t)
    
    return (qi/di)*np.log(qi/q)
    


def periodic_monthly_volume(cumulative_array):
    
    """
    Parameters
    ----------
    cumulative_array: an array of cumulative production for each month

    Returns
    -------
    returns an array containing the periodic monthly volume

    """
    import numpy as np
    
    periodic_monthly_volume_array = np.float32(range(len(cumulative_array)-1))
    
    # loop through cumulative array and calculate the monthly production as
    # the cumulative value at the end of the month minus the cumulative value 
    # at the beggining of the month
    for i in range(0, len(cumulative_array)-1):
        periodic_monthly_volume_array[i] = cumulative_array[i+1]-cumulative_array[i]
        
    
    return periodic_monthly_volume_array