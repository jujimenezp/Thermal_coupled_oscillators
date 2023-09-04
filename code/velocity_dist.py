#!/usr/bin/python3

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('results/oscillator.dat', delimiter='\t')
#print(data)
t = data['vx'].truncate(after=int(sys.argv[2]))
bins = int(sys.argv[1])

fig,ax = plt.subplots()
ax.set_title(r'Distribución de velocidades')
ax.hist(t, bins)

plt.show()
#plt.savefig('results/velocity_hist.pdf',format='pdf',bbox_inches='tight')
