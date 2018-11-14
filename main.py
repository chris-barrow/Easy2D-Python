"""
EASY2D-python

A Boundary Element Method (BEM) solver using python.

Author(s):
    Christopher Barrow
    Simeon Schmitt
"""

import os
import numpy.polynomial.legendre.leggauss as SETINT


def easy2D():
    inputfilename = input('Specify input file name. ', 's')
    [XI, W] = SETINT() # This should just be getting the Gaussian Quadrature
    XIPMAP = SETMAP()
    [fid2,NNODE, NELEM, X, Y, NODE, KIND, TEMP, CA, CB, CC, FREC,Field, Exterior,Px,Py,VINF]=PREP(inputfilename)
    [CP,DTDN,TEMP,XS,A,B,PhiP,dPhidPX,dPhidPY,QN]=PROC(fid2,XI, W, NNODE, NELEM, X, Y, NODE, KIND, TEMP, XIPMAP, CA,CB, CC, FREC,Field, Exterior,Px,Py,VINF)
    fclose(fid2)


def SETMAP():
    XIPMAP = [[], []]

    # Linear Elements
    XIPMAP[1, 1] = -1
    XIPMAP[2, 1] = 1

    # Quadratic Elements
    XIPMAP[1, 2] = -1
    XIPMAP[2, 2] = 0
    XIPMAP[3, 2] = 1

    # Cubic Elements
    XIPMAP[1, 3] = -1
    XIPMAP[2, 3] = -1/3
    XIPMAP[3, 3] = 1/3
    XIPMAP[4, 3] = 1

    return XIPMAP
