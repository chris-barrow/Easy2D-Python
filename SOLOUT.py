#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Print solution on boundary.

#### NOT YET DEBUGGED!!!

Created on Tue Nov 20 10:58:36 2018
@author: Simon Schmitt
"""
# Import necessary Python Packages
import numpy as np

def Solout(fid2,NNODE, NELEM, KIND, NODE, CP, TEMP, CA, CB, CC, XS,Exterior):
    #
    #   IDENTIFY THE SOLUTION VECTOR
    #
    BIG = 1.0e15
    DTDN = np.zeros(4,NELEM)
    for I in range(NNODE):
        if TEMP[I]==BIG:
            TEMP[I] = XS[I]
    
    for K in range(NELEM):
        NL = KIND[K]+1
        for J in range(NL):
            NOD = NODE[J,K]
            if CB[J,K]==0.0:
                DTDN[J,K] = XS[NOD]
            else:
                DTDN[J,K] = (CC[J,K]-CA[J,K]*TEMP[NOD]) / CB[J,K]
            
        
    ## From here on I dont know yet...
#    fprintf(fid2,'\n %s \n \n', 'CP ON THE NODES:');
#    for I=1:NNODE
#        fprintf(fid2,'%s  %i  %s   %15.3f \n', 'NODE #', I, 'CP=', CP(I));
#    end
#    if Exterior~=3
#        fprintf(fid2,'\n %s  \n \n', 'TEMPERATURE ON THE BOUNDARY:');
#        ss='TEMP=';
#    else
#        fprintf(fid2,'\n %s  \n \n', 'PHI ON THE BOUNDARY:');
#        ss='PHI=';
#    end
#    for I=1:NNODE
#        fprintf(fid2,'%s  %i  %s   %15.3f \n', 'NODE #', I, ss, TEMP(I));
#    end
#    if Exterior~=3
#    fprintf(fid2,'\n %s \n \n','DTDN ON THE BOUNDARY:');
#    hh='DTDN=';
#    else
#        fprintf(fid2,'\n %s \n \n','VELOCITY ON THE BOUNDARY:');
#        hh='V=';
#    end
#    for K=1:NELEM
#        if KIND(K)==1
#            fprintf(fid2,'%s %i  \t %s  %15.3f  %15.3f \n', 'ELEMENT # ',K ,hh,DTDN(1,K), DTDN(2,K));
#        end
#        if KIND(K)==2
#            fprintf(fid2,'%s %i  \t %s  %15.3f  %15.3f  %15.3f \n', 'ELEMENT # ',K ,hh,DTDN(1,K), DTDN(2,K), DTDN(3,K) );
#        end
#        if KIND(K)==3
#            fprintf(fid2,'%s %i  \t %s  %15.3f  %15.3f  %15.3f  %15.3f \n', 'ELEMENT # ',K ,hh,DTDN(1,K), DTDN(2,K),DTDN(3,K),DTDN(4,K) );
#        
    return DTDN,TEMP
