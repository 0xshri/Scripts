#!/usr/bin/env python

import os
import sys
import time
import urllib2
import csv

class neo:
	def Main(self):

		uagent= {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'}


		self.url = "https://www.nseindia.com/content/fo/fo_secban.csv"
		self.data = urllib2.Request(self.url,headers=uagent)
		self.conn = urllib2.urlopen(self.data)
		cr = csv.reader(self.conn)
		for row in cr:
			man = str(row)
			#str1=''.join(str(e) for e in row)
			#print str1

			neo = time.strftime("%d.%m.%Y")
			with open(neo,'a') as f:
				b = f.write(man+"\n")


		set_line = open(neo, 'r').read().splitlines()
		for i in set_line:
			x = i.replace("['","").replace("']","").replace("', '",": ")
			print x
			if 'Date' in x:
				maxx = x.split("Date ")[1].replace(": ","")
				
			with open(maxx+".txt",'a') as fi:
				fi.write(x+"\n")
				

		os.unlink(neo)
			

if __name__ == "__main__":

	if os.name == "nt":
		os.system("cls")

	else:
		os.system("clear")

	banner = '''
\t\t-----------------------------------------------
\t\t| F & O Ban Share List
\t\t| Coded By: Shrinivas 
\t\t| Web: http://blackcoder.info
\t\t-----------------------------------------------
'''

	print banner

	neo().Main()
