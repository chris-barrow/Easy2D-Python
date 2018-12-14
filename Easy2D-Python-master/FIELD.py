#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
...

Created on Mon Nov 26 17:35:38 2018
@author: Simon Schmitt
"""
import numpy as np
from GETINT import getint
from SHAPE import shape

def field(fid2,Px,Py,FREC,NNODE,NELEM,KIND,NODE,X,Y,TEMP,DTDN,Exterior,VINF,PhiI):

    PhiP = np.zeros(FREC)
    dPhidPX = np.zeros(FREC)
    dPhidPY = np.zeros(FREC)
    PhiPI = np.zeros(FREC)
    DPhidPXI = np.zeros(FREC)
    DPhidPYI = np.zeros(FREC)
    
    for IP in range(FREC):
        XP = Px[IP]
        YP = Py[IP]
        CP = 0
        FPT = 0
        FPDX = 0
        FPDY = 0
        QN = np.zeros(2)
        if Exterior==3:
            CP = np.ones(NNODE)
        #
        #       ELEMENT LOOP
        #  
        for K in range(NELEM):
            KINDI = KIND[K]
            NL = KINDI+1
            XQ = np.zeros(NL)
            YQ = np.zeros(NL)
            TEMQ = np.zeros(NL)
            DTDQ = np.zeros(NL)
            for J in range(NL):
                IQ = NODE[J,K]
                XQ[J] = X[int(IQ)]
                YQ[J] = Y[int(IQ)]
                TEMQ[J] = TEMP[0,int(IQ)]
                DTDQ[J] = DTDN[J,K]  
            #
            #      INTERPOLATION
            #
            C1 = -1/(2*np.pi)
            [NINP, XII, WT] = getint(KINDI)
            for INP in range(NINP):
                [PSI,DPSI] = shape(XII[INP],KINDI)
                XX = 0
                YY = 0
                DXDS = 0
                DYDS = 0
                TEM = 0
                DTN = 0
                for I in range(NL):
                    XX += XQ[I]*PSI[I]
                    YY += YQ[I]*PSI[I]
                    DXDS += XQ[I]*DPSI[I]
                    DYDS += YQ[I]*DPSI[I]
                    TEM += TEMQ[I]*PSI[I]
                    DTN += DTDQ[I]*PSI[I]
                DETJ = np.sqrt(DXDS**2+DYDS**2)
                QN[0] = (-1)**(Exterior)*DYDS/DETJ
                QN[1] = -(-1)**(Exterior)*DXDS/DETJ
                RX = XX-XP
                RY = YY-YP
                R = np.sqrt(RX**2+RY**2)
                DRDN = (QN[0]*RX+QN[1]*RY)/R
                ALOGR = np.log(R)
                GREEN = C1*ALOGR*DETJ*WT[INP]
                DGDN = C1*DRDN/R*DETJ*WT[INP]
                DRDX = RX/R
                DRDY = RY/R
                DGDX = -C1*DRDX/R*DETJ*WT[INP]
                DGDY = -C1*DRDY/R*DETJ*WT[INP]
                DXDGDN = C1/(R**2)*(2*DRDX*DRDN-QN[0])*DETJ*WT[INP]
                DYDGDN = C1/(R**2)*(2*DRDY*DRDN-QN[1])*DETJ*WT[INP]
                FPT += GREEN*DTN-TEM*DGDN
                FPDX += DGDX*DTN-TEM*DXDGDN
                FPDY += DGDY*DTN-TEM*DYDGDN
                CP -= DGDN
            
        if Exterior!=3:
            PhiP[IP] = FPT
            dPhidPX[IP] = FPDX
            dPhidPY[IP] = FPDY
        else:
            PhiPI[IP] = VINF*XP
            DPhidPXI[IP] = VINF
            DPhidPYI[IP] = 0
            PhiP[IP] = FPT+PhiPI[IP]
            dPhidPX[IP] = FPDX+DPhidPXI[IP]
            dPhidPY[IP] = FPDY+DPhidPYI[IP]
       
    fid2.write('\n {} \n \n'.format('FIELD POINTS COORDINATES AND SOLUTION:'))
    for K in range(FREC):
        fid2.write('{} {:d} \t {} {:3.3f} \t {} {:3.3f} \t {} {:3.3f} \t {} {:3.3f} \t {} {:3.3f}\n'.format('FIELD POINT # ', K+1, 'X=', float(Px[K]) , 'Y=', float(Py[K]), 'PHI=', float(PhiP[K]), 'dPHIdX=', float(dPhidPX[K]), 'dPHIdY=', float(dPhidPY[K]) ))
    
    return PhiP,dPhidPX,dPhidPY,QN