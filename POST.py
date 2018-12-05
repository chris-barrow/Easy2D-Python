#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
...

Created on Thu Nov 15 15:58:55 2018
@author: Simon Schmitt
"""
# Import necessary Python Packages
import numpy as np
import matplotlib.pyplot as plt
#import scipy.interpolate as interp

def post(X,Y,DTDN,TEMP,Px, Py,PhiP,dPhidPX,dPhidPY):
    X = X.reshape(len(X))
    Y = Y.reshape(len(X))
    TEMP = TEMP.reshape(len(X))
    Xdat = np.append(X,Px);
    Ydat = np.append(Y,Py)
    Zdat = np.append(TEMP,PhiP)
    X = np.append(X,X[0])
    Y = np.append(Y,Y[0])
    levels = np.arange(Zdat.min()-0.15,Zdat.max()+0.15,0.1)
    plt.figure()
    plt.plot(X,Y)
#    plt.tricontourf(Xdat,Ydat,Zdat,11,cmap='jet')
    plt.tricontourf(Xdat,Ydat,Zdat,levels,cmap='jet')
    plt.colorbar()
#    plt.quiver(Px,Py,dPhidPX,dPhidPY)
#    Xi, Yi, Zi1 = grid(Px, Py, dPhidPX)
#    Xi, Yi, Zi2 = grid(Px, Py, dPhidPY)
#    plt.streamplot(Xi,Yi,Zi1,Zi2)
    return 
#
    




#def post2(X,Y,DTDN,TEMP,Px, Py,PhiP,dPhidPX,dPhidPY):
#    X = X.reshape(len(X))
#    Y = Y.reshape(len(X))
#    X = np.append(X,X[0])
#    Y = np.append(Y,Y[0])
##    levels = [Zi.min()/2,Zi.mean(),Zi.max()*3/2]
#    plt.figure()
#    plt.plot(X,Y)
#    Xi, Yi, Zi0 = grid(Px, Py, PhiP)
#    Xi, Yi, Zi1 = grid(Px, Py, dPhidPX)
#    Xi, Yi, Zi2 = grid(Px, Py, dPhidPY)
#    plt.contourf(Xi,Yi,Zi0,20, cmap='jet')
#    plt.colorbar()
##    plt.quiver(Px,Py,dPhidPX,dPhidPY)
##    plt.streamplot(Xi,Yi,Zi1,Zi2)
#    return 
#
#
#def post1(X,Y,XS,Px, Py,PhiP,dPhidPX,dPhidPY):
#    
#    
#    X = X.reshape(len(X))
#    Y = Y.reshape(len(Y))
#    Xdat = np.append(Y,Px);
#    Ydat = np.append(Y,Py)
#    XSdat = np.append(XS,PhiP)
##    Xdat = Px
##    Ydat = Py
##    XSdat = PhiP
#    
#    Xi, Yi, Zi = grid(Xdat, Ydat, XSdat)
#    
#    X = np.append(X,X[0])
#    Y = np.append(Y,Y[0])
#    plt.figure()
#    plt.plot(X,Y)
#    plt.contourf(Xi,Yi,Zi, 20, cmap='jet')
#    plt.colorbar()
#    plt.quiver(Px,Py,dPhidPX,dPhidPY)
#    Xi, Yi, Zi1 = grid(Px, Py, dPhidPX)
#    Xi, Yi, Zi2 = grid(Px, Py, dPhidPY)
#    plt.streamplot(Xi,Yi,Zi1,Zi2)
#    return 


#
#def grid(x, y, z, resX=2, resY=2):
#    # Convert 3 column data to matplotlib grid
#    xi = np.linspace(min(x), max(x), resX)
#    yi = np.linspace(min(y), max(y), resY)
#    Zi = interp.griddata((x, y), z, (xi[None,:], yi[:,None]), method='nearest')
#    Xi, Yi = np.meshgrid(xi, yi)
#    return Xi, Yi, Zi










