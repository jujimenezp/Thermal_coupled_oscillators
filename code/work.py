#!/usr/bin/python

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['mathtext.fontset'] = 'stix'
mpl.rcParams['font.family'] = 'STIXGeneral'
mpl.rcParams['agg.path.chunksize'] = 10000

data_pos = pd.read_csv('results/coupled_pos.dat', delimiter='\t')
data_w = pd.read_csv('results/coupled_w.dat', delimiter='\t')
fig = plt.figure(layout='tight')
gs = fig.add_gridspec(2,2)
ax = []
ax.append(fig.add_subplot(gs[0, :]))
ax.append(fig.add_subplot(gs[1, 0]))
ax.append(fig.add_subplot(gs[1, 1]))

for i in range(len(data_pos.columns)-1):
    ax[0].plot(data_pos.iloc[:,0],data_pos.iloc[:,i+1], linewidth=0.5)
ax[1].plot(data_w.iloc[:,0],data_w.iloc[:,1], linewidth=0.5)
#ax[1].plot(data_w.iloc[:,3],data_w.iloc[:,4], linewidth=0.5)
ax[2].plot(data_w.iloc[:,0],data_w.iloc[:,2], linewidth=0.5)

ax[0].grid()
ax[0].set_xticks(np.arange(0, 1000+1, 100))
ax[0].set_yticks(np.arange(-10, 10+1, 1.0))
ax[0].set_xlabel('Time')
ax[0].set_ylabel('Position')

ax[1].grid()
ax[1].set_xticks(np.arange(-10, 0+1, 1.0))
ax[1].set_xlabel('Center position')
ax[1].set_ylabel('Spring Force')

ax[2].grid()
ax[2].set_xlabel('Center Position')
ax[2].set_ylabel('Work')


plt.show()
#plt.savefig('results/coupled_work.png',format='png',bbox_inches='tight',dpi=300)
