#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This function is used to get the shape functions.

Created on Thu Nov 22 10:50:09 2018
@author: Simon Schmitt
"""

# Import necessary Python Packages
import numpy as np


def shape(XI, KINDI):
    PSI = np.zeros(KINDI+1)
    DPSI = np.zeros(KINDI+1)
    # Linear Elements
    if KINDI == 1:
        PSI[0] = 0.5*(1.0-XI)
        PSI[1] = 0.5*(1.0+XI)
        DPSI[0] = -0.5
        DPSI[1] = 0.5
    # Quadratic Elements
    elif KINDI == 2:
        PSI[0] = 0.5*XI*(XI-1.0)
        PSI[1] = 1.0-XI**2
        PSI[2] = 0.5*XI*(XI+1.0)
        DPSI[0] = XI-0.5
        DPSI[1] = -2.0*XI
        DPSI[2] = XI+0.5
    # Cubic Elements
    elif KINDI == 3:
        PSI[0] = 9./16.*(1./9.-XI**2)*(XI-1.0)
        PSI[1] = 27./16.*(1.0-XI**2)*(1./3.-XI)
        PSI[2] = 27./16.*(1.0-XI**2)*(1./3.+XI)
        PSI[3] = -9./16.*(1./9.-XI**2)*(XI+1.0)
        DPSI[0] = -9./16.*(3.*XI**2-2.*XI-1./9.)
        DPSI[1] = 27./16.*(3.*XI**2-2./3.*XI-1.)
        DPSI[2] = 27./16.*(-3.*XI**2-2./3.*XI+1.)
        DPSI[3] = -9./16.*(-3.*XI**2-2.*XI+1./9.)
    return PSI, DPSI
