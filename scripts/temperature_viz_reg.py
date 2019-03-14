import os
import numpy as np, pandas as pd, matplotlib.pyplot as plt
from jupyterthemes import jtplot

jtplot.style(theme='onedork')

def farenheit(x):
    return 1.8*x + 32

X = np.arange(-50, 51, 10)
Y = farenheit(X)

plt.figure(figsize=(12,8))
plt.scatter(X,Y) 
