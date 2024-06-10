# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 14:39:57 2024

@author: BontL
"""

import numpy as np
t = np.arange(0,365,1/24)

T = -10*np.cos(2*np.pi/365 * t) - 8*np.cos(2*np.pi* t) + 5

P = 8e-3

x = np.arange(0,5000,500)

z = x/5  + 1400

lapse_rate = -0.6/100
melt_factor = 0.005
T_threshold = 4


from melt import synthetic_T, synthetic_P
import matplotlib.pyplot as plt

Ts = synthetic_T(t)
plt.plot(t,Ts)
plt.show()








