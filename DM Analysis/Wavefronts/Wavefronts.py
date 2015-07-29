# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 18:16:54 2015

@author: aline
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import parseWF
from parseWF import *

myDir =  os.getcwd()+'/20150710_raw/'

#Parse and covert files to something sensible if they're not already converted
for file in os.listdir(myDir):
    if (file.startswith("WF") and not file.endswith("parsed.txt")): 
        
        parse_WF(myDir + file);
        
#Load parsed files and save to pictures (.tiff)

    
 
for file in os.listdir(myDir):
    pupil = []   
    RMS = 0.
    num = 0.
    if file.endswith("parsed.txt"): 
        with open(myDir + file, 'r') as f: 
            for line in f.readlines():
                pupil.append(
                map(float, line.split()))
            #
            pupil = np.array(pupil)
            flatPupil = pupil.flatten()
            for element in flatPupil:
                if not np.isnan(element):
                    RMS = RMS + element*element
                    num = num + 1

            RMS = np.around(np.sqrt(RMS/num), decimals = 3)
                
            fig, ax = plt.subplots()
            ax.text(25,3, 'RMS = ' + str(1000*RMS) + 'nm', fontsize = 11)

            cax = ax.imshow(pupil, interpolation = 'none', cmap = cm.afmhot )
            
            cbar = fig.colorbar(cax)
            
            #plt.show()
            plt.savefig(os.path.splitext(file)[0] + '_RMS.tiff' )
            plt.cla()
       #file_out.close()



