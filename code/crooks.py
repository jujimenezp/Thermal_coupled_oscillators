#!/usr/bin/env python3

import sys
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['mathtext.fontset'] = 'stix'
mpl.rcParams['font.family'] = 'STIXGeneral'

def gaussian(x,avg,variance,A):
    y = A*np.exp(-0.5*np.power(x-avg,2)/variance)
    return y

bins = int(sys.argv[1])
data_un_eq = pd.read_csv("results/crooks_un_eq.dat", delimiter='\t', header=None).iloc[:,0]
data_re_eq = pd.read_csv("results/crooks_re_eq.dat", delimiter='\t', header=None).iloc[:,0]

data_un_5_48 = pd.read_csv("results/crooks_un_v5_48.dat", delimiter='\t', header=None).iloc[:,0]
data_re_5_48 = pd.read_csv("results/crooks_re_v5_48.dat", delimiter='\t', header=None).iloc[:,0]

data_un_10_48 = pd.read_csv("results/crooks_un_v10_48.dat", delimiter='\t', header=None).iloc[:,0]
data_re_10_48 = pd.read_csv("results/crooks_re_v10_48.dat", delimiter='\t', header=None).iloc[:,0]

data_un_30_48 = pd.read_csv("results/crooks_un_v30_48.dat", delimiter='\t', header=None).iloc[:,0]
data_re_30_48 = pd.read_csv("results/crooks_re_v30_48.dat", delimiter='\t', header=None).iloc[:,0]

avg_un_eq = np.average(data_un_eq)
avg_re_eq = np.average(data_re_eq)
avg_un_v5 = np.average(data_un_5_48)
avg_re_v5 = np.average(data_re_5_48)
avg_un_v10 = np.average(data_un_10_48)
avg_re_v10 = np.average(data_re_10_48)
avg_un_v30 = np.average(data_un_30_48)
avg_re_v30 = np.average(data_re_30_48)

var_un_eq = np.var(data_un_eq)
var_re_eq = np.var(data_re_eq)
var_un_v5 = np.var(data_un_5_48)
var_re_v5 = np.var(data_re_5_48)
var_un_v10 = np.var(data_un_10_48)
var_re_v10 = np.var(data_re_10_48)
var_un_v30 = np.var(data_un_30_48)
var_re_v30 = np.var(data_re_30_48)

x=np.arange(-5,35,0.1)

heights=[0,1]
borders=[]

fig, ax = plt.subplots(layout='tight')

ax.grid
ax.set_title('Work Histogram')
ax.set_xlabel('Work')
# bin_heights, bin_borders,_ = ax.hist(data_un_eq, bins, label='Unfolding', color='blue', histtype='step')
# heights.append(bin_heights.max())
# bin_heights, bin_borders,_=ax.hist(data_re_eq, bins, label='Refolding', color='red', histtype='step')
# heights.append(bin_heights.max())

bin_heights, bin_borders,_=ax.hist(data_un_5_48, bins, label='Unfolding v=5/48', color='green', histtype='step')
heights.append(bin_heights.max())
bin_heights, bin_borders,_=ax.hist(data_re_5_48, bins, label='Refolding v=5/48', color='orange', histtype='step')
heights.append(bin_heights.max())

bin_heights, bin_borders,_=ax.hist(data_un_10_48, bins, label='Unfolding v=10/48', color='violet', histtype='step')
heights.append(bin_heights.max())
bin_heights, bin_borders,_=ax.hist(data_re_10_48, bins, label='Refolding v=10/48', color='yellow', histtype='step')
heights.append(bin_heights.max())

bin_heights, bin_borders,_=ax.hist(data_un_30_48, bins, label='Unfolding v=30/48', color='blue', histtype='step')
heights.append(bin_heights.max())
bin_heights, bin_borders,_=ax.hist(data_re_30_48, bins, label='Refolding v=30/48', color='red', histtype='step')
heights.append(bin_heights.max())


#ax.plot(x,gaussian(x,avg_un_eq,var_un_eq,heights[0]), color='blue', linewidth=1)
#ax.plot(x,gaussian(x,avg_re_eq,var_re_eq,heights[1]), color='red', linewidth=1)
ax.plot(x,gaussian(x,avg_un_v5,var_un_v5,heights[2]), color='green', linewidth=1)
ax.plot(x,gaussian(x,avg_re_v5,var_re_v5,heights[3]), color='orange', linewidth=1)
ax.plot(x,gaussian(x,avg_un_v10,var_un_v10,heights[4]), color='violet', linewidth=1)
ax.plot(x,gaussian(x,avg_re_v10,var_re_v10,heights[5]), color='yellow', linewidth=1)
ax.plot(x,gaussian(x,avg_un_v30,var_un_v30,heights[6]), color='blue', linewidth=1)
ax.plot(x,gaussian(x,avg_re_v30,var_re_v30,heights[7]), color='red', linewidth=1)

ax.legend()

plt.show()
