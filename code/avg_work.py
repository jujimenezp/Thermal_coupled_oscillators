#!/usr/bin/python

import numpy as np
import pandas as pd
import scipy.interpolate as inter
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['mathtext.fontset'] = 'stix'
mpl.rcParams['font.family'] = 'STIXGeneral'
mpl.rcParams['figure.figsize'] = 6, 10

data = pd.read_csv('results/jarzynski_v10_48.dat', delimiter='\t', header=None)
#data_eq = pd.read_csv('results/jarzynski_eq.dat', delimiter='\t', header=None)

try:
    p1, p2 = np.split(data,2)
except:
    p1, p2  = np.split(data.iloc[:-1,:],2)

# data.drop_duplicates(0, inplace=True)
# data_eq.drop_duplicates(0, inplace=True)

# f1 = inter.interp1d(data.iloc[:,0], data.iloc[:,2], kind='cubic')
# v1 = f1(data_eq.iloc[:,0])

# f_eq = inter.interp1d(data_eq.iloc[:,0], data_eq.iloc[:,2], kind='cubic')
# v_eq = f_eq(data_eq.iloc[:,0])

# print(f_eq)

fig, ax = plt.subplots(2,1,layout='tight')

ax[0].grid()
ax[0].set_title('Fuerza promedio')
ax[0].set_xlabel('Posición del centro')
ax[0].set_ylabel('Fuerza')
ax[0].plot(p1.iloc[:,0],p1.iloc[:,1], color='blue')
ax[0].plot(p2.iloc[:,0],p2.iloc[:,1], color='red')

ax[1].grid()
ax[1].set_title('Trabajo promedio')
ax[1].set_xlabel('Posición del centro')
ax[1].set_ylabel('Trabajo')
#ax[1].plot(data_eq.iloc[:,0],v1-v_eq)
#ax[1].plot(data_eq.iloc[:,0],data_eq.iloc[:,2], color='red')
ax[1].plot(p1.iloc[:,0],p1.iloc[:,2], color='blue', label = 'despliegue')
ax[1].plot(p2.iloc[:,0],p2.iloc[:,2], color='red', label='repliegue')
ax[1].legend()

#plt.show()
plt.savefig('results/jarzynski_v10_48.png',format='png',bbox_inches='tight',dpi=600)
