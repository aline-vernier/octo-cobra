# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 19:39:42 2015

@author: aline
"""

import numpy as np
from numpy import *
from scipy import optimize
from pylab import *



#Fitting

                
def bivarGaussian(height, center_x, center_y, width_x, width_y, rho):
    """Returns a bivariate gaussian function with the given parameters"""
#    width_x = float(width_x)
#    width_y = float(width_y)
#    rho = float(rho)
    return lambda x,y: height*(
                1/(2*3.14*width_x*width_y*sqrt(1-rho**2)))*exp(
                -(((center_x-x)/width_x)**2+((center_y-y)/width_y)**2-(
                2*rho*(center_x-x)*(center_y-y))/(width_x*width_y))/(
                2*(1-rho**2)))


def bivarParams(data):
    """Returns (height, x, y, width_x, width_y, rho)
    the gaussian parameters of a 2D distribution by calculating its
    moments """
    total = data.sum()
    X, Y = indices(data.shape)
    x = (X*data).sum()/total
    y = (Y*data).sum()/total
    col = data[:, int(y)]
    width_x = sqrt(abs((arange(col.size)-y)**2*col).sum()/col.sum())
    row = data[int(x), :]
    width_y = sqrt(abs((arange(row.size)-x)**2*row).sum()/row.sum())
    height = data.max()
    rho = 0.5
    return height, x, y, width_x, width_y, rho



def fitbivarGaussian(data):
    """Returns (height, x, y, width_x, width_y, rho)
    the gaussian parameters of a 2D distribution found by a fit"""
    params = bivarParams(data)
    errorfunction = lambda p: ravel(bivarGaussian(*p)(*indices(data.shape)) -
                                 data)
    p, success = optimize.leastsq(errorfunction, params)
    return p

