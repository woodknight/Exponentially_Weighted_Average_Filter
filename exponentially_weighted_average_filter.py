# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 22:16:57 2018

"""
import numpy as np
from matplotlib import pyplot as plt

#%% Generage data
N = 300
sigma = 0.1
data = np.random.random(N)*sigma
data[0] = sigma # make the first point biased

break_idx = int(N/2)
data[break_idx] = -sigma
data[break_idx:] += 1


#%% Exponentially weighted average with bias correction
beta = 0.98
data_filtered = np.zeros(len(data) + 1)
data_filtered_corrected = np.copy(data_filtered)
bias_correction_idx = 0

data_filtered[0] = 0
for i in range(N):
    if (data[i] - data[i-1]) > 0.5:
        data_filtered[i+1] = 0 + (1 - beta) * data[i]
        bias_correction_idx = i
    else:
        data_filtered[i+1] = beta * data_filtered[i] + (1 - beta) * data[i]
    # bias correction    
    data_filtered_corrected[i+1] = data_filtered[i+1] / (1 - beta ** (i+1 - bias_correction_idx))

plt.plot(data, label = 'raw')
plt.plot(data_filtered[1:], label = 'filtered')
plt.plot(data_filtered_corrected[1:], label = 'filtered corrected')
plt.legend()
