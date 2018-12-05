#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This is the gaussian elimination solver.

Created on Thu Nov 22 10:51:00 2018
@author: Simon Schmitt
"""
# Import necessary Python Packages
import numpy as np

def solve(A,B):
    XS = np.linalg.solve(A,B)
    return XS