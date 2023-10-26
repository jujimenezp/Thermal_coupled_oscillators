#!/usr/bin/python

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['mathtext.fontset'] = 'stix'
mpl.rcParams['font.family'] = 'STIXGeneral'

data = pd.read_csv('results/avg_w.dat', delimiter='\t')

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
ax[1].plot(data.iloc[:,0],data.iloc[:,2])

#plt.show()
plt.savefig('results/avg_work.png',format='png',bbox_inches='tight',dpi=300)
