#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This function adds contributions of h and g to A and B.

Created on Thu Nov 22 10:50:48 2018
@author: Simon Schmitt
"""


def assmb(K, NL, H, G, IP, NODE, TEMP, CA, CB, CC, A, B):
    BIG = 1.0e15
    for J in range(NL):
        IQ = NODE[J, K]
        if TEMP[0, int(IQ)] != BIG:
            B[IP] -= H[J]*TEMP[0, int(IQ)]
            if CB[J, K] != 0:
                B[IP] += G[J] * (CC[J, K] - CA[J, K]*TEMP[0, int(IQ)])/CB[J, K]
            else:
                A[IP, int(IQ)] -= G[J]
        else:
            A[IP, int(IQ)] += H[J] + G[J]*CA[J, K]/CB[J, K]
            B[IP] += G[J]*CC[J, K]/CB[J, K]
    return A, B
