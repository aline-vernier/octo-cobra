__author__ = 'stephan'

import numpy as np
import matplotlib.pyplot as plt

def Gauss(amp,x0,sigma,x):
    y = amp*np.exp(-np.square(x-x0)/(2.*np.square(sigma)))
    return y

def SumLorentz(A1,A2,A3,fwhm1,fwhm2,fwhm3,f1,f2,f3,f):
    return A1/(1+(4*np.square(f-f1))/np.square(fwhm1))+A2/(1+(4*np.square(f-f2))/np.square(fwhm2))+A3/(1+(4*np.square(f-f3))/np.square(fwhm3))

tableau20 = [(31, 119, 180), (174, 199, 232), (255, 127, 14), (255, 187, 120),
             (44, 160, 44), (152, 223, 138), (214, 39, 40), (255, 152, 150),
             (148, 103, 189), (197, 176, 213), (140, 86, 75), (196, 156, 148),
             (227, 119, 194), (247, 182, 210), (127, 127, 127), (199, 199, 199),
             (188, 189, 34), (219, 219, 141), (23, 190, 207), (158, 218, 229)]

tableau20Edge = list(tableau20)

for i in range(len(tableau20)):
    r, g, b = tableau20[i]
    tableau20[i] = (r / 255., g / 255., b / 255.)

for i in range(len(tableau20Edge)):
    r, g, b = tableau20Edge[i]
    r = r * 1/2
    g = g * 1/2
    b = b * 1/2
    tableau20Edge[i] = (r / 255., g / 255., b / 255.)

##############################################
###
###     Pristinifier for publication
###
#############################################

fig_width_pt = 246.0  # Get this from LaTeX using \showthe\columnwidth
inches_per_pt = 1.0/72.27               # Convert pt to inches
golden_mean = (np.sqrt(5)-1.0)/2.0         # Aesthetic ratio
fig_width = fig_width_pt*inches_per_pt  # width in inches
fig_height =fig_width * 1      # height in inches
fig_size = [fig_width,fig_height]

params = {'font.size' : 10,
          'font.family' : 'Helvetica',
          'font.monospace' : 'Computer Modern',
          'axes.labelsize' : 10,
          'backend' : 'ps',
          'legend.fontsize': 10,
          'xtick.labelsize' : 8,
          'ytick.labelsize' : 8,
          'text.usetex': True,
          'figure.figsize' : fig_size}
plt.rcParams.update(params)

############# Prestinifier END ##############


###########################################
#######                             #######
#######         Upper               #######
#######                             #######
###########################################

##########################
####   Temporal Data  ####
##########################

detuning = (-5.49, -3.83, -2.83, -2.16, -1.33, -0.99, -0.66, -0.33, 0.01, 0.34, 0.67, 1.17, 1.84, 2.84)
atoms = (12, 30, 72, 90, 140, 170)


fig, ax = plt.subplots(2,sharex=True)

det1 = 6;
dashes = [3,1]
fileRaw = 'Gaussian-Temporal/' + str(atoms[5]) + 'Atoms_Temporal_' + str(detuning[det1]) + 'Gamma.csv'
dataRaw = np.genfromtxt(fileRaw, delimiter=',')
xRaw = dataRaw[:,0]
refRaw = dataRaw[:,1]
atomRaw = dataRaw[:,2]
refErr = dataRaw[:,3]
atomErr = dataRaw[:,4]
fileFit = 'Gaussian-Temporal/' + str(atoms[5]) + 'Atoms_TemporalFit_' + str(detuning[det1]) + 'Gamma.csv'
data = np.genfromtxt(fileFit, delimiter=',')
(RefAmp,RefX0,RefSigma) = data[0,:]
(AtomAmp,AtomX0,AtomSigma) = data[1,:]

vfunc = np.vectorize(Gauss)
x = np.linspace(0,600,500)
ref = vfunc(RefAmp,RefX0,RefSigma,x)
atom = vfunc(AtomAmp,AtomX0,AtomSigma,x)
xPlot = x - RefX0
ax[0].plot(xPlot,atom,color=tableau20[2],markeredgecolor=tableau20Edge[0])
ax[0].plot(xPlot,ref,color=tableau20[4],markeredgecolor=tableau20Edge[6])
ax[0].errorbar(xRaw - RefX0,refRaw,fmt='o',yerr=refErr,color='black',markerfacecolor='none',markersize=5)
ax[0].errorbar(xRaw - RefX0,atomRaw,fmt='d',yerr=atomErr,color='black',markerfacecolor='none',markersize=5)
ax[0].plot([RefX0 - RefX0, RefX0 - RefX0],[0, 140],'--',color=tableau20[4])
ax[0].plot([AtomX0 - RefX0, AtomX0 - RefX0],[0, 140],'--',color=tableau20[2])
##########################
####   Temporal Calc  ####
##########################


