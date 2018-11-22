#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This function sets up the system matrix A and the right-hand-side forcing 
vector B.

#### NOT YET DEBUGGED!!!

Created on Tue Nov 20 10:56:09 2018
@author: Simon Schmitt
"""
# Import necessary Python Packages
import numpy as np
# Import BEM functions
import ELEMT.elemt as elemt
import SING.sing as sing
import ASSMB.assmb as assmb

def form(NNODE,NELEM,NODE,KIND,X,Y,TEMP,XI,W,XIPMAP,CA,CB,CC,Exterior,PhiI):
    # Initialize variables
    BIG = 1.0e15
    B = np.zeros(1,NNODE)
    A = np.zeros(NNODE)
    CP = np.zeros(1,NNODE)
    if Exterior==3:
        CP = np.ones(1,NNODE)
    
    # Loop over collocation points
    for IP in range(NNODE): 
        XP = X[IP]
        YP = Y[IP]
        # Loop over Elements
        for K in range(NELEM): 
            KINDI = KIND[K]
            NL = KINDI+1
            ISING = 0
            for J in range(NL): 
                IQ = NODE[J,K]
                if IQ==IP:
                    ISING = J
                XQ[J] = X[IQ]
                YQ[J] = Y[IQ]
                
            if ISING==0:
                CP[IP],G,H,QN = elemt(XP,YP,NL,KINDI,XQ,YQ,XI,W,CP[IP],Exterior)
            else:
                CP[IP],G,H,QN = sing(XP,YP,NL,KINDI,XQ,YQ,XI,W,ISING,XIPMAP,CP[IP],Exterior)
            A,B = assmb(K,NL,H,G,IP,NODE,TEMP,CA,CB,CC,A,B)
        
        #
        #   Contribution from C(P)
        #
        if TEMP[IP]==BIG:
            A[IP,IP] = A[IP,IP] + CP[IP]
        else:
            B[IP] = B[IP] - CP[IP]*TEMP[IP]
        B[IP] = B[IP] + PhiI[IP]
    
    return CP,A,B,QN