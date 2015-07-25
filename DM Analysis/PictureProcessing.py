# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 11:58:08 2015

@author: aline
"""

import numpy as np
from numpy import *
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import math as math



pxSize = 4.65; #in um
mxFoc = 100;

gaussLim = 40.; #gaussian beam limit size in um
pxLim = math.ceil(gaussLim/pxSize);
 

spotPicture = np.array(mpimg.imread("/home/aline/programming/Python/DM Analysis/20/tachefoc_moins10_3.tiff")).astype(float)/16;
background = np.array(mpimg.imread("/home/aline/programming/Python/DM Analysis/20/fond_3.tiff")).astype(float)/16;
exposure = 50; #millisec



img = (spotPicture - background)/exposure;

dimCam = img.shape; #Camera dimensions




coordMax = unravel_index(img.argmax(), img.shape)
ROI = img[coordMax[0]-mxFoc:coordMax[0]+mxFoc,coordMax[1]-mxFoc:coordMax[1]+mxFoc]

#ROIplot = plt.imshow(ROI)

data = ROI;

#Calculate mask 
a, b = mxFoc, mxFoc;
n = mxFoc*2;
r = pxLim+1;

x,y = np.ogrid[-a:n-a, -b:n-b]
mask = x*x + y*y <= r*r

diffSpot = np.zeros((n,n))
diffSpot[mask]=1

maskedData = np.multiply(diffSpot, data);

#plt.imshow(maskedData)

limSum = sum(maskedData.flatten());
fullSum = sum(data.flatten());

print("Energy ratio = " + str(limSum/fullSum))

"""
To calculate Strehl Ratio : 
Integrate full energy in ROI
Generate ideal gaussian beam whose inegrated energy is that of the ROI
Calculate ratio of focal area energy by binning by 4 and comparing max
"""
binning = 2;
    
gaussianData = np.ones((n, n)).astype(float)
for i in range(0, n):
    for j in range(0, n):
        gaussianData[i,j] = np.exp(-((i-mxFoc)**2+(j-mxFoc)**2)/pxLim**2);

gaussianData = gaussianData/sum(gaussianData.flatten())*fullSum

gaussianData_bin = gaussianData.reshape(mxFoc*2/binning, binning, mxFoc*2/binning, binning);
gaussianData_bin = gaussianData_bin.mean(axis=3).mean(axis=1);
gaussianData_bin_max = max(gaussianData_bin.flatten());

data_bin = data.reshape(mxFoc*2/binning, binning, mxFoc*2/binning, binning);
data_bin = data_bin.mean(axis=3).mean(axis=1);
data_bin_max = max(data_bin.flatten());

print("Strehl ratio = " + str(data_bin_max/gaussianData_bin_max))

plt.figure(1)
plt.subplot(211)
plt.imshow(data)
plt.subplot(212)
plt.imshow(gaussianData) 
plt.show()
