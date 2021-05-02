#!/usr/bin/python3
# TODO Get rid of some of these
import os
from os import path
import sys
import time
import math
import csv

currentDT = math.floor(time.time())
two_weeks = currentDT - 1209600 #60*60*24*14 # number of seconds in 2 weeks
# Get the `reference` values for the products in the DB
references = []

with open('CSV_file_goes_here.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
      if not row: # if the row is empty
        continue
      else:
        references.append(row[0]) # Add the value to the list

# Local directory where pics are stored
localDir = 'local\directory\goes\here'
# localDir = '/Users/caine2003/Desktop'
for f in os.listdir(localDir):
	f = os.path.join(localDir, f) # Creates full directory from file name
	if os.stat(f).st_ctime > two_weeks:
	  if os.path.isfile(f): # Only deals with file types
	  	a = f.split('\\') # For Windows
	  	# a = f.split('/') # For Unix/Linux

	  	# Filtering can be applied here
	  	if "_1." in a[-1]: # Only deal with the last element in the list
	  		continue # Move to the next element since the current doesn't match the wanted criteria
			# TODO delete to file
			# os.remove(f)
	  	else:
			# TODO Check the `references` list for if a substring is contained within
				# if not in list, delete it
	  		print(a[-1])
