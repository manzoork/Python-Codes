# Check description below for excercise details.
"""
Created on Sat Jun 27 22:41:56 2020

@author: Mak
"""

filename = input("Enter file name: ")

if len(filename) < 1:
    fhandle = open("mbox-short.txt")
else:
    fhandle = open(filename)

words = list()
hours = dict()

for line in fhandle:
    line = line.rstrip()
    if line.startswith("From: "):
        continue
    if line.startswith("From "):
        words = line.split()
        hrs = words[5]
        hours[hrs[0:2]] = hours.get(hrs[0:2], 0) + 1

temp_hours = sorted(hours.items())
for k, v in temp_hours:
    print(k, v)
