"""
A_01A.py
Date: 2017-05-05
Revised: 2017-06-14

Author Christopher

Condition: Your computer running this code must be connected to the internet. 
Inputs: faf_2017-06-12.xls from https://www.hsi.com.hk/HSI-Net/static/revamp/contents/en/indexes/is/faf.xls
Outputs: Number of issued shares from https://www.hkex.com.hk/eng/invest/company/profile_page_e.asp?WidCoID=5&WidCoAbbName=&Month=&langcode=e
         Each profile page of HSI's component stock is saved as htm
         A final csv file called "A_01A.csv" of the extracted information

"""

from __future__ import print_function

from lxml import html
import requests
from pandas import read_excel
import math

url_base = "https://www.hkex.com.hk/eng/invest/company/profile_page_e.asp?WidCoID="
url_tail = "&WidCoAbbName=&Month=&langcode=e"

search_str = "<br>(as at"

def get_shares(ticker):

   ticker = str(ticker)
   url = url_base + ticker + url_tail
   response = requests.get(url)
   content = response.content
 
   fname = ticker + ".htm"
   fd = open(fname, 'w')
   fd.write(content)
   fd.close()
  
   shares = 0
   with open(fname, 'r') as f:
      for aline in f:
         s = aline.strip()
         #s.replace('?', '')
         s = s.lower()
         if s.find(search_str) != -1:
            h = s.find("&")
            ss = s[0:h]
            g = ss.find("<br>")
            if g :
               ss = ss[0:g]
            s0 = ss.replace(',', '')
            print(ss)
            shares = int(s0)
            break

   return shares


if __name__ == "__main__":

   faf_fn = 'faf_2017-06-12.xls'
   data = read_excel(faf_fn, sheetname = 'latest', skiprows = 6, skip_footer = 30)
   print(data.head())
   tickers = data.iloc[:,0]
   company = data.iloc[:,1]
   faf = data.iloc[:,3]
   freefloat = data.iloc[:,4]    # Column of HSI's free float
   n = len(freefloat)

   fd = open("A_01A.csv", "w")
   fd.write("Code,Stock,FAF,CF\n")
   for i in range(n):
      ff = freefloat[i]
      if math.isnan(ff):
         continue
      ticker = tickers[i]
      a = ticker.find('.')
      ticker = int(ticker[0:4])
      shares = get_shares(ticker)

      s = '%s,%s,%0.2f,%0.4f,%u\n' % (ticker, company[i], faf[i], ff, shares) 
      fd.write(s)
      s = s.replace("," , "|")
      #print('%s|%s|%0.2f|%0.4f|%u' % (ticker, company[i], faf[i], ff, shares))
      print(s)
   fd.close()

     
      











