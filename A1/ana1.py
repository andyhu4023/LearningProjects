"""
ana1.py
Christopher Ting 2017-03-28
"""

from __future__ import division, print_function
import pandas as pd
import numpy as np

data = pd.read_csv('ana1.csv')
msci_index = data['Index']

m = np.column_stack((np.asarray(data.iloc[0][2:,]), \
                     np.asarray(data.iloc[1][2:,])))

n = len(msci_index)
for i in range(2,n):
   m = np.column_stack((m, np.asarray(data.iloc[i][2:,])))
m = np.matrix(m, dtype=float)

im = np.linalg.inv(m)
nD = im.dot(msci_index)
print(nD)
   





