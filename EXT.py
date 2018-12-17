#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Do not know yet what this does.

#### NOT YET DEBUGGED!!!

Created on Mon Nov 26 17:35:38 2018
@author: Simon Schmitt
"""
import numpy as np


def ext(fid2, NNODE, X, VINF):
    PhiI = np.zeros(NNODE)
    for I in range(NNODE):
        PhiI[I] = VINF*X[I]

    fid2.write('\n {}  \n \n'.format('==============EXTERIOR PROBLEM:'
                                     '====================='))
    fid2.write('{} \n'.format('V infinity = '+str(VINF)))

    return PhiI
