# Check description below for details of Excercise
fname = input("Enter file name: ")
try:
    fhandle = open(fname)
except :
    print ("Invalid file name")

lst = list()
wds = list()
for line in fhandle:
    wds = line.split()
    for wd in wds:
        if wd in lst:
            continue
        else:
            lst.append(wd)
lst.sort()
print(lst)            
