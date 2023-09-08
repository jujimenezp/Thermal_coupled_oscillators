#!/usr/bin/python3

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def gaussian(x, mean, amplitude, standard_deviation):
    return amplitude * np.exp( - (x - mean)**2 / (2*standard_deviation ** 2))


data = pd.read_csv('results/ou_process.dat', delimiter='\t')
#print(data)
t = data['vx'].truncate(after=int(sys.argv[2]))
#t = data['vx']
bins = int(sys.argv[1])
bin_heights, bin_borders, _ = plt.hist(t,bins)
bin_centers = bin_borders[:-1] + np.diff(bin_borders)/2
popt, pcov = curve_fit(gaussian, bin_centers, bin_heights)
print(popt)
print(pcov)

fig,ax = plt.subplots()
ax.set_title(r'Distribución de velocidades')
x=np.linspace(-5,5,1000)
y = gaussian(x,popt[0],popt[1],popt[2])
ax.plot(x,y)
ax.hist(t, bins)

#plt.show()
plt.savefig('results/velocity_hist.pdf',format='pdf',bbox_inches='tight')
