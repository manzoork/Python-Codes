#  Finding Numbers in a Haystack
# In this assignment you will read through and parse a file with text and numbers. You will extract all the numbers in the file and compute the sum of the numbers
"""
Created on Thu Jul 16 13:53:43 2020

@author: Mak
"""

import re

filename = input("Enter file name: ")

if len(filename) < 1:
    fhandle = open("mbox-short.txt")
else:
    fhandle = open(filename)

fstring = fhandle.read()
num = [int(i) for i in re.findall('[0-9]+',fstring)]
print (sum(num))
