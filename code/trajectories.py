#!/usr/bin/python3

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('results/trajectories.dat', delimiter='\t')
print(data)
fig,ax = plt.subplots()
ax.set_title(r'Trayectorias')
for i in range(len(data.columns)-1):
    plt.plot(data.iloc[:,0],data.iloc[:,i+1], linewidth=0.5)

#plt.show()
plt.savefig('results/trajectories.pdf',format='pdf',bbox_inches='tight')
