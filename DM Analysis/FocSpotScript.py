# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 19:42:07 2015

@author: aline
"""

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import BiVarFit as bv

from numpy import unravel_index
from numpy import *
from scipy import optimize
from pylab import *

def analysis(fileName):
#    fileName = str(fileName)
    img=mpimg.imread(fileName)/16;


    binning = 4;
    mxFoc = 100;
    dimCam = img.shape;


#binning


    img_bin = img.reshape(dimCam[0]/binning, binning, dimCam[1]/binning, binning);
    img_bin = img_bin.mean(axis=3).mean(axis=1);
    img_bin = img_bin-img_bin.min();


#imgplot = plt.imshow(img_bin)
#imgplot.set_cmap('hot')
#imgplot.set_clim(0.0,img.max())

#Find ROI

    coordMax = unravel_index(img_bin.argmax(), img_bin.shape)
    ROI = img_bin[coordMax[0]-mxFoc:coordMax[0]+mxFoc,coordMax[1]-mxFoc:coordMax[1]+mxFoc]

#ROIplot = plt.imshow(ROI)



    data = ROI;

#    matshow(data, cmap=cm.gist_earth_r)

    params = bv.fitbivarGaussian(data)
    fit = bv.bivarGaussian(*params)

#    contour(fit(*indices(data.shape)), cmap=cm.copper)
#    ax = gca()
    (height, x, y, width_x, width_y, rho) = params

#    text(0.95, 0.05, """
#    x : %.1f
#    y : %.1f
#    width_x : %.1f
#    width_y : %.1f
#    rho : %.lf""" %(x, y, width_x, width_y, rho),
#        fontsize=16, horizontalalignment='right',
#        verticalalignment='bottom', transform=ax.transAxes)

 #   show()
    return x, y, width_x, width_y, rho
    
