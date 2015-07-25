# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 18:16:54 2015

@author: aline
"""
import re
from re import * 
import numpy as np
import scipy.sparse as ssp

myDir = '/home/aline/programming/Python/DM Analysis/Wavefronts/20150710/'


with open(myDir + 'WF_Zonal_PleineEnergie6.txt') as f:
    pupil = f.readlines()[9:] 
    

for i in range(0,len(pupil)):
    pupil[i] = sub(',', '.', sub('\t\t', '\t0.\t', pupil[i]))
    pupil[i] = np.array(map(float, pupil[i].split()))
    print(len(pupil[i]))
pupil = np.array(pupil)

#pupil = np.lib.pad(pupil, max(len(l) for l in pupil), 'minimum')