# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 16:08:11 2015
All lengths in meters
p = q^(-1)
@author: aline
"""
import numpy as np
import LensTransformation as lt
from LensTransformation import *
import matplotlib.pyplot as plt


l = 0.8*10**(-6);

invQ0 = invQ(np.inf, 0.022, l);
invQ1 = propagInvQ(invQ0, lens(1.25));
invQ2 = propagInvQ(invQ1, freespace(0.63));
invQ3 = propagInvQ(invQ2, lens(-1.));


zmin = 1.62;
zmax = 1.64;
numPoints = 1000;
dz = (zmax - zmin)/numPoints;

waistArr = [];
z = [];
for i in range(0, numPoints):
    invQ4 = propagInvQ(invQ3, freespace(zmin + i*dz));
    waist =  waistFromInvQ(invQ4, l);
    waistArr.append(waist);
    z.append(zmin+i*dz);
    
plt.plot(z,waistArr)

print("w0 = "+ str(min(waistArr)*10**6)+" um")
