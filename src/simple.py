# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 14:39:57 2024

@author: BontL

Generate synthetic temperature data.

Parameters:
t (numpy.ndarray): Array of time values.

Returns:
numpy.ndarray: Array of temperature values.
"""

## returns a file name with git commit hash
from utils import make_sha_filename

basename = "file"
ext = ".txt"
filename = make_sha_filename(basename, ext)
print(filename)


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


# Plot the synthetic temperature data
plt.plot(t, T)
plt.xlabel('Time (days)')
plt.ylabel('Temperature (°C)')
plt.title('Synthetic Temperature Data')
plt.grid(True)
plt.show()






