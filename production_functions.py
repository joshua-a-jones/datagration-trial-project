#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 30 2021

@author: joshuajones
"""
import numpy as np

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

    Q = np.full(len(t),0.0)
    
    for i in range(0, len(Q)):
        q = qi*np.exp(-di*t[i])
        Q[i] = (qi - q)/di
    
    return Q


def hyperbolic_equation(t, qi, b, di, dmin):
    """
    Parameters
    ----------
    t : time since initial. numpy array
    qi : Initial production rate. Float
    b : hyperbolic decline constant. Float
    di : Nominal decline rate at t = 0.

    Returns
    -------
    returns Q, the cummulative production at time t

    """
    Q = np.full(len(t), 0.0)
    
    # these variables track and what time the decline switches to
    # exponential. This is needed so that the hyperbolic curve and the
    # exponential curve match up
    hyperbolic_q_min = qi
    hyperbolic_stop_time = 0.0
    hyperbolic_stop_Q = 0.0
    
    for i in range(0, len(Q)):
        
        d = decline_rate(t[i], di, b)

        # if d > dmin, use hyperbolic function
        if d > dmin:
            q = qi/((1.0 + b*di*t[i])**(1.0/b))
            hyperbolic_q_min = q
            hyperbolic_stop_time = t[i]
            Q[i] = ((qi**b)/(di*(1.0-b)))*(qi**(1.0-b)-q**(1.0-b))
            hyperbolic_stop_Q = Q[i]

        # when d < dmin, switch to exponential 
        else:
            q = hyperbolic_q_min*np.exp(-dmin*(t[i]-hyperbolic_stop_time))
            Q[i] = hyperbolic_stop_Q + (hyperbolic_q_min - q)/dmin
                     
    return Q



def harmonic_equation(t, qi, di, dmin):
    """
    Parameters
    ----------
    t : Time since initial. numpy array
    qi : Initial production rate. Float
    di : Nominal decline rate. Float

    Returns
    -------
    returns Q, the ecummulative production at time t

    """
    b = 1.0
    Q = np.full(len(t), 0.0)
    
    # these variables track and what time the decline switches to
    # exponential. This is needed so that the hyperbolic curve and the
    # exponential curve match up
    harmonic_q_min = qi
    harmonic_stop_time = 0.0
    harmonic_stop_Q = 0.0
    
    for i in range(0, len(t)):
        
        d = decline_rate(t[i], di, b)
        
        #if d > dmin, use harmonic function
        if d > dmin:
            q = qi/(1.0 + di*t[i])
            harmonic_q_min = q
            harmonic_stop_time = t[i]
            Q[i] = (qi/di)*(np.log(qi/q))
            harmonic_stop_Q = Q[i]
        # when d < dmin, switch to exponential function
        else:
            q = harmonic_q_min*np.exp(-dmin*(t[i]-harmonic_stop_time))
            Q[i] = harmonic_stop_Q + (harmonic_q_min - q)/dmin
    return Q
    


def decline_rate(t, di, b):
    
    return di/(1+(b*di*t))



def periodic_monthly_volume(cumulative_array):
    
    """
    Parameters
    ----------
    cumulative_array: an array of cumulative production for each month

    Returns
    -------
    returns an array containing the periodic monthly volume

    """
    
    periodic_monthly_volume_array = np.float64(range(len(cumulative_array)-1))
    
    # loop through cumulative array and calculate the monthly production as
    # the cumulative value at the end of the month minus the cumulative value 
    # at the beggining of the month
    for i in range(0, len(cumulative_array)-1):
        periodic_monthly_volume_array[i] = cumulative_array[i+1]-cumulative_array[i]
        
    
    return periodic_monthly_volume_array
