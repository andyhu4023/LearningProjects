"""
use_wget.py
Author: Christopher Ting
Date: 2017-05-10
This Python 2.x script allows you to download prices from Webb's site
"""

from __future__ import division, print_function
import wget
import numpy as np
from pandas import read_excel

url_base = "https://webb-site.com/dbpub/pricesCSV.asp?i="

ifn = "Webb_2016-12-30.xlsx"
data = read_excel(ifn)
stock_code = data["Stock Code"]
code2 = data['Webb Code 2']
stype = data["Type"]

n = len(code2)

for i in range(n):
   if np.isnan(code2[i]) == True:
      continue
   if stype[i] != "O":
      continue
   c = int(code2[i])
   url = url_base + str(c)
   ofile = str(stock_code[i]) + ".csv"
   print ('%s %s' % (url, ofile))
   fn =  wget.download(url, out=ofile)


