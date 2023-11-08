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
fig, ax = plt.subplots(2,2, layout='tight')
#fig2, ax2 = plt.subplots(1,3, layout='tight')
data = pd.read_csv('results/prueba_r0.01.dat', header=None, delimiter='\t')

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
    avg.append(np.average(vx))
    sigma.append(np.std(vx))

parms, parms_cov = curve_fit(expo, t, avg)
print('\ngamma=0.01')
print(parms)
print(parms_cov)
t_fit = np.linspace(0,250,1000)
v_fit = expo(t_fit,parms[0],parms[1])

ax[0,0].set_title(r'$\gamma=0.01$')
ax[0,0].grid()
ax[0,0].set_xlabel('Tiempo')
ax[0,0].set_ylabel('Promedio de Velocidad')
ax[0,0].scatter(t, avg, s=1, color='black', label='Datos')
textstr=(r'$v=v_0 e^{-\gamma t}$'
         '\n'
         r'$\gamma = 0.01005\pm 0.00001$')
ax[0,0].plot(t_fit,v_fit,color='red',label=textstr)
ax[0,0].legend(loc='upper right', fontsize=8)

parms2, parms_cov2 = curve_fit(f_sigma, t, sigma)
print(f'\n{parms2}')
print(parms_cov2)
t_fit = np.linspace(0,250,1000)
sigma_fit = f_sigma(t_fit,parms2[0], parms2[1])
ax[1,0].grid()
ax[1,0].set_xlabel('Tiempo')
ax[1,0].set_ylabel('Desviación Estándar de Velocidad')
textstr=(r'$\sigma_v=\sqrt{k_B T(1-e^{-2\gamma t})}$'
         '\n'
         r'$\gamma = 0.01021\pm 0.00001$'
         '\n'
         r'$k_B T = 4.0191 \pm 0.0009$')
ax[1,0].scatter(t,sigma,s=0.5,color='black')
ax[1,0].plot(t_fit,sigma_fit,label=textstr)
ax[1,0].legend(loc='lower right', fontsize=7)




data = pd.read_csv('results/prueba_r0.05.dat', header=None, delimiter='\t')

t=data.iloc[:,0]
avg = []
sigma = []

for i in range(len(t+1)):
    vx = data.iloc[i,1:]
    bin_heights, bin_borders = np.histogram(vx,bins)
    bin_centers = bin_borders[:-1] +np.diff(bin_borders)/2
    # try:
    #     popt, pcov = curve_fit(gaussian, bin_centers, bin_heights, [5,10,2])
    # except:
    #     print(f'Not using gaussian for t={i} in gamma=0.5')
    avg.append(np.average(vx))
    sigma.append(np.std(vx))

parms, parms_cov = curve_fit(expo, t, avg)
print('\ngamma=0.05')
print(parms)
print(parms_cov)
t_fit = np.linspace(0,200,1000)
v_fit = expo(t_fit,parms[0],parms[1])

ax[0,1].set_title(r'$\gamma=0.05$')
ax[0,1].grid()
ax[0,1].set_xlabel('Tiempo')
#ax[0,1].set_ylabel('Promedio de Velocidad')
#ax[0,1].set_xlim(0,40)
ax[0,1].scatter(t, avg, s=1, color='black', label='Datos')
textstr=(r'$v=v_0 e^{-\gamma t}$'
         '\n'
         r'$\gamma = 0.05036\pm 0.00001$')
ax[0,1].plot(t_fit,v_fit,color='red',label=textstr)
ax[0,1].legend(loc='upper right', fontsize=8)

parms2, parms_cov2 = curve_fit(f_sigma, t, sigma)
print(f'\n{parms2}')
print(parms_cov2)
t_fit = np.linspace(0,200,1000)
sigma_fit = f_sigma(t_fit,parms2[0], parms2[1])
ax[1,1].grid()
ax[1,1].set_xlabel('Tiempo')
#ax[1,1].set_ylabel('Desviación Estándar de Velocidad')
textstr=(r'$\sigma_v=\sqrt{k_B T(1-e^{-2\gamma t})}$'
         '\n'
         r'$\gamma = 0.05086\pm 0.00008$'
         '\n'
         r'$k_B T = 4.0182 \pm 0.0009$')
ax[1,1].scatter(t,sigma,s=0.5,color='black')
ax[1,1].plot(t_fit,sigma_fit, label=textstr)
ax[1,1].legend(loc='lower right', fontsize=7)

fig.savefig('results/vel_poster1.png',format='png',bbox_inches='tight',dpi=600)
