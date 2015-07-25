# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 15:42:33 2015
l = lambda
w0 = waist
z = distance
R = Radius of curvature
@author: aline
"""
import numpy as np
from numpy import *

def RCurv(z, w0, l):
    if z == 0:
        R = np.inf;
    else:    
        R = z*(1+(np.pi*w0**2/(l*z))**2);
    return R
    
def Wz(z, w0, l):
    w = np.sqrt(w0**2*(1+(l*z/(np.pi*w0**2))**2))
    return w
    
    
def invQ(R, w, l):
    if np.isinf(R):
        mq = complex(0, -l/(np.pi*w**2));
    else:
        mq =  complex(1/R, - l/(np.pi*w**2));  
    return mq 
    
def lens(f):
    return np.matrix([[1., 0], [-1./f, 1.]])

    
def freespace(D):
    return np.matrix([[1., D],[0, 1.]])


    
def propagInvQ(invq1, mat):
    invq2 = (mat[1,0]+mat[1,1]*invq1)/(mat[0,0]+mat[0,1]*invq1)
    return invq2

def waistFromInvQ(invQ, l):
    return np.sqrt(l/(np.pi*np.imag(-invQ)));
    

    