import numpy as np
import pandas as pd

data = pd.read_csv('ana1.csv')
msci_index=data['Index']
m = data.ix[:, 2:].T.as_matrix()

nD = np.linalg.inv(m).dot(msci_index)
print(['%.2f' %i for i in nD])

new_data=pd.read_csv('ana1c.csv')
price= new_data['Price']
print('%.3f' % nD.dot(price))