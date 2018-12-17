#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Print solution on the boundary.

Created on Tue Nov 20 10:58:36 2018
@author: Simon Schmitt
"""
# Import necessary Python Packages
import numpy as np


def solout(fid2, NNODE, NELEM, KIND, NODE, CP, TEMP, CA, CB, CC, XS, Exterior):

    #   IDENTIFY THE SOLUTION VECTOR
    BIG = 1.0e15
    DTDN = np.zeros((4, NELEM))
    for I in range(NNODE):
        if TEMP[0, I] == BIG:
            TEMP[0, I] = XS[I]

    for K in range(NELEM):
        NL = KIND[K]+1
        for J in range(NL):
            NOD = NODE[J, K]
            if CB[J, K] == 0.0:
                DTDN[J, K] = XS[int(NOD)]
            else:
                DTDN[J, K] = (CC[J, K]-CA[J, K]*TEMP[0, int(NOD)]) / CB[J, K]

    fid2.write('\n {} \n \n'.format('CP ON THE NODES:'))
    for I in range(0, NNODE):
        fid2.write('{} {:d} \t {} {:3.3f} \n'.format('NODE # ', I+1, 'CP =',
                                                     float(CP[I])))

    fid2.write('\n {} \n \n'.format('PHI ON THE BOUNDARY:'))
    for I in range(0, NNODE):
        fid2.write('{} {:d} \t {} {:3.3f} \n'.format('NODE # ', I+1, 'PHI =',
                                                     float(TEMP[0, I])))

    fid2.write('\n {} \n \n'.format('dPHId. ON THE BOUNDARY:'))
    for K in range(0, NELEM):
        fid2.write('{} {:d} \t {} {:3.3f}'
                   ' \t {} {:3.3f} \n'.format('ELEMENT # ', K+1, 'dPHIdX =',
                                              float(DTDN[0, K]), 'dPHIdY =',
                                              float(DTDN[1, K])))

    return DTDN, TEMP
