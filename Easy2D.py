"""
EASY2D-python

A Boundary Element Method (BEM) solver using python.

Author(s):
    Christopher Barrow
    Simeon Schmitt
"""

import os
import numpy as np
import PREP


def easy2D(inputFileName=None):
    if inputFileName == None:
        inputFileName = input('Specify input file name: ')

    # This should just be getting the Gaussian Quadrature
    [XI, W] = np.polynomial.legendre.leggauss(5)
    XIPMAP = SETMAP()
    [fid2, NNODE, NELEM, X, Y, NODE, KIND, TEMP, CA, CB, CC, FREC, Field,
     Exterior, Px, Py, VINF] = PREP.PREP(inputFileName)
    # [CP,DTDN,TEMP,XS,A,B,PhiP,dPhidPX,dPhidPY,QN]=PROC(fid2,XI, W, NNODE, NELEM, X, Y, NODE, KIND, TEMP, XIPMAP, CA,CB, CC, FREC,Field, Exterior,Px,Py,VINF)
    # fclose(fid2)


def SETMAP():
    XIPMAP = np.zeros((4,3))

    # Linear Elements
    XIPMAP[0, 0] = -1
    XIPMAP[1, 0] = 1

    # Quadratic Elements
    XIPMAP[0, 1] = -1
    XIPMAP[1, 1] = 0
    XIPMAP[2, 1] = 1

    # Cubic Elements
    XIPMAP[0, 2] = -1
    XIPMAP[1, 2] = -1/3
    XIPMAP[2, 2] = 1/3
    XIPMAP[3, 2] = 1

    return XIPMAP

if __name__ == "__main__":
    easy2D("Easy2D_MATLAB\TestCase1.dat")
