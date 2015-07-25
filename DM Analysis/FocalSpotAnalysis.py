import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from numpy import unravel_index

from numpy import *
from scipy import optimize
from pylab import *


img=mpimg.imread('/home/aline/programming/Python/DM Analysis/15/tachefoc_moins5_12.tiff')/16;


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

ROIplot = plt.imshow(ROI)




#Fitting

                
def bivarGaussian(height, center_x, center_y, width_x, width_y, rho):
    """Returns a bivariate gaussian function with the given parameters"""
    width_x = float(width_x)
    width_y = float(width_y)
    rho = float(rho)
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


# Fitting

data = ROI;

matshow(data, cmap=cm.gist_earth_r)

params = fitbivarGaussian(data)
fit = bivarGaussian(*params)

contour(fit(*indices(data.shape)), cmap=cm.copper)
ax = gca()
(height, x, y, width_x, width_y, rho) = params

text(0.95, 0.05, """
x : %.1f
y : %.1f
width_x : %.1f
width_y : %.1f
rho : %.lf""" %(x, y, width_x, width_y, rho),
        fontsize=16, horizontalalignment='right',
        verticalalignment='bottom', transform=ax.transAxes)

show()