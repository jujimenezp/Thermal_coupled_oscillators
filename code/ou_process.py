#!/usr/bin/python3

import sys
import numpy as np
import pandas as pd
import matplotlib as mpl
mpl.rcParams['mathtext.fontset'] = 'stix'
mpl.rcParams['font.family'] = 'STIXGeneral'
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def expo(t, y0, gamma):
    return y0*np.exp(-gamma*t)

fig, ax = plt.subplots(1,3, layout='tight')
data = pd.read_csv('results/ou_process_r0.1.dat', delimiter='\t')

t = data['t']
v = data['vx']
popt, pcov = curve_fit(expo, t.truncate(after=252), v.truncate(after=252))
print(r'gamma=0.1')
print(popt)
print(pcov)
t_fit = np.linspace(0,100,1000)
v_fit = expo(t_fit,popt[0],popt[1])

ax[0].set_title(r'$\gamma=0.1$')
ax[0].grid()
ax[0].set_xlabel('Tiempo')
ax[0].set_ylabel('Velocidad')
ax[0].scatter(t, v, s=1, color='black')
textstr=(r'$v=v_0 e^{-\gamma t}$'
         '\n'
         r'$\gamma = 0.1059\pm 0.0004$')
ax[0].plot(t_fit,v_fit,color='red',label=textstr)
ax[0].legend(loc='upper right', fontsize=8)

data = pd.read_csv('results/ou_process_r0.5.dat', delimiter='\t')
t = data['t']
v = data['vx']
popt, pcov = curve_fit(expo, t.truncate(after=152), v.truncate(after=152))
print(r'gamma=0.5')
print(popt)
print(pcov)
t_fit = np.linspace(0,100,1000)
v_fit = expo(t_fit,popt[0],popt[1])

ax[1].set_title(r'$\gamma=0.5$')
ax[1].grid()
ax[1].set_xlabel('Tiempo')
ax[1].set_ylabel('Velocidad')
ax[1].set_xlim(0,40)
ax[1].scatter(t, v, s=1, color='black')
textstr=(r'$v=v_0 e^{-\gamma t}$'
         '\n'
         r'$\gamma = 0.504\pm 0.003$')
ax[1].plot(t_fit,v_fit,color='red',label=textstr)
ax[1].legend(loc='upper right', fontsize=8)

data = pd.read_csv('results/ou_process_r1.dat', delimiter='\t')
t = data['t']
v = data['vx']
popt, pcov = curve_fit(expo, t.truncate(after=62), v.truncate(after=62))
print(r'gamma=1')
print(popt)
print(pcov)
t_fit = np.linspace(0,100,1000)
v_fit = expo(t_fit,popt[0],popt[1])

ax[2].set_title(r'$\gamma=1$')
ax[2].grid()
ax[2].set_xlabel('Tiempo')
ax[2].set_ylabel('Velocidad')
ax[2].set_xlim(0,15)
ax[2].scatter(t, v, s=1, color='black')
textstr=(r'$v=v_0 e^{-\gamma t}$'
         '\n'
         r'$\gamma = 1.009\pm 0.006$')
ax[2].plot(t_fit,v_fit,color='red',label=textstr)
ax[2].legend(loc='upper right', fontsize=8)

#plt.show()
plt.savefig('results/ou_process.pdf',format='pdf',bbox_inches='tight')
