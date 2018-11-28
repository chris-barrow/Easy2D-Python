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

def solout(fid2,NNODE, NELEM, KIND, NODE, CP, TEMP, CA, CB, CC, XS,Exterior):
    #
    #   IDENTIFY THE SOLUTION VECTOR
    #
    BIG = 1.0e15
    DTDN = np.zeros((4,NELEM))
    for I in range(NNODE):
        if TEMP[0,I]==BIG:
            TEMP[0,I] = XS[I]
    
    for K in range(NELEM):
        NL = KIND[K]+1
        for J in range(NL):
            NOD = NODE[J,K]
            if CB[J,K]==0.0:
                DTDN[J,K] = XS[NOD]
            else:
                DTDN[J,K] = (CC[J,K]-CA[J,K]*TEMP[0,int(NOD)]) / CB[J,K]
            
        
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
    fid2.write('\n {} \n \n'.format('CP ON THE NODES:'))
    for I in range(0, NNODE):
        fid2.write('{} {:d} \t {} {:3.3f} \n'.format('NODE # ', I+1, 'CP =', float(CP[I])))
                   
    fid2.write('\n {} \n \n'.format('PHI ON THE BOUNDARY:'))
    for I in range(0, NNODE):
        fid2.write('{} {:d} \t {} {:3.3f} \n'.format('NODE # ', I+1, 'PHI =', float(TEMP[0,I])))
                   
    fid2.write('\n {} \n \n'.format('VELOCITY ON THE BOUNDARY:'))
    for K in range(0, NELEM):
        fid2.write('{} {:d} \t {} {:3.3f} \t {} {:3.3f} \n'.format('ELEMENT # ', K+1, 'V1 =', float(DTDN[0,K]) , 'V2 =', float(DTDN[1,K]) ))
    
    return DTDN,TEMP
