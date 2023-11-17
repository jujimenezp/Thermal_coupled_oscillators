#!/usr/bin/python

import numpy as np
import pandas as pd
import scipy.interpolate as inter
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['mathtext.fontset'] = 'stix'
mpl.rcParams['font.family'] = 'STIXGeneral'

data = pd.read_csv('results/jarzynski_v10_48.dat', delimiter='\t', header=None)
#data_eq = pd.read_csv('results/jarzynski_eq.dat', delimiter='\t', header=None)

# data.drop_duplicates(0, inplace=True)
# data_eq.drop_duplicates(0, inplace=True)

# f1 = inter.interp1d(data.iloc[:,0], data.iloc[:,2], kind='cubic')
# v1 = f1(data_eq.iloc[:,0])

# f_eq = inter.interp1d(data_eq.iloc[:,0], data_eq.iloc[:,2], kind='cubic')
# v_eq = f_eq(data_eq.iloc[:,0])

# print(f_eq)

fig, ax = plt.subplots(1,2,layout='tight')

ax[0].grid()
ax[0].set_title('Average Force')
ax[0].set_xlabel('Center Position')
ax[0].set_ylabel('Force')
ax[0].plot(data.iloc[:,0],data.iloc[:,1])

ax[1].grid()
ax[1].set_title('Average Work')
ax[1].set_xlabel('Center Position')
ax[1].set_ylabel('Work')
#ax[1].plot(data_eq.iloc[:,0],v1-v_eq)
#ax[1].plot(data_eq.iloc[:,0],data_eq.iloc[:,2], color='red')
ax[1].plot(data.iloc[:,0],data.iloc[:,2], color='blue')

plt.show()
#plt.savefig('results/jarzynski2_T0_25.png',format='png',bbox_inches='tight',dpi=600)
