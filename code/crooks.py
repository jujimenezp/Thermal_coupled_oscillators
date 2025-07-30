#!/usr/bin/env python3

import sys
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.patches as mpatches
mpl.rcParams['mathtext.fontset'] = 'stix'
font = {'family' : 'STIXGeneral',
        'weight' : 'normal',
        'size'   : 22}
mpl.rc('font', **font)
mpl.rcParams['figure.figsize'] = 10, 6


def gaussian(x,avg,variance):
    y = (1/np.sqrt(2*np.pi*variance))*np.exp(-0.5*np.power(x-avg,2)/variance)
    return y

T=4
bins = int(sys.argv[1])

#names = ['v1_48','v5_48','v10_48','v30_48']
#labels =  [r'$v=\frac{1}{48}$',r'$v=\frac{5}{48}$',r'$v=\frac{10}{48}$',r'$v=\frac{30}{48}$']
names = ['v1_48','v5_48','v75_480','v10_48','v15_48','v20_48','v30_48']
labels = [r'$v=\frac{1}{48}$',r'$v=\frac{5}{48}$',r'$v=\frac{75}{480}$',r'$v=\frac{10}{48}$',r'$v=\frac{15}{48}$',r'$v=\frac{20}{48}$',r'$v=\frac{30}{48}$']
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
    data_un.append(pd.read_csv('results/crooks_un_'+names[i]+'.dat', delimiter='t', header=None).iloc[:,0])
    data_re.append(pd.read_csv('results/crooks_re_'+names[i]+'.dat', delimiter='t', header=None).iloc[:,0])
    avg_un.append(np.average(data_un[i]))
    avg_re.append(np.average(data_re[i]))
    var_un.append(np.var(data_un[i]))
    var_re.append(np.var(data_re[i]))
print(avg_un[0])
print(avg_re[0])

x=np.arange(-45,45,0.1)
x1 = np.arange(-7,7,0.1)

heights_un=[]
heights_re=[]
borders=[]

fig, ax = plt.subplots(layout='tight')

ax.set_title('Cumulative Work Histograms',fontsize=22)
#ax.set_xlabel('Work', fontsize=22)
ax.grid()
ax.set_xlabel(r'Work $W$')
ax.set_ylabel(r'ln$\frac{W_{re}}{-W_{un}}$')

line = mpl.lines.Line2D([],[],color='black', linestyle='-', label = 'Uncoupling')
line2 = mpl.lines.Line2D([],[],color='black', linestyle='--', label = 'Coupling')
lines = [line, line2]

ax.axhline(0,linestyle='dashed',color='black', linewidth=1)
ax.axvline(0,linestyle='dashed',color='black', linewidth=1)
ax.text(-0.5,0.4, 'x=0', rotation=90, fontsize=20)

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
    y = np.log(gaussian(x1,avg_re[i],var_re[i])/gaussian(x1,avg_un[i],var_un[i]))
    ax.plot(x1,y,color=colors[i])

ax.legend(handles=patches, fontsize=14, loc ='upper left')


#plt.show()
plt.savefig('paper_images/system2_crooks.png', format='png', bbox_inches='tight', dpi=600)
