#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This function is the BEM Processor, taking its input from the preprocessor 
PREP, and writing the solution out in outputfiles.

Created on Thu Nov 15 15:58:55 2018
@author: Simon Schmitt
"""
# Import necessary Python Packages
import numpy as np
# Import BEM functions
from FORM import form
from SOLVE import solve
from SOLOUT import solout
from EXT import ext

def proc(fid2,XI,W,NNODE,NELEM,X,Y,NODE,KIND,TEMP,XIPMAP,CA,CB,CC,FREC,Field,Exterior,Px,Py,VINF):
#    # ????????
    if Exterior==3:
        PhiI = ext(fid2,NNODE,X,VINF)
    else:
        PhiI = np.zeros(NNODE)

    # form system of eqs
    CP,A,B,QN = form(NNODE, NELEM, NODE, KIND, X, Y, TEMP,XI,W, XIPMAP, CA, CB, CC,Exterior,PhiI)
    # solve
    XS,A,B = solve(A,B)
    # save solution
    DTDN,TEMP = solout(fid2,NNODE, NELEM, KIND, NODE,CP, TEMP, CA, CB, CC, XS,Exterior)
    
#    # ???????
#    if Field==2:
#        PhiP,dPhidPX,dPhidPY,QN = FIELD(fid2,Px,Py,FREC,NNODE,NELEM,KIND,NODE,X,Y,TEMP,DTDN,XI,W,Exterior,VINF,PhiI)
#    else:
#        PhiP,dPhidPX,dPhidPY = np.zeros(1,3)
     
#    return CP,DTDN,TEMP,XS,A,B,PhiP,dPhidPX,dPhidPY,QN
    return CP,DTDN,TEMP,XS,A,B


