filename = 'CalculatedPulsesWithChirp/' + str(atoms[5]) + 'Atoms_Pulse_Det_' + str(detuning[det1]) + '_Gamma.csv'
data = np.genfromtxt(filename, delimiter=',')
x = data[:,0]
atom = data[:,1]*RefAmp
ref = data[:,2]*RefAmp
line5, = ax[0].plot(x,atom,'--',color=tableau20[0],markeredgecolor=tableau20Edge[0])
line5.set_dashes(dashes)
# line4 = ax1.plot(x,ref,color=tableau20[6],linewidth=2,markeredgecolor=tableau20Edge[6])


ax[0].set_ylabel('\#photons/run')

ax[0].set_yticks(np.arange(0,0.6,0.1))
x1,x2,y1,y2 = ax[0].axis()
ax[0].axis((200,425,0,0.5))

ax[0].text(210,0.38,'a)')


###########################################
#######                             #######
#######            Lower            #######
#######                             #######
###########################################

det2 = 12;
fileRaw = 'Gaussian-Temporal/' + str(atoms[5]) + 'Atoms_Temporal_' + str(detuning[det2]) + 'Gamma.csv'
dataRaw = np.genfromtxt(fileRaw, delimiter=',')
xRaw = dataRaw[:,0]
refRaw = dataRaw[:,1]
atomRaw = dataRaw[:,2]
refErr = dataRaw[:,3]
atomErr = dataRaw[:,4]
fileFit = 'Gaussian-Temporal/' + str(atoms[5]) + 'Atoms_TemporalFit_' + str(detuning[det2]) + 'Gamma.csv'
data = np.genfromtxt(fileFit, delimiter=',')
(RefAmp,RefX0,RefSigma) = data[0,:]
(AtomAmp,AtomX0,AtomSigma) = data[1,:]
ax[1].plot([RefX0 - RefX0, RefX0 - RefX0],[0, 0.5],'--',linewidth=1,color=tableau20[4]);
ax[1].plot([AtomX0 - RefX0, AtomX0 - RefX0],[0, 0.5],'--',linewidth=1,color=tableau20[2]);

vfunc = np.vectorize(Gauss)
x = np.linspace(0,600,500)
ref = vfunc(RefAmp,RefX0,RefSigma,x)
atom = vfunc(AtomAmp,AtomX0,AtomSigma,x)
xPlot = x - RefX0
line1 = ax[1].plot(xPlot,atom,color=tableau20[2],linewidth=1,markeredgecolor=tableau20Edge[0])
line2 = ax[1].plot(xPlot,ref,color=tableau20[4],linewidth=1,markeredgecolor=tableau20Edge[6])
line3 = ax[1].errorbar(xRaw-RefX0,refRaw,fmt='o',yerr=refErr,color='black',markerfacecolor='none',markersize=5)
line3 = ax[1].errorbar(xRaw-RefX0,atomRaw,fmt='d',yerr=atomErr,color='black',markerfacecolor='none',markersize=5)


##########################
####   Temporal Calc  ####
##########################


filename = 'CalculatedPulsesWithChirp/' + str(atoms[5]) + 'Atoms_Pulse_Det_' + str(detuning[det2]) + '_Gamma.csv'
data = np.genfromtxt(filename, delimiter=',')
x = data[:,0]
atom = data[:,1]*RefAmp
ref = data[:,2]*RefAmp
line5, = ax[1].plot(x,atom,'--',color=tableau20[0],linewidth=1,markeredgecolor=tableau20Edge[0])
line5.set_dashes(dashes)
# line4 = ax[1].plot(x,ref,color=tableau20[6],linewidth=2,markeredgecolor=tableau20Edge[6])


ax[1].set_ylabel(r'\#photons/run')
ax[1].set_xlabel(r'Time [ns]')
ax[1].set_yticks(np.arange(0,0.6,0.1))
x1,x2,y1,y2 = ax[1].axis()
ax[1].axis((-100,100,0,0.5))

ax[1].text(210,0.38,'b)')


outputFile = 'Temporal_Reconstruct.pdf'
plt.tight_layout()
plt.savefig(outputFile)
# plt.savefig(outputFile,bbox_inches='tight')
plt.show()