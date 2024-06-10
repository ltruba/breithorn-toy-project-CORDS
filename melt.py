# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 09:32:11 2024

@author: BontL
"""

# Melt at a point M


 

def melt_at_point_M(T, melt_factor):
    if T > 0:
        return  melt_factor*T
    else:
        return 0
        


def Accumulation_at_a_point_C(T,P,Tth):
    if T < Tth:
        return P
    else:
        return 0
    
    

melt_factor  = 1    
T = 3   
out = melt_at_point_M(T, melt_factor)