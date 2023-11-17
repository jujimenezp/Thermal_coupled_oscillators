#!/usr/bin/env python3

import sys
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['mathtext.fontset'] = 'stix'
mpl.rcParams['font.family'] = 'STIXGeneral'

def gaussian(x,avg,variance,A):
    y = A*np.exp(-0.5*np.power(x-avg,2)/variance)
    return y

bins = int(sys.argv[1])
names = ['v1_48','v5_48','v10_48', 'v15_48','v20_48', 'v30_48']
#names =['v30_48']
colors = ['blue', 'red', 'green', 'orange', 'brown', 'violet']


data_un = []
data_re = []
avg_un = []
avg_re = []
var_un = []
var_re = []

for i in range(len(names)):
    data_un.append(pd.read_csv('results/crooks_un_'+names[i]+'.dat', delimiter='t', header=None).iloc[:,0])
    data_re.append(pd.read_csv('results/crooks_re_'+names[i]+'.dat', delimiter='t', header=None).iloc[:,0])
    avg_un.append(np.average(data_un[i]))
    avg_re.append(np.average(data_re[i]))
    var_un.append(np.var(data_un[i]))
    var_re.append(np.var(data_re[i]))
print(avg_un[0])
print(avg_re[0])

x=np.arange(-30,60,0.1)
x1 = np.arange(-10,10,2)

heights_un=[]
heights_re=[]
borders=[]

fig, ax = plt.subplots(1,2, layout='tight')

ax[0].set_title('Work Histogram')
ax[0].set_xlabel('Work')
ax[1].grid()

for i in range(len(names)):
    bin_heights, bin_borders_un,_ = ax[0].hist(data_un[i], bins, density=True, label=f'Unfolding {names[i]}', histtype='step', color=colors[i])
    heights_un.append(bin_heights.max())
    ax[0].plot(x,gaussian(x,avg_un[i],var_un[i],heights_un[i]), color=colors[i])
    bin_heights, bin_borders_re,_ = ax[0].hist(data_re[i], bins, density=True, label=f'Refolding {names[i]}', histtype='step', color=colors[i], linestyle='--')
    heights_re.append(bin_heights.max())
    ax[0].plot(x,gaussian(x,avg_re[i],var_re[i],heights_re[i]), color=colors[i], linestyle='--')
    y = np.log(gaussian(x1,avg_re[i],var_re[i],heights_re[i])/gaussian(x1,avg_un[i],var_un[i],heights_un[i]))
    ax[1].plot(x1,y,color=colors[i])

ax[0].legend()


plt.show()
#plt.savefig('results/crooks.png', format='png', bbox_inches='tight', dpi=600)
