#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This function integrates h and g on singular elements.

#### NOT YET DEBUGGED!!!

Created on Thu Nov 22 10:51:00 2018
@author: Simon Schmitt
"""
# Import necessary Python Packages
import numpy as np
# Import BEM functions
import GETINT.getint as getint
import SHAPE.shape as shape

def Sing(XP,YP,NL,KINDI,XQ,YQ,XI,W,ISING,XIPMAP,CP,Exterior):
    #
    #---- CALL SETMAP in the EASY2D to set up XIPMAP(4,3) first
    #
    C1 = -1/(2*np.pi)
    H = np.zeros(1,NL)
    G = np.zeros(1,NL)
    NINP, ETA, WT = getint(KINDI,XI,W)
    XIP = XIPMAP(ISING, KINDI)
    #
    #---- THIS LOOP IS FOR THE PURPOSE OF INTEGRATING TO THE RIGHT OF P
    #
    if XIP != 1:
        for INP in range(NINP):
            A = np.sqrt(1-XIP)/2
            Z = A+A*ETA[INP]
            XII = Z**2+XIP
            PSI,DPSI = shape(XII,KINDI)
            XX = 0
            YY = 0
            DXDS = 0
            DYDS = 0
            for I in range(NL):
                XX = XX+XQ[I]*PSI[I]
                YY = YY+YQ[I]*PSI[I]
                DXDS = DXDS+XQ[I]*DPSI[I]
                DYDS = DYDS+YQ[I]*DPSI[I]
            JAC = np.sqrt(DXDS**2+DYDS**2)
            RX = XX-XP
            RY = YY-YP
            R = np.sqrt(RX**2+RY**2)
            QN[0] = (-1)**(Exterior)*DYDS/JAC
            QN[1] = -(-1)**(Exterior)*DXDS/JAC
            DRDN = (QN[0]*RX+QN[1]*RY)/R
            DZDE = (np.sqrt(1-XIP))/2
            GREEN = C1*np.log(R)*JAC*2*Z*DZDE*WT[INP]
            DGDN = C1*DRDN/R*JAC*2*Z*DZDE*WT[INP]
            for I in range(NL):
                G[I] = G[I]+PSI[I]*GREEN
                H[I] = H[I]+PSI[I]*DGDN
            CP = CP-DGDN
    #
    #*** THIS LOOP IS FOR THE PURPOSE OF INTEGRATING TO THE LEFT OF P
    #
    if XIP != -1:
        for INP in range(NINP):
            A = np.sqrt(1+XIP)/2
            Z = A+A*ETA[INP]
            XII = XIP-Z**2
            PSI,DPSI = shape(XII,KINDI)
            XX = 0
            YY = 0
            DXDS = 0
            DYDS = 0
            for I in range(NL):
                XX = XX+XQ[I]*PSI[I]
                YY = YY+YQ[I]*PSI[I]
                DXDS = DXDS+XQ[I]*DPSI[I]
                DYDS = DYDS+YQ[I]*DPSI[I]
            JAC = np.sqrt(DXDS**2+DYDS**2)
            RX = XX-XP
            RY = YY-YP
            R = np.sqrt(RX**2+RY**2)
            QN[0] = (-1)**(Exterior)*DYDS/JAC
            QN[1] = -(-1)**(Exterior)*DXDS/JAC
            DRDN = (QN[0]*RX+QN[1]*RY)/R
            DZDE = (np.sqrt(1+XIP))/2
            GREEN = C1*np.log(R)*JAC*2*Z*DZDE*WT[INP]
            DGDN = C1*DRDN/R*JAC*2*Z*DZDE*WT[INP]
            for I in range(NL):
                G[I] = G[I]+PSI[I]*GREEN
                H[I] = H[I]+PSI[I]*DGDN
            CP = CP-DGDN
    return CP,G,H,QN