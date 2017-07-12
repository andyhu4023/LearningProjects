"""
A_01B.py
Date: 2017-05-06
Author: Christopher

Inputs: HSI--Index.csv
Output: Plot of PX_LAST and a png file
"""

from __future__ import division, print_function
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime

years = mdates.YearLocator(4,7,31)   # every 4 years with July 31 as anchor
yearsFmt = mdates.DateFormatter('%Y')

fn = 'HSI--Index.csv'
data = pd.read_csv(fn)
dates = pd.to_datetime(data['Date'], format='%Y-%m-%d')
p0 = data['PX_LAST']

n = len(dates)
tdate = ["" for i in range(n)] 
c = 0
for i in range (n):
   if np.isnan(p0[i]):
      continue
   tdate[c] = dates[i]
   c += 1
tdate = tdate[0:c]

fig, ax = plt.subplots(1,1)
lp0 = np.log(p0)
ax.plot(tdate,lp0, color=(144/255,238/255,144/255),alpha=0.01)

ax.xaxis.set_major_locator(years)
ax.xaxis.set_major_formatter(yearsFmt)

fig.autofmt_xdate()

a = dates.tolist
ax.fill_between(tdate, round(lp0.min()), lp0, facecolor=(144/255,238/255,144/255), alpha=0.95)
ax.grid(True)

# Get current size
fig_size = plt.rcParams["figure.figsize"]

plt.ylabel('Log Scale')
plt.grid(b=True, which='major', color='g', alpha=0.5, linestyle='--')

print (fig_size)

# Set figure width to 12 and height to 9
fig_size[0] = 16
fig_size[1] = 8
plt.rcParams["figure.figsize"] = fig_size

plt.title('Hang Seng Index')
plt.savefig('A_01B.png', format = 'png', dpi=300)
plt.show()
plt.close()

