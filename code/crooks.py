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
names = ['v5_48', 'v10_48', 'v30_48']
colors = ['blue', 'red', 'green', 'orange', 'violet', 'yellow']

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

x=np.arange(-30,60,0.1)

heights=[]
borders=[]

fig, ax = plt.subplots(layout='tight')

ax.grid
ax.set_title('Work Histogram')
ax.set_xlabel('Work')

for i in range(len(names)):
    bin_heights, bin_borders,_ = ax.hist(data_un[i], bins, label=f'Unfolding {names[i]}', histtype='step', color=colors[2*i])
    heights.append(bin_heights.max())
    ax.plot(x,gaussian(x,avg_un[i],var_un[i],heights[2*i]), color=colors[2*i])
    bin_heights, bin_borders,_ = ax.hist(data_re[i], bins, label=f'Refolding {names[i]}', histtype='step', color=colors[2*i+1])
    heights.append(bin_heights.max())
    ax.plot(x,gaussian(x,avg_re[i],var_re[i],heights[2*i+1]), color=colors[2*i+1])

ax.legend()

#plt.show()
plt.savefig('crooks.png', format='png', bbox_inches='tight', dpi=600)
