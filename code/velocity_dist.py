#!/usr/bin/python3

import sys
import numpy as np
import pandas as pd
import matplotlib
matplotlib.rcParams['mathtext.fontset'] = 'stix'
matplotlib.rcParams['font.family'] = 'STIXGeneral'
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def gaussian(x, mean, amplitude, variance):
    return amplitude * np.exp( - (x - mean)**2 / (2*variance))


data = pd.read_csv('results/oscillator.dat', delimiter='\t')
#print(data)
t = data['vx'].truncate(after=int(sys.argv[2]))
#t = data['vx']
bins = int(sys.argv[1])
bin_heights, bin_borders, _ = plt.hist(t,bins)
bin_centers = bin_borders[:-1] + np.diff(bin_borders)/2
popt, pcov = curve_fit(gaussian, bin_centers, bin_heights, [0, 40000, 1])
print(popt)
print(pcov)

fig,ax = plt.subplots()
ax.set_title(r'Distribución de velocidades')
ax.set_xlabel('Velocidad [u.a.]')
ax.set_ylabel('Conteo')
x=np.linspace(-5,5,1000)
y = gaussian(x,popt[0],popt[1],popt[2])
textstr = (r'$\mu=(-6\pm 3)e-4$'
           '\n'
           r'$\sigma^2=(9.993\pm 0.003)e-1$')
ax.plot(x,y, label=textstr)
ax.legend(loc='upper right', fontsize=8)
ax.hist(t, bins)

#plt.show()
plt.savefig('results/velocity_hist.pdf',format='pdf',bbox_inches='tight')
