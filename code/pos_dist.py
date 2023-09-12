#!/usr/bin/python3

import sys
import numpy as np
import pandas as pd
import matplotlib as mpl
mpl.rcParams['mathtext.fontset'] = 'stix'
mpl.rcParams['font.family'] = 'STIXGeneral'
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.stats import linregress

def gaussian(x, mean, amplitude, standard_deviation):
    return amplitude * np.exp( - (x - mean)**2 / (2*standard_deviation ** 2))

data = pd.read_csv('results/oscillator.dat', header=None, delimiter='\t')

ts = []
xs = []
bins=50
ies = np.arange(2500,10,-25)
fig,ax = plt.subplots(1,2, layout='tight')
cmap = mpl.colormaps.get_cmap('gist_rainbow_r')
color_gradients = cmap(ies/2500)
for i in ies:
    ts.append(data.iloc[i,0])
    x=data.iloc[i,1:]
    bin_heights, bin_borders, _ = ax[0].hist(x,bins,color=color_gradients[int(i/25-1)])
    bin_centers = bin_borders[:-1] + np.diff(bin_borders)/2
    popt, pcov = curve_fit(gaussian, bin_centers, bin_heights)
    xs.append(np.power(popt[2],2))

res = linregress(ts, xs)
print(f'slope = {res.slope} +/- {res.stderr}')
print(f'intercept = {res.intercept} +/- {res.intercept_stderr}')
print(f'R2 = {res.rvalue}')
t = np.linspace(0,9990,10000)
y = res.intercept + t*res.slope
ax[0].set_title('Distribuciones de posición')

ax[1].set_title(r'Varianza vs tiempo')
ax[1].set_xlabel(r'Tiempo [u.a]')
ax[1].set_ylabel(r'Varianza')
textstr=(r'$\sigma^2=2D t+b$'
         '\n'
         r'$D=0.302 \pm 0.001$'
         '\n'
         r'$b=8\pm9$'
         '\n'
         r'$R^2=0.9997$')
ax[1].plot(t,y, color='red', label=textstr)
ax[1].legend(loc='upper left', fontsize=8)
ax[1].scatter(ts, xs, s=1, color='black')

#plt.show()
plt.savefig('results/pos_dist.pdf',format='pdf',bbox_inches='tight')
