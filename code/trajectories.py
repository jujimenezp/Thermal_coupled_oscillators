#!/usr/bin/python3

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('results/coupled.dat', delimiter='\t')
print(data)
fig,ax = plt.subplots()
ax.grid()
# ax.set_title(r'Trajectories')
# ax.set_xlabel('Time')
# ax.set_ylabel('Position')
ax.set_xlabel('Time')
ax.set_ylabel('Position')
for i in range(len(data.columns)-1):
    plt.plot(data.iloc[:,0],data.iloc[:,i+1], linewidth=0.5)

#plt.show()
plt.savefig('results/coupled.png',format='png',bbox_inches='tight',dpi=300)
