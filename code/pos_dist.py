#!/usr/bin/python3

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.stats import linregress

def gaussian(x, mean, amplitude, standard_deviation):
    return amplitude * np.exp( - (x - mean)**2 / (2*standard_deviation ** 2))

data = pd.read_csv('results/trajectories.dat', header=None, delimiter='\t')

ts = []
xs = []
bins=50
ies = np.linspace(1,4951,50, dtype=int)
fig,ax = plt.subplots(1,2)
for i in ies:
    ts.append(data.iloc[i,0])
    x=data.iloc[i,1:]
    bin_heights, bin_borders, _ = ax[0].hist(x,bins)
    bin_centers = bin_borders[:-1] + np.diff(bin_borders)/2
    popt, pcov = curve_fit(gaussian, bin_centers, bin_heights)
    xs.append(np.power(popt[2],2))

res = linregress(ts, xs)
print(f'slope = {res.slope} +/- {res.stderr}')
print(f'R2 = {res.rvalue}')
t = np.linspace(0,9990,10000)
y = res.intercept + t*res.slope

ax[1].set_title(r'Trayectorias')
ax[1].plot(t,y, color='red')
ax[1].scatter(ts, xs, s=1, color='black')

#plt.show()
plt.savefig('results/pos_dist.pdf',format='pdf',bbox_inches='tight')
