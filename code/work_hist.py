#!/usr/bin/python

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['mathtext.fontset'] = 'stix'
mpl.rcParams['font.family'] = 'STIXGeneral'

data = []
data.append(pd.read_csv('results/hist_work_v6_4800.dat', delimiter='\t'))
data.append(pd.read_csv('results/hist_work_v10_48.dat', delimiter='\t'))
data.append(pd.read_csv('results/hist_work_v30_48.dat', delimiter='\t'))
label = ['v = 6/4800', 'v = 10/48', 'v=30/48']

bins = int(sys.argv[1])

fig, ax = plt.subplots(1,3,layout='tight')
for j in range(len(data[0].columns)):
    avg = np.average(data[0].iloc[:,j])
    for i in range(len(data)):
        bin_heights, bin_borders, _ = ax[j].hist(data[i].iloc[:,j]-avg,bins,histtype='step', label=label[i])

fig.suptitle('Work histograms')
fig.text(0.5, 0.01, 'Work', ha='center')
ax[0].grid()
ax[0].set_title(r'$x_{c}=-6$')
ax[1].grid()
ax[1].set_title(r'$x_{c}=-9$')
ax[2].grid()
ax[2].set_title(r'$x_{c}=-3$')
ax[1].legend()

plt.show()
#plt.savefig('results/hist_work.png', format='png',bbox_inches='tight',dpi=300)
