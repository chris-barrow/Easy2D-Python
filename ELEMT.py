#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This function integrates h and g on each element.

Created on Thu Nov 22 10:37:23 2018
@author: Simon Schmitt
"""

# Import necessary Python Packages
import numpy as np

# Import BEM functions
from GETINT import getint
from SHAPE import shape


def elemt(XP, YP, NL, KINDI, XQ, YQ, CP, Exterior):

    # Formulate element coefficient matrices
    C1 = -1/(2*np.pi)
    H = np.zeros(NL)
    G = np.zeros(NL)
    NINP, XII, WT = getint(KINDI)

    #  Integration loop
    QN = np.zeros(2)
    for INP in range(NINP):
        PSI, DPSI = shape(XII[INP], KINDI)
        XX = 0.0
        YY = 0.0
        DXDS = 0.0
        DYDS = 0.0
        for I in range(NL):
            XX = XX+XQ[I]*PSI[I]
            YY = YY+YQ[I]*PSI[I]
            DXDS = DXDS+XQ[I]*DPSI[I]
            DYDS = DYDS+YQ[I]*DPSI[I]

        DETJ = np.sqrt(DXDS**2+DYDS**2)
        QN[0] = (-1)**(Exterior)*DYDS/DETJ
        QN[1] = -(-1)**(Exterior)*DXDS/DETJ
        RX = XX-XP
        RY = YY-YP
        R = np.sqrt(RX**2+RY**2)
        DRDN = (QN[0]*RX+QN[1]*RY)/R
        ALOGR = np.log(R)
        GREEN = C1*ALOGR*DETJ*WT[INP]
        DGDN = C1*DRDN/R*DETJ*WT[INP]
        for I in range(NL):
            H[I] = H[I]+PSI[I]*DGDN
            G[I] = G[I]+PSI[I]*GREEN
        CP = CP-DGDN
    return CP, G, H, QN
