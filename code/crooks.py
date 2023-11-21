#!/usr/bin/env python3

import sys
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.patches as mpatches
mpl.rcParams['mathtext.fontset'] = 'stix'
mpl.rcParams['font.family'] = 'STIXGeneral'

def gaussian(x,avg,variance):
    y = (1/np.sqrt(2*np.pi*variance))*np.exp(-0.5*np.power(x-avg,2)/variance)
    return y

T=4
bins = int(sys.argv[1])

#names = ['v1_48','v5_48','v10_48','v30_48']
#labels =  ['v1_48','v5_48','v10_48','v30_48']
names = ['v1_48','v5_48','v75_480','v10_48','v15_48','v20_48','v30_48']
labels = ['v1_48','v5_48','v75_480','v10_48','v15_48','v20_48','v30_48']
#names =['v75_480']
colors = ['blue', 'red', 'green', 'orange', 'violet','gold', 'purple', 'brown', 'purple']
patches = []


data_un = []
data_re = []
avg_un = []
avg_re = []
var_un = []
var_re = []

for i in range(len(names)):
    data_un.append(pd.read_csv('results/crooks1_un_'+names[i]+'.dat', delimiter='t', header=None).iloc[:,0])
    data_re.append(pd.read_csv('results/crooks1_re_'+names[i]+'.dat', delimiter='t', header=None).iloc[:,0])
    avg_un.append(np.average(data_un[i]))
    avg_re.append(np.average(data_re[i]))
    var_un.append(np.var(data_un[i]))
    var_re.append(np.var(data_re[i]))
print(avg_un[0])
print(avg_re[0])

x=np.arange(-30,60,0.1)
x1 = np.arange(5,20,0.1)

heights_un=[]
heights_re=[]
borders=[]

fig, ax = plt.subplots(layout='tight')

# ax.set_title('Histogramas de trabajo',fontsize=14)
# ax.set_xlabel('Trabajo', fontsize=10)
ax.grid()
ax.set_xlabel(r'Trabajo $W$',fontsize=10)
ax.set_ylabel(r'ln$\frac{W_{re}}{-W_{un}}$',fontsize=14)

line = mpl.lines.Line2D([],[],color='black', linestyle='-', label = 'Despliegue')
line2 = mpl.lines.Line2D([],[],color='black', linestyle='--', label = 'Repliegue')
lines = [line, line2]

# ax.axhline(0,linestyle='dashed',color='black', linewidth=1)
# ax.axvline(0,linestyle='dashed',color='black', linewidth=1)
#ax.text(-0.5,0.6, 'x=0', rotation=90, fontsize=11)

for i in range(len(names)):
    bins_un = np.histogram_bin_edges(data_un[i],bins='fd')
    bins_re = np.histogram_bin_edges(data_re[i],bins='fd')
    patches.append(mpatches.Patch(color=colors[i], label=labels[i]))
#    bin_heights, bin_borders_un,_ = ax.hist(data_un[i], bins, density=True, histtype='step', color=colors[i])
    bin_heights, bin_borders_un = np.histogram(data_un[i], bins, density=True)
    heights_un.append(bin_heights.max())
#    ax.plot(x,gaussian(x,avg_un[i],var_un[i]), color=colors[i], linewidth=1)
#    bin_heights, bin_borders_re,_ = ax.hist(data_re[i], bins, density=True, histtype='step', color=colors[i], linestyle='--')
    bin_heights, bin_borders_re = np.histogram(data_re[i], bins, density=True)
    heights_re.append(bin_heights.max())
#    ax.plot(x,gaussian(x,avg_re[i],var_re[i]), color=colors[i], linestyle='--', linewidth=1)
    y = T*np.log(gaussian(x1,avg_re[i],var_re[i])/gaussian(x1,avg_un[i],var_un[i]))
    ax.plot(x1,y,color=colors[i])

ax.legend(handles=lines+patches)


plt.show()
#plt.savefig('results/crooks.png', format='png', bbox_inches='tight', dpi=600)
