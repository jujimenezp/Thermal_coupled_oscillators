#!/usr/bin/python

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['mathtext.fontset'] = 'stix'
mpl.rcParams['font.family'] = 'STIXGeneral'
mpl.rcParams['agg.path.chunksize'] = 10000
mpl.rcParams['figure.figsize'] = 6, 10

data_pos = pd.read_csv('results/coupled_pos3.dat', delimiter='\t', header=None)
data_w = pd.read_csv('results/coupled_w3.dat', delimiter='\t', header=None)
try:
    w1, w2 = np.split(data_w,2)
except:
    w1, w2 = np.split(data_w.iloc[:-1,:],2)

print(w2)
# fig = plt.figure(layout='tight')
# gs = fig.add_gridspec(2,2)
# ax = []
# ax.append(fig.add_subplot(gs[0, :]))
# ax.append(fig.add_subplot(gs[1, 0]))
# ax.append(fig.add_subplot(gs[1, 1]))
fig, ax = plt.subplots(2,1,layout='tight')

# for i in range(len(data_pos.columns)-1):
#     ax.plot(data_pos.iloc[:,0],data_pos.iloc[:,i+1], linewidth=0.5)

#ax[0].plot(data_w.iloc[:,0],data_w.iloc[:,1], linewidth=0.5)
ax[0].plot(w1.iloc[:,0],w1.iloc[:,1], linewidth=0.5, color='blue')
ax[0].plot(w2.iloc[:,0],w2.iloc[:,1], linewidth=0.5, color='red')
ax[1].plot(w1.iloc[:,0],w1.iloc[:,2], linewidth=0.5, color='blue', label='despliegue')
ax[1].plot(w2.iloc[:,0],w2.iloc[:,2], linewidth=0.5, color='red', label='repliegue')
ax[1].legend()
# ax.grid()
# ax.set_title('Trayectoria de dos partículas')
# #ax.set_xticks(np.arange(0, 1000+1, 100))
# #ax.set_yticks(np.arange(-10, 10+1, 1.0))
# ax.set_xlabel('Tiempo')
# ax.set_ylabel('Posición')

ax[0].grid()
ax[0].set_title('Fuerza del resorte externo')
#ax[0].set_xticks(np.arange(-10, 0+1, 1.0))
ax[0].set_xlabel(r'Posición del centro $x_c$')
ax[0].set_ylabel('Fuerza')

ax[1].grid()
ax[1].set_title('Trabajo acumulado')
ax[1].set_xticks(np.arange(-12, -3+1, 1.0))
ax[1].set_xlabel(r'Posición del centro $x_c$')
ax[1].set_ylabel('Trabajo')


#plt.show()
plt.savefig('results/Un_work2.png',format='png',bbox_inches='tight',dpi=300)
