# -*- coding: utf-8 -*-
"""
Created on Fri Oct 24 10:43:34 2014

@author: Rudy
"""

import numpy as np
from math import *

dBZ = 40
R = 20

def radarequation(dBZ,R):
    
    K = 0.93 #for rain/liquid
    La = 1
    R1 = 2.17 * 10**-10    
    Z1 = 1
    Z = 10 ** (dBZ / 10) * Z1
    Pt = 750000
    
    
    b = 14255
    
    atmos_effect = K / La
    
    range_inverse = R1 / R
    
    target_ref = Z / Z1
    
    Pr = b * atmos_effect**2 * range_inverse**2 * target_ref * Pt    
    
    return Pr
    
print radarequation(dBZ,R)