#!/usr/bin/python3

import sys
import numpy as np
import pandas as pd
import matplotlib as mpl
mpl.rcParams['mathtext.fontset'] = 'stix'
mpl.rcParams['font.family'] = 'STIXGeneral'
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def gaussian(x, mean, amplitude, variance):
    return amplitude * np.exp( - (x - mean)**2 / (2*variance))

def expo(t, y0, gamma):
    return y0*np.exp(-gamma*t)

def f_sigma(t, gamma, A):
    return np.sqrt(A*(1-np.exp(-2*gamma*t)))

bins = int(sys.argv[1])
fig, ax = plt.subplots(layout='tight')
fig2, ax2 = plt.subplots(layout='tight')
data = pd.read_csv('results/overdamped.dat', header=None, delimiter='\t')

t=data.iloc[:,0]
avg = []
sigma = []

for i in range(len(t+1)):
    vx = data.iloc[i,1:]
    bin_heights, bin_borders = np.histogram(vx,bins)
    bin_centers = bin_borders[:-1] +np.diff(bin_borders)/2
    # try:
    #     popt, pcov = curve_fit(gaussian, bin_centers, bin_heights, [5,100,2])
    # except:
    #     print(f'Not using gaussian for t={i} in gamma=0.1')
    popt=[]; pcov=[]
    popt.append(np.average(vx))
    popt.append(np.var(vx))
    avg.append(popt[0])
    sigma.append(np.sqrt(popt[1]))

parms, parms_cov = curve_fit(expo, t, avg)
#print('\ngamma=0.01')
print(parms)
print(parms_cov)
t_fit = np.linspace(0,150,1000)
v_fit = expo(t_fit,parms[0],parms[1])

#ax.set_title(r'$\gamma=0.01$')
ax.grid()
ax.set_xlabel('Time')
ax.set_ylabel('Position')
ax.scatter(t, avg, s=1, color='black', label='Datos')
# textstr=(r'$\sigma=\sqrt{k_B T(1-e^{-2\gamma t})}$'
#          '\n'
#          r'$\gamma = 0.01021\pm 0.00001$')
ax.plot(t_fit,v_fit,color='red')
#ax.legend(loc='upper right', fontsize=6)

parms2, parms_cov2 = curve_fit(f_sigma, t, sigma)
print(f'\n{parms2}')
print(parms_cov2)
t_fit = np.linspace(0,150,1000)
sigma_fit = f_sigma(t_fit,parms2[0], parms2[1])
ax2.grid()
#ax2.set_title(r'$\gamma=0.01$')
ax2.set_xlabel('Time')
ax2.set_ylabel('Position Standard Deviation')
# textstr=(r'$\sigma_v=\sqrt{k_B T(1-e^{-2\gamma t})}$'
#          '\n'
#          r'$\gamma = 0.1005\pm 0.0001$'
#          '\n'
#          r'$k_B T = 4.0191 \pm 0.0009$')
ax2.scatter(t,sigma,s=1,color='black')
ax2.plot(t_fit,sigma_fit)
#ax2.legend(loc='lower right', fontsize=7)


#plt.show()
fig.savefig('results/over1.png',format='png',bbox_inches='tight',dpi=300)
fig2.savefig('results/over.png',format='png',bbox_inches='tight',dpi=300)
