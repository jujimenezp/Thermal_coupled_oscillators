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

def expo(t, y0, k):
    return y0*np.exp(-k*t/100)

def f_sigma(t, A, k):
    return np.sqrt(A*(1-np.exp(-2*k*t/100)))

bins = int(sys.argv[1])
fig, ax = plt.subplots(layout='tight')
fig2, ax2 = plt.subplots(layout='tight')
data = pd.read_csv('results/O_U_pos.dat', header=None, delimiter='\t')

t=data.iloc[:,0]
avg = []
sigma = []

for i in range(len(t+1)):
    x = data.iloc[i,1:]
    bin_heights, bin_borders = np.histogram(x,bins)
    bin_centers = bin_borders[:-1] +np.diff(bin_borders)/2
    # try:
    #     popt, pcov = curve_fit(gaussian, bin_centers, bin_heights, [5,100,2])
    # except:
    #     print(f'Not using gaussian for t={i} in gamma=0.1')
    #popt=[]; pcov=[]
    avg.append(np.average(x))
    sigma.append(np.std(x))

parms, parms_cov = curve_fit(expo, t, avg, [5,1])
print('\ngamma=400')
print(parms)
print(parms_cov)
t_fit = np.linspace(0,500,1000)
x_fit = expo(t_fit,parms[0],parms[1])

ax.set_title(r'$\gamma=100$, $k=1$, $T=4$')
ax.grid()
ax.set_xlabel('Tiempo')
ax.set_ylabel('Posición')
ax.scatter(t, avg, s=1, color='black', label='Data')
textstr=(r'$\sigma=\sqrt{k_B T/k(1-e^{-2kt/\gamma})}$'
         '\n'
         r'$k = 1.097 \pm 0.001$')
ax.plot(t_fit,x_fit,color='red',label=textstr)
ax.legend(loc='upper right', fontsize=11)

parms2, parms_cov2 = curve_fit(f_sigma, t, sigma, [1, 1])
print(f'\n{parms2}')
print(parms_cov2)
t_fit = np.linspace(0,500,1000)
sigma_fit = f_sigma(t_fit,parms2[0], parms2[1])
ax2.grid()
ax2.set_title(r'$\gamma=100$, $k=1$, $T=4$')
ax2.set_xlabel('Tiempo')
ax2.set_ylabel('Desv. Est. de la posición')
textstr=(r'$\sigma_v=\sqrt{k_B T/k(1-e^{-2k t/\gamma})}$'
         '\n'
         r'$k = 1.12 \pm 0.01$'
         '\n'
         r'$k_B T = 3.98 \pm 0.01$')
ax2.scatter(t,sigma,s=1,color='black')
ax2.plot(t_fit,sigma_fit,label=textstr)
ax2.legend(loc='lower right', fontsize=11)


#plt.show()
fig.savefig('results/O_U1.png',format='png',bbox_inches='tight',dpi=600)
fig2.savefig('results/O_U2.png',format='png',bbox_inches='tight',dpi=600)
