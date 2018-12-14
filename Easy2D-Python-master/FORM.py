#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This function sets up the system matrix A and the right-hand-side forcing 
vector B.

Created on Tue Nov 20 10:56:09 2018
@author: Simon Schmitt
"""
# Import necessary Python Packages
import numpy as np
# Import BEM functions
from ELEMT import elemt
from SING import sing
from ASSMB import assmb

def form(NNODE,NELEM,NODE,KIND,X,Y,TEMP,XIPMAP,CA,CB,CC,Exterior,PhiI):
    # Initialize variables
    BIG = 1.0e15
    B = np.zeros(NNODE)
    A = np.zeros((NNODE,NNODE))
    CP = np.zeros(NNODE)
    if Exterior==3:
        CP = np.ones(NNODE)
    
    # Loop over collocation points
    for IP in range(NNODE): 
        XP = X[IP]
        YP = Y[IP]
        # Loop over Elements
        for K in range(NELEM): 
            KINDI = KIND[K]
            NL = KINDI+1
            ISING = 0
            XQ = np.zeros(NL)
            YQ = np.zeros(NL)
            for J in range(NL): 
                IQ = NODE[J,K]
                if IQ==IP:
                    ISING = J+1
                XQ[J] = X[int(IQ)]
                YQ[J] = Y[int(IQ)]        
            if ISING==0:
                CP[IP],G,H,QN = elemt(XP,YP,NL,KINDI,XQ,YQ,CP[IP],Exterior)
            else:
                CP[IP],G,H,QN = sing(XP,YP,NL,KINDI,XQ,YQ,ISING,XIPMAP,CP[IP],Exterior)
            A,B = assmb(K,NL,H,G,IP,NODE,TEMP,CA,CB,CC,A,B)
        #
        #   Contribution from C(P)
        #
        if TEMP[0,IP]==BIG:
            A[IP,IP] += CP[IP]
        else:
            B[IP] -= CP[IP]*TEMP[0,IP]
        B[IP] += PhiI[IP]
    
    return CP,A,B,QN