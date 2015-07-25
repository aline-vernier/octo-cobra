# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 16:19:13 2015

@author: aline
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

flatMirror = np.array(mpimg.imread(
"/home/aline/programming/Python/DM Analysis/20/tachefoc_10_5.tiff")).astype(float)/16;

DM0 = np.array(mpimg.imread(
"/home/aline/programming/Python/DM Analysis/15/AtZero/tachefoc_moins5_12.tiff")).astype(float)/16;

DMAlgo = np.array(mpimg.imread(
"/home/aline/programming/Python/DM Analysis/15/Optimized/tachefoc_moins5_6.tiff")).astype(float)/16;

plt.figure(1)
plt.subplot(211)
plt.imshow(flatMirror)
plt.subplot(212)
plt.imshow(DMAlgo) 
plt.show()