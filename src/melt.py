# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 09:32:11 2024

@author: BontL
"""
import numpy as np
# Melt at a point M


 

def melt(T, melt_factor):
    if T > 0:
        return  melt_factor*T
    else:
        return 0
        
def accumulate(T,P,Tth):
    if T < Tth:
        return P
    else:
        return 0
    
    

melt_factor  = 1    
T = 3   
out = melt(T, melt_factor)


# Precipitation function
def synthetic_P(t):
    return 8e-3


# Synthetic temperature
def synthetic_T(t):    
    return -10.0*np.cos(2*np.pi/364 * t) - 8.0*np.cos(2*np.pi* t) + 5.0


# Lapsed temperature 
def lapse(T, dz, lapse_rate):
    return lapse_rate * dz + T


def net_balance_fn(dt, Ts, Ps, melt_factor, T_threshold):
    """
    Integrate the balance rate (this is at a point) over time for given temperature and precipitation arrays to get the "net balance".

    Args:
        dt: The time step.
        Ts: Array of temperatures.
        Ps: Array of precipitations.
        melt_factor: The factor to compute melt amount.
        T_threshold: The temperature threshold for accumulation.

    Returns:
        net balance (this is at a point)
    """
    assert len(Ts) == len(Ps)
    total = 0.0
    for T, P in zip(Ts, Ps):
        balance_rate = -melt(T, melt_factor) + accumulate(T, P, T_threshold)
        total += balance_rate * dt
    return total


def glacier_net_balance_fn(zs, dt, Ts, Ps, melt_factor, T_threshold, lapse_rate):
    """
    Calculate:
    - the glacier net balance (integration of balance rate over time and space)
    - the net balance at each point (integration of balance rate over time)

    Args:
        zs: Array of elevations (with the weather station as datum)
        dt: The time step.
        Ts: Array of temperatures.
        Ps: Array of precipitations.
        melt_factor: The factor to compute melt amount.
        T_threshold: The temperature threshold for accumulation.
        lapse_rate: The lapse rate (temperature change per unit elevation change).

    Returns:
        the glacier net balance [m]
        net balance at all points [m]
    """
    glacier_net_balance = 0.0
    net_balance = np.zeros(len(zs))
    for i, z in enumerate(zs):
        TT = [lapse(T, z, lapse_rate) for T in Ts]
        net_balance[i] = net_balance_fn(dt, TT, Ps, melt_factor, T_threshold)
        glacier_net_balance += net_balance[i]
    return glacier_net_balance / len(zs), net_balance
