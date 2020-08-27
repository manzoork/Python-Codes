

tfname = input("Enter file name: ")
fhandle = open(fname)
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
