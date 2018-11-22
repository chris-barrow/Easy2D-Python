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
    NARRAY = NINP/2
    XII = np.zeros(NINP,NARRAY) # integration points
    WT = np.zeros(NINP,NARRAY) # weights
    # loop over integration points
    for I in range(NINP):
        XII[I] = XI[I,NARRAY]
        WT[I] = W[I,NARRAY]
    
    return NINP, XII, WT