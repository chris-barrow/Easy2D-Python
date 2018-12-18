#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Do not know yet what this does.

#### NOT YET DEBUGGED!!!

Created on Mon Nov 26 17:35:38 2018
@author: Simon Schmitt
"""
import numpy as np


def ext(fid2, NNODE, X, Y, VINF, ALPHA):
    PhiI = np.zeros(NNODE)
    if VINF != 0:
        for I in range(NNODE):
            PhiI[I] = VINF*X[I]
    elif ALPHA != 0:
        for I in range(NNODE):
            PhiI[I] = -ALPHA/(2*np.pi)*np.log(np.sqrt(X[I]**2 + Y[I]**2))

    fid2.write('\n {}  \n \n'.format('==============EXTERIOR PROBLEM:'
                                     '====================='))
    if VINF != 0:
        fid2.write('{} \n'.format('V infinity = '+str(VINF)))
    elif ALPHA != 0:
        fid2.write('{} \n'.format('ALPHA = '+str(ALPHA)))

    return PhiI
