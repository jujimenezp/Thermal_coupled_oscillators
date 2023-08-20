#!/usr/bin/python3

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('results/gauss.dat',delimiter='\t')
x = data.iloc[:,0]
bins = 200

fig,ax = plt.subplots()
ax.set_title(r'Distribución Gaussiana')
ax.hist(x, bins)
plt.show()
#plt.savefig('results/hist.pdf',format='pdf',bbox_inches='tight')
