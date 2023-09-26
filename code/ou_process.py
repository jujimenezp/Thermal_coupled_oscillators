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
fig, ax = plt.subplots(1,3, layout='tight')
fig2, ax2 = plt.subplots(1,3, layout='tight')
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
    popt=[]; pcov=[]
    popt.append(np.average(vx))
    popt.append(np.var(vx))
    avg.append(popt[0])
    sigma.append(np.sqrt(popt[1]))

parms, parms_cov = curve_fit(expo, t, avg)
print('\ngamma=0.1')
print(parms)
print(parms_cov)
t_fit = np.linspace(0,250,1000)
v_fit = expo(t_fit,parms[0],parms[1])

ax[0].set_title(r'$\gamma=0.1$')
ax[0].grid()
ax[0].set_xlabel('Tiempo')
ax[0].set_ylabel('Velocidad')
ax[0].scatter(t, avg, s=1, color='black', label='Datos')
textstr=(r'$v=v_0 e^{-\gamma t}$'
         '\n'
         r'$\gamma = 0.1059\pm 0.0004$')
ax[0].plot(t_fit,v_fit,color='red',label=textstr)
ax[0].legend(loc='upper right', fontsize=8)

parms2, parms_cov2 = curve_fit(f_sigma, t, sigma)
print(f'\n{parms2}')
print(parms_cov2)
t_fit = np.linspace(0,250,1000)
sigma_fit = f_sigma(t_fit,parms2[0], parms2[1])
ax2[0].grid()
ax2[0].scatter(t,sigma,s=1,color='black')
ax2[0].plot(t_fit,sigma_fit)




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
    popt=[]; pcov=[]
    popt.append(np.average(vx))
    popt.append(np.var(vx))
    avg.append(popt[0])
    sigma.append(np.sqrt(popt[1]))

parms, parms_cov = curve_fit(expo, t, avg)
print('\ngamma=0.5')
print(parms)
print(parms_cov)
t_fit = np.linspace(0,200,1000)
v_fit = expo(t_fit,parms[0],parms[1])

ax[1].set_title(r'$\gamma=0.5$')
ax[1].grid()
ax[1].set_xlabel('Tiempo')
ax[1].set_ylabel('Velocidad')
ax[1].set_xlim(0,40)
ax[1].scatter(t, avg, s=1, color='black', label='Datos')
textstr=(r'$v=v_0 e^{-\gamma t}$'
         '\n'
         r'$\gamma = 0.504\pm 0.003$')
ax[1].plot(t_fit,v_fit,color='red',label=textstr)
ax[1].legend(loc='upper right', fontsize=8)

parms2, parms_cov2 = curve_fit(f_sigma, t, sigma)
print(f'\n{parms2}')
print(parms_cov2)
t_fit = np.linspace(0,200,1000)
sigma_fit = f_sigma(t_fit,parms2[0], parms2[1])
ax2[1].grid()
ax2[1].scatter(t,sigma,s=1,color='black')
ax2[1].plot(t_fit,sigma_fit)




data = pd.read_csv('results/prueba_r0.1.dat', header=None, delimiter='\t')

t=data.iloc[:,0]
avg = []
sigma = []

for i in range(len(t+1)):
    vx = data.iloc[i,1:]
    bin_heights, bin_borders = np.histogram(vx,bins)
    bin_centers = bin_borders[:-1] +np.diff(bin_borders)/2
    #try:
    #    popt, pcov = curve_fit(gaussian, bin_centers, bin_heights, [5,10,2])
    #except:
    #    print(f'Not using gaussian for t={i} in gamma=1')
    popt=[]; pcov=[]
    popt.append(np.average(vx))
    popt.append(np.var(vx))
    avg.append(popt[0])
    sigma.append(np.sqrt(popt[1]))

parms, parms_cov = curve_fit(expo, t, avg)
print('\ngamma=1.0')
print(parms)
print(parms_cov)
t_fit = np.linspace(0,100,1000)
v_fit = expo(t_fit,parms[0],parms[1])

ax[2].set_title(r'$\gamma=1$')
ax[2].grid()
ax[2].set_xlabel('Tiempo')
ax[2].set_ylabel('Velocidad')
ax[2].set_xlim(0,15)
ax[2].scatter(t, avg, s=1, color='black', label='Datos')
textstr=(r'$v=v_0 e^{-\gamma t}$'
         '\n'
         r'$\gamma = 1.009\pm 0.006$')
ax[2].plot(t_fit,v_fit,color='red',label=textstr)
ax[2].legend(loc='upper right', fontsize=8)

parms2, parms_cov2 = curve_fit(f_sigma, t, sigma)
print(f'\n{parms2}')
print(parms_cov2)
t_fit = np.linspace(0,100,1000)
sigma_fit = f_sigma(t_fit,parms2[0], parms2[1])
ax2[2].grid()
ax2[2].scatter(t,sigma,s=1,color='black')
ax2[2].plot(t_fit,sigma_fit)

plt.show()
#plt.savefig('results/vel_dist.pdf',format='pdf',bbox_inches='tight')
