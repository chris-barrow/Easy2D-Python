#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This function is used to get the integration points.

### NOT YET DEBUGGED!!!

Created on Thu Nov 22 10:50:28 2018
@author: Simon Schmitt
"""
# Import necessary Python Packages
import numpy as np

def getint(KINDI,XI,W):
    if KINDI == 1:
        NINP = 4
    elif KINDI == 2:
        NINP = 6
    else:
        NINP = 8
#    NARRAY = NINP/2
#    XII = np.zeros([NINP,int(NARRAY)]) # integration points
#    WT = np.zeros([NINP,int(NARRAY)]) # weights
#    # loop over integration points
#    for I in range(NINP):
#        XII[I,:] = XI[I]
#        WT[I,:] = W[I]
        
    XII, WT = np.polynomial.legendre.leggauss(NINP)
    
    return NINP, XII, WT