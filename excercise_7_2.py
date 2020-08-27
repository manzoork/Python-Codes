fname = input("Enter file name: ")
try:
    fhandle = open(fname)
except :
    print ("Invalid file name")
n = 0
tot = 0
for line in fhandle:
    if line.startswith("X-DSPAM-Confidence:") :
        pos = line.find(' ')
        num = float(line[pos:])
        tot = (tot + num) 
        n = n + 1
avg = tot/n

print("Average spam confidence:",avg)