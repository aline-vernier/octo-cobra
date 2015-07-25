# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 23:02:52 2015

@author: aline
"""

import FocSpotScript as fss
import os
import numpy as np
from numpy import *
import matplotlib.pyplot as plt

myDir = "/home/aline/programming/Python/DM Analysis/15/AtZero"



f = open(myDir + '/dataAnalysis.txt', 'w')

#f.write("distance\twidth_x\twidth_y\trho\n")

z = []
wx = []
wy = []


for file in os.listdir(myDir):
    if file.endswith(".tiff") and file.startswith("tachefoc"): 
        print(file)
        dist = file.split( "_")[1]
        
        if dist.startswith("moins"):
            print("-" + dist.split("moins")[1])
            f.write("-" + dist.split("moins")[1]+"\t")
            z.append(-float(dist.split("moins")[1]))
        else:
            print(dist)
            f.write(dist + "\t")
            z.append(float(dist))
        
        x, y, width_x, width_y, rho = fss.analysis(myDir + "/"+ file)
        wx.append(4*4.65*width_x)
        wy.append(4*4.65*width_y)
        f.write(str(4*4.65*width_x) +  "\t" + str(4*4.65*width_y) +  "\t" + str(rho) + "\n" )
            

f.close()
plt.close()
plt.plot(z, wx, 'x')
plt.plot(z, wy, 'o')
plt.xlabel("z (cm)")
plt.savefig(myDir + "/plot.png")



