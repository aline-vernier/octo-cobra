# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 20:54:11 2015

@author: aline
"""

import matplotlib.pyplot as plt
import numpy as np
from numpy import *





myDirs = ["/home/aline/programming/Python/DM Analysis/15/AtZero",
          "/home/aline/programming/Python/DM Analysis/15/Optimized",
          "/home/aline/programming/Python/DM Analysis/20"]
myLabels = ['DM at 0\n', 'Gen. Alg. converged\n', 'Flat mirror\n']


favColors = [(31, 119, 180), (174, 199, 232), (255, 127, 14), (255, 187, 120),
             (44, 160, 44), (152, 223, 138), (214, 39, 40), (255, 152, 150),
             (148, 103, 189), (197, 176, 213), (140, 86, 75), (196, 156, 148),
             (227, 119, 194), (247, 182, 210), (127, 127, 127), (199, 199, 199),
             (188, 189, 34), (219, 219, 141), (23, 190, 207), (158, 218, 229)]


for i in range(len(favColors)):
    r, g, b = favColors[i]
    favColors[i] = (r / 255., g / 255., b / 255.)

data = []       
plt.close()
for i in range(0, len(myDirs)):
    data.append(
    np.transpose(
    np.loadtxt(myDirs[i] + '/dataAnalysis.txt')))
    

    line1, = plt.plot(data[i][0], data[i][2], 'o', color = favColors[i*2], label = myLabels[i] +(
    'wy = '+ str(min(2*data[i][2]*sqrt(1-data[i][3]**2)))))
    parabCoeff = np.polyfit(data[i][0], data[i][2], 2)
    print(parabCoeff)
    
    polynomial = np.poly1d(parabCoeff)
#    x = range((int)(np.rint(min(data[i][0]))), (int)(np.rint(max(data[i][0]))))
    x = range(-40, 20)
    ys = polynomial(x)
    line2, = plt.plot(x, ys, color = favColors[i*2], label = 'fitted')

plt.xlabel("$z$ (cm)")
plt.ylabel('$\sigma_y$ (um)')
plt.legend(loc = 0, fontsize = 10)

    
plt.savefig('/home/aline/programming/Python/DM Analysis/parabolicFits_y.pdf')
